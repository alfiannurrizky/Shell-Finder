import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

with open("urls.txt", "r") as file:
    urls = [line.strip() for line in file.readlines()]
    
with open("shell.txt", "r") as file:
    shells = [line.strip() for line in file.readlines()]

def check_shell(url, shell):
    path = f"{url}/{shell}"
    try:
        res = requests.get(path, timeout=5)
        if res.status_code == 200:
            return f"Found Shell at {path}"
    except requests.RequestException:
        pass
    return None

def findshell():
    print("[*] INFO: Searching...")
    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_path = {
            executor.submit(check_shell, url, shell): (url, shell)
            for url in urls
            for shell in shells
        }
        
        for future in as_completed(future_to_path):
            result = future.result()
            if result:
                print(result)

if __name__ == '__main__':
    findshell()
