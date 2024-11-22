import time
import threading
import ctypes
import os



def start_on():
    try:
        ADlib = ctypes.CDLL("AD.so") #Don't forget to compile the library into .so; command: gcc -fPIC -shared -o AD.so AD.c
    except:
        try:
            ADlib = ctypes.CDLL("./AD.so")
        except:
            print("The protection file cannot be found!\n")
            os._exit(0)
    while True:
        try:
            if ADlib.detect_debugger() == 1:
                os._exit(0)
            elif ADlib.detect_debugger() == 0:
                pass
        except Exception as e:
            os._exit(0)
        time.sleep(1)


def start():
    threading.Thread(target=start_on).start()
