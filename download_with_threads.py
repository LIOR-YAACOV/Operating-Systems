import threading
import time
import requests

def downloader(url, thread_id, download_times_dict):
    start = time.time()
    requests.get(url).json()
    end = time.time()
    download_times_dict[thread_id] = end-start
    
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
    download_time_dict = {}
    for i, url in enumerate(urls):
        thread = threading.Thread(target=downloader, args=(url, i, download_time_dict))
        thread.start()
        Threads.append(thread)
    
    for thread in Threads:
        thread.join()
    
    for thread_id, download_time in download_time_dict.items():
        print(f"Thread {thread_id} took {download_time} seconds to download.")
        
if __name__ == "__main__":
    main()