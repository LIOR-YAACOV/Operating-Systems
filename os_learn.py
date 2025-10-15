import time
import os
import multiprocessing

def secondary(target_number):
    for i in range(target_number):
        print(i)
    print(f"Secondary pid is {os.getpid()} and the ppid is {os.getppid()}")

def main():
    print(f"Current pid is {os.getpid()} and the ppid is {os.getppid()}")
    process = multiprocessing.Process(target=secondary, args=(10,))
    process.start()
    process.join()
    print(1)
    print(2)
    
    # time.sleep(20)

if __name__ == "__main__":
    main()    