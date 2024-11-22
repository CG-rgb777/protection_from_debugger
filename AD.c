#include <windows.h>
#include <stdio.h>

int check_is_debugger_present() {
    return IsDebuggerPresent() ? 1 : 0;
}

int check_remote_debugger() {
    BOOL debugger_present = FALSE;
    if (CheckRemoteDebuggerPresent(GetCurrentProcess(), &debugger_present)) {
        return debugger_present ? 1 : 0;
    }
    return 0;
}

int check_hardware_breakpoints() {
    CONTEXT ctx;
    HANDLE hThread = GetCurrentThread();
    memset(&ctx, 0, sizeof(CONTEXT));
    ctx.ContextFlags = CONTEXT_DEBUG_REGISTERS;

    if (GetThreadContext(hThread, &ctx)) {
        if (ctx.Dr0 || ctx.Dr1 || ctx.Dr2 || ctx.Dr3) {
            return 1;
        }
    } else {
    }
    return 0;
}

int check_execution_time() {
    LARGE_INTEGER start, end, freq;
    if (!QueryPerformanceFrequency(&freq)) {
        return 0;
    }
    QueryPerformanceCounter(&start);

    for (volatile int i = 0; i < 1000000; i++) {}

    QueryPerformanceCounter(&end);
    double elapsed_time = (double)(end.QuadPart - start.QuadPart) / freq.QuadPart;

    return elapsed_time > 0.05 ? 1 : 0; 
}





int CheckIfModuleLoaded_1() {
    const char *moduleName = "vehdebug-x86_64.dll";
    HMODULE hModule = GetModuleHandleA(moduleName);
    if (hModule != NULL) {
        return 1;
    } else {
        return 0;
    }
}

int CheckIfModuleLoaded_2() {
    const char *moduleName = "allochook-x86_64.dll";
    HMODULE hModule = GetModuleHandleA(moduleName);
    if (hModule != NULL) {
        return 1;
    } else {
        return 0;
    }
}



int detect_debugger() {
    if (check_is_debugger_present() ||
        check_remote_debugger() ||
        check_hardware_breakpoints() ||
        check_execution_time() ||
        CheckIfModuleLoaded_1() ||
        CheckIfModuleLoaded_2()) {
        return 1;
    }
    return 0;
}
