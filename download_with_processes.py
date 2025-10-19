import multiprocessing
import time
import requests

def downloader(url):
    requests.get(url).json()

def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/albums",
        "https://jsonplaceholder.typicode.com/photos",
        "https://jsonplaceholder.typicode.com/todos",
        "https://jsonplaceholder.typicode.com/users"
    ]
    
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=downloader, args=(url,))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()    
    print(f"Downloaded URLs in {end_time - start_time} seconds.")