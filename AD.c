#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>
#include <process.h>



int started_time_check = 0;


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



unsigned int __stdcall check_time(void *arg) {
    time_t user_time = time(NULL);
    if (user_time == (time_t)(-1)) {
        perror("Ошибка при получении времени");
        return 1;
    }

    time_t program_time = user_time;

    while (1) {
        Sleep(1000);
        program_time++;

        time_t current_time = time(NULL);
        if (current_time == (time_t)(-1)) {
            return 1;
        }

        if (abs((int)(current_time - program_time)) > 2) {
            exit(EXIT_FAILURE);
        }
    }

    return 0;
}


void start_time_check() {
    HANDLE thread_handle;
    unsigned thread_id;

    thread_handle = (HANDLE)_beginthreadex(NULL, 0, check_time, NULL, 0, &thread_id);
    if (thread_handle == NULL) {
        exit(EXIT_FAILURE);
    }

    CloseHandle(thread_handle);
    int started_time_check = 1;
}





int detect_debugger() {
    if(started_time_check == 0) {
        start_time_check();
    }
    
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
