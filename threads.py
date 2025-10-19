import threading
import time
from random import randint

def worker(thread_id, text, returns):
    num_sleep = randint(0, 10)
    time.sleep(num_sleep)
    print(f"Thread {thread_id}: {text}, slept for {num_sleep} seconds")
    returns.append(thread_id)
    
def main():
    num_of_threads = 5
    threads = []
    threads_returns = []
    for i in range(num_of_threads):
        thread = threading.Thread(target=worker, args=(i, f"Hello from thread {i}", threads_returns))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    
    print(threads_returns)
      
if __name__ == "__main__":
    main()
