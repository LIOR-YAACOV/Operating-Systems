import time
import os
import multiprocessing

def secondary(target_number, queue):
    sum = 0
    for i in range(target_number):
        print(i)
        sum += i
        time.sleep(1)
    print(f"Secondary pid is {os.getpid()} and the ppid is {os.getppid()}")
    queue.put(sum)
    
def main():
    queue = multiprocessing.Queue()
    print(f"Current pid is {os.getpid()} and the ppid is {os.getppid()}")
    process = multiprocessing.Process(target=secondary, args=(10, queue))
    process.start()
    print("Main process continues to run while the secondary process is running.")
    print_starting_time = time.time()
    for i in range(40):
        print(f"Main process iteration {i}")
    print_ending_time = time.time()
    print(f"Main process completed in {print_ending_time - print_starting_time} seconds.")
    process.join()
    ret_from_secondary = queue.get()
    print(f"Sum from secondary process is {ret_from_secondary}")
    
    # time.sleep(20)

if __name__ == "__main__":
    main()    