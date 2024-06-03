from bs4 import BeautifulSoup
import requests


def parse():
    proxies = {
        'http': 'http://proxy.omgtu:8080',
        'https': 'http://proxy.omgtu:8080'
    }
    url = 'http://imdb.com/chart/top/?ref_=nv_mv_250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    page = requests.get(url,verify=False, headers=headers)
    print(page.status_code)

    soup = BeautifulSoup(page.text, "html.parser")
    block = soup.find_all('li', class_='ipc-metadata-list-summary-item')
    soup2 = BeautifulSoup(page.text, "html.parser")
    # rate = soup.find_all('span', class_='ipc-rating-star')
    movies = {}
    for data in block:
        if (data.find('h3', class_='ipc-title__text')) and data.find('span', class_='ipc-rating-star'):
            name = data.find('h3', class_='ipc-title__text')
            rate = data.find('span', class_='ipc-rating-star')
            movies[name.text] = rate.text[:3]

    return movies
