import pandas as pd
import requests
import pandas as pd
from bs4 import BeautifulSoup
from database import DataBase
from typing import List, Dict


class Scraper(DataBase):
    def __init__(self, tag: str = None) -> None:
        self.tag = tag

    def recommendations(self, tag: str) -> pd.DataFrame:
        """
        Function for scraping lubimyczytac.pl. The script will look for recommendations based on tag, and
        provide the first page.
        """
        response = requests.get(f"https://lubimyczytac.pl/ksiazki/t/{tag}")

        soup = BeautifulSoup(response.content, "html.parser")
        result = soup.find_all("a", class_="authorAllBooks__singleTextTitle")
        authors_htmls = soup.find_all("div", class_="authorAllBooks__singleTextAuthor")

        links = ["https://lubimyczytac.pl" + res.get("href") for res in result]
        authors = [author.text for author in authors_htmls]
        titles = list(map(lambda x: x.strip(), [res.text for res in result]))

        df = pd.DataFrame({"title": titles, "author": authors, "link": links})

        return df

    def display(self, title: str = None) -> List[Dict]:
        """
        Function to look for book recommendations from lubimyczytac.pl based on a provided title.
        """
        tag = super().query_db(
            f"""SELECT DISTINCT(genre) FROM books WHERE title LIKE '%{title}%' """
        )[0][0]

        rec = self.recommendations(tag=tag)

        recs = []
        for i in zip(rec.title, rec.author, rec.link):
            d = {}
            d["title"] = i[0]
            d["author"] = i[1]
            d["link"] = i[2]
            recs.append(d)

        return recs
