from defi import follow
from concurrent.futures import ThreadPoolExecutor

def main():
    print("TG channel: https://t.me/cryptomicrob\n")

    with ThreadPoolExecutor(max_workers=50) as executor: #Max_workers - потоки
        executor.map(follow, range(76000, 100000)) #ренж - ID пользователей в defi



if __name__ == '__main__':
    main()
