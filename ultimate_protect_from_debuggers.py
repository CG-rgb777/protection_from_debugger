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
    exit()


if True == False:
    sus_num = 1
    os._exit(1)
    exit()
    


def scan_for_sus_process():
    global sus_num
    while True:
        for proc in psutil.process_iter(["name"]):
            try:
                process_name = proc.info["name"]
                if process_name.startswith(("cheatengine", "dumpcap", "wireshark", "capinfos", "captype",  "editcap", "mergecap", "mmdbresolve", "randpkt",  "reordercap",  "sharkd", "text2pcap", "tshark", "uninstall-wireshark", "Wireshark", "ida64", "ida32", "ida96", "x32dbg", "x32dbg-unsigned", "x64dbg", "x64dbg-unsigned", "x96dbg", "x96dbg-unsigned")):
                    sus_num = 1
                    os._exit(1)
                    exit()
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
            exit()
        time.sleep(1)


def check_ctypes_debugger():
    global sus_num
    while True:
        is_debugger_present = ctypes.windll.kernel32.IsDebuggerPresent()
        if is_debugger_present:
            sus_num = 1
            os._exit(1)
            fill_memory()
            exit()
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
            exit()


def check_virtualization():
    global sus_num
    while True:
        if is_virtual_machine():
            sus_num = 1
            os._exit(1)
            fill_memory()
            exit()
        time.sleep(1)


def sanbox_check():
        global sus_num
        directory_path = r"C:\\Users"
        target_folder = "WDAGUtilityAccount"

        while True:
            folders = os.listdir(directory_path)

            if target_folder in folders:
                sus_num = 1
                exit()
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
            exit()
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



def detected_sus_thing():
    global sus_num
    while True:
        if sus_num == 0:
            if sus_num != 1:
                pass
        elif sus_num == 1:
            os._exit(1)
            fill_memory()
            exit()
            if sus_num != 0:
                os._exit(1)
                fill_memory()
                exit()
        else:
            os._exit(1)
            fill_memory()
            exit()
        time.sleep(1)


def printt():
    while True:
        print(1)
        time.sleep(1)


def start_pfd():
    global p1, p2, p3, p4, p5, p6, p7, p8
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
    threading.Thread(target=printt).start()
    return p1, p2, p3, p4, p5, p6, p7, p8

def protection_started_check():
    while True:
        protection_started_num = 1
        time.sleep(10)
        try:
            if not p1.is_alive():
                protection_started_num = 0
                sys.exit()
            if not p2.is_alive():
                protection_started_num = 0
                sys.exit()
            if not p3.is_alive():
                protection_started_num = 0
                sys.exit()
            if not p4.is_alive():
                protection_started_num = 0
                sys.exit()
            if not p5.is_alive():
                protection_started_num = 0
                sys.exit()
            if not p6.is_alive():
                protection_started_num = 0
                sys.exit()
            if not p7.is_alive():
                protection_started_num = 0
                sys.exit()
            if not p8.is_alive():
                protection_started_num = 0
                sys.exit()
        except Exception:
            sys.exit()


        if protection_started_num == 1 and protection_started_num != 0:
            pass
        elif protection_started_num == 0:
            os._exit()
            fill_memory()
            protection_bridge()
            exit()
        else:
            fill_memory()
            time.sleep(1)
            exit()
        time.sleep(10)


def exit_for_protection_bridge():
    os._exit()
    sys.exit()
    exit()
    os.remove(__file__)


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
