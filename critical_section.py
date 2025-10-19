import threading
import time

COUNTER = 0

def worker():
    global COUNTER
    for i in range(10000):
        temp = COUNTER
        temp += 1
        #forced context switch
        time.sleep(0.00000001)
        COUNTER = temp

def main():
    thread_1 = threading.Thread(target=worker)
    thread_2 = threading.Thread(target=worker)
    thread_3 = threading.Thread(target=worker)
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_1.join()
    thread_2.join()
    thread_3.join()
    
    print(COUNTER)

if __name__ == "__main__":
    main()

