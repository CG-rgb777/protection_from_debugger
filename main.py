import time
import threading
import upfd
import upfd_c



#Enabling protection written only in Python
upfd.start()

#Enabling protection written only in C
upfd_c.start()








def main():
    while True:
        print("work")
        time.sleep(1)
        
threading.Thread(target=main).start()
