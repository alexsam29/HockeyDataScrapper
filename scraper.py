import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, url):
        """
        Initialize the Scraper class with a URL.

        Args:
            url (str): The URL of the webpage to scrape.
        """
        self.url = url

    def fetch(self):
        """
        Fetch the webpage content and parse it using BeautifulSoup.

        Returns:
            BeautifulSoup: The parsed HTML content of the webpage.
        """
        page = requests.get(self.url)
        return BeautifulSoup(page.text, "html.parser")
