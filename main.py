import time
import threading
import upfd
import upfd_c



#Enabling protection written only in Python
upfd.start()

#Enabling protection written only in C
upfd_c.start()

#You will have to choose one of these, 
#because for some reason they conflict :(
#I'm trying to solve this problem.







def main():
    while True:
        print("work")
        time.sleep(1)
        
threading.Thread(target=main).start()