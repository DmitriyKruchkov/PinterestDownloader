import asyncio
from time import time

from downloader import downloader
from links_parser import links_parser


def main():
    print('Введите количество картинок')
    nums = int(input())
    print('Введите запрос для поиска')
    request = input()
    links = links_parser(nums, request)
    asyncio.run(downloader(links))


if __name__ == "__main__":
    t0 = time()
    main()
    print(f'{time() - t0} seconds')
