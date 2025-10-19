import threading
import json
import requests

NUMBER_OF_THREADS = 0
COUNTERS = [0] 

def downloader(url, thread_id):
    global COUNTERS
    response = requests.get(url).json()
    COUNTERS[thread_id] = len(json.dumps(response))
    print(f"Thread {thread_id} Downloaded {COUNTERS[thread_id]} from {url}")
    
def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/albums",
        "https://jsonplaceholder.typicode.com/photos",
        "https://jsonplaceholder.typicode.com/todos",
        "https://jsonplaceholder.typicode.com/users"
    ]
    global NUMBER_OF_THREADS, COUNTERS
    NUMBER_OF_THREADS = len(urls)
    COUNTERS = [0] * NUMBER_OF_THREADS

    threads = []
    for i, url in enumerate(urls):
        thread = threading.Thread(target=downloader, args=(url, i))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    total_number_of_chars = sum(COUNTERS)
    print(f"Total number of chars downloaded is {total_number_of_chars}")
    
if __name__ == "__main__":
    main()
