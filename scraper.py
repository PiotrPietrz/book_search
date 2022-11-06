import pandas as pd
import requests
import pandas as pd
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, tag: str = None) -> None:
        self.tag = tag

    def recommendations(self, tag: str):
        response = requests.get(f'https://lubimyczytac.pl/ksiazki/t/{tag}')

        soup = BeautifulSoup(response.content, "html.parser")
        result = soup.find_all("a", class_='authorAllBooks__singleTextTitle')
        authors_htmls = soup.find_all(
            "div", class_='authorAllBooks__singleTextAuthor')

        links = ['https://lubimyczytac.pl' + res.get('href') for res in result]
        authors = [author.text for author in authors_htmls]
        titles = list(map(lambda x: x.strip(), [res.text for res in result]))

        df = pd.DataFrame({'title': titles, 'author': authors, 'link': links})

        return df
