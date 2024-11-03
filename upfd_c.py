import threading
import ctypes
import time
import os



def start_on():
    try:
        ADlib = ctypes.CDLL("AD.so") #Don't forget to compile the library into .so; command: gcc -fPIC -shared -o AD.so AD.c -lntdll
    except:
        try:
            ADlib = ctypes.CDLL("./AD.so")
        except:
            print("The protection file cannot be found!\n")
            os._exit(0)
    while True:
        try:
            if ADlib.debug_check() == 1:
                print("detect")
            else:
                print(0)
        except Exception as e:
            print(e)
        time.sleep(1)


def start():
    threading.Thread(target=start_on).start()
