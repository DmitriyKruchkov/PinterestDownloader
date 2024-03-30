from links_parser import links_parser
from downloader import downloader

if __name__ == "__main__":

    print('Введите количество картинок')
    nums = int(input())
    print('Введите запрос для поиска')
    request = input()
    links = links_parser(nums, request)
    downloader(links)
