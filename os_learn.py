import time
import os
import multiprocessing

def secondary(target_number):
    for i in range(target_number):
        print(i)
        time.sleep(1)
    print(f"Secondary pid is {os.getpid()} and the ppid is {os.getppid()}")

def main():
    print(f"Current pid is {os.getpid()} and the ppid is {os.getppid()}")
    process = multiprocessing.Process(target=secondary, args=(10,))
    process.start()
    print("Main process continues to run while the secondary process is running.")
    print_starting_time = time.time()
    for i in range(4000):
        print(f"Main process iteration {i}")
    print_ending_time = time.time()
    print(f"Main process completed in {print_ending_time - print_starting_time} seconds.")
    process.join()
    
    # time.sleep(20)

if __name__ == "__main__":
    main()    