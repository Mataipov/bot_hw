from pprint import pprint

import requests
from bs4 import BeautifulSoup as BS

URL = "https://renovels.org/novel"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.114 YaBrowser/22.9.1.1095 Yowser/2.5 Safari/537.36"
}


def get_html(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BS(html, "html.parser")
    items = soup.find_all("div", class_="gridItem")
    novels = []
    for item in items:

        novels.append({
            "title": item.find("a", class_='Vertical_card__Sxft_').find("h4").getText(),
            "link": item.find("a", class_='Vertical_card__Sxft_').get("href"),
            "author": item.find("a", class_='Vertical_card__Sxft_').find("p").getText(),

        })

    return novels


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        answer = []
        for page in range(1, 5):
            html = get_html(f"{URL}?page{page}")
            current_page = get_data(html.text)
            answer.extend(current_page)
        pprint(answer)

        return answer
    else:
        raise Exception("Error in parser!")


parser()