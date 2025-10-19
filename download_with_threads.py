import threading
import json
import requests

NUMBER_OF_THREADS = 6
COUNTERS = [0] * NUMBER_OF_THREADS

def downloader(url, thread_id):
    global COUNTERS
    response = requests.get(url).json()
    COUNTERS[thread_id] = len(json.dumps(response))
    print(f"Process {thread_id} Downloaded {COUNTERS[thread_id]} from {url}")
    
def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/albums",
        "https://jsonplaceholder.typicode.com/photos",
        "https://jsonplaceholder.typicode.com/todos",
        "https://jsonplaceholder.typicode.com/users"
    ]
    
    Threads = []
    for i, url in enumerate(urls):
        thread = threading.Thread(target=downloader, args=(url, i))
        thread.start()
        Threads.append(thread)
    
    for thread in Threads:
        thread.join()
    
    total_number_of_chars = sum(COUNTERS)
    print(f"Total number of chars downloaded is {total_number_of_chars}")
    
if __name__ == "__main__":
    main()
