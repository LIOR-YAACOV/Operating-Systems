import multiprocessing
import requests
import json

def downloader(process_id, url, queue):
    response = requests.get(url).json()
    num_chars = len(json.dumps(response))
    print(f"Process {process_id} Downloaded {num_chars} from {url}")
    queue.put(num_chars)

def main():
    queue = multiprocessing.Queue()
    total_number_of_chars = 0
    urls = [
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/albums",
        "https://jsonplaceholder.typicode.com/photos",
        "https://jsonplaceholder.typicode.com/todos",
        "https://jsonplaceholder.typicode.com/users"
    ]
    
    processes = []
    for i, url in enumerate(urls):
        process = multiprocessing.Process(target=downloader, args=(i, url, queue))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    while not queue.empty():    
        total_number_of_chars += queue.get()
    
    print(f"Total number of chars downloaded is {total_number_of_chars}")

if __name__ == "__main__":
    main()  