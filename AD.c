#include <stdio.h>
#include <windows.h>
#include <winternl.h>
#include <stdbool.h>



BOOL DebuggerCheck_1();
BOOL CheckIfModuleLoaded_1();
BOOL CheckIfModuleLoaded_2();



BOOL DebuggerCheck_1() {
    if (IsDebuggerPresent()) {
        return TRUE;
    }

    PEB *pPeb = (PEB *)__readgsqword(0x60);
    ULONG ntGlobalFlag = *(ULONG *)((BYTE *)pPeb + 0x68);
    if (ntGlobalFlag & 0x2) {
        return TRUE;
    }


    BOOL remoteDebuggerPresent;
    CheckRemoteDebuggerPresent(GetCurrentProcess(), &remoteDebuggerPresent);
    if (remoteDebuggerPresent) {
        return TRUE;
    }


    HANDLE hProcess = GetCurrentProcess();
    PROCESS_BASIC_INFORMATION pbi;
    ULONG returnLength;


    NtQueryInformationProcess(hProcess, ProcessBasicInformation, &pbi, sizeof(pbi), &returnLength);


    if (pbi.PebBaseAddress) {
        PPEB pPebInfo = pbi.PebBaseAddress;
        ULONG ntGlobalFlagInfo = *(ULONG *)((BYTE *)pPebInfo + 0x68);
        if (ntGlobalFlagInfo & 0x2) {
            return TRUE;
        }
    }

    CONTEXT context;
    context.ContextFlags = CONTEXT_DEBUG_REGISTERS;
    if (GetThreadContext(GetCurrentThread(), &context)) {
        if (context.Dr0 || context.Dr1 || context.Dr2 || context.Dr3) {
            return TRUE;
        }
    }



    HANDLE hToken;
    TOKEN_PRIVILEGES tp;
    DWORD dwSize;

    if (OpenProcessToken(GetCurrentProcess(), TOKEN_QUERY, &hToken)) {
        GetTokenInformation(hToken, TokenPrivileges, NULL, 0, &dwSize);
        GetTokenInformation(hToken, TokenPrivileges, &tp, dwSize, &dwSize);
        for (DWORD i = 0; i < tp.PrivilegeCount; i++) {
            if (tp.Privileges[i].Attributes & SE_PRIVILEGE_ENABLED) {
                if (tp.Privileges[i].Luid.LowPart == 20) {
                    CloseHandle(hToken);
                    return TRUE;
                }
            }
        }
        CloseHandle(hToken);
    }

    return FALSE;
}


BOOL CheckIfModuleLoaded_1() {
    const char *moduleName = "vehdebug-x86_64.dll";
    HMODULE hModule = GetModuleHandleA(moduleName);
    if (hModule != NULL) {
        return TRUE;
    } else {
        return FALSE;
    }
}



BOOL CheckIfModuleLoaded_2() {
    const char *moduleName = "allochook-x86_64.dll";
    HMODULE hModule = GetModuleHandleA(moduleName);
    if (hModule != NULL) {
        return TRUE;
    } else {
        return FALSE;
    }
}




int debug_check() {
    while (1) {

        if (CheckIfModuleLoaded_1()) {
            return 1;
        }

        if (CheckIfModuleLoaded_2()) {
            return 1;
        }

        if (DebuggerCheck_1()) {
            return 1;
        }

        return 0;
        Sleep(666);
    }
}



//gcc -fPIC -shared -o AD.so AD.c -lntdll         - .so
