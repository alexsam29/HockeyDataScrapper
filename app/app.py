from table import Table
from utils.csv_writer import CSVWriter
from scraper import Scraper

URL = "https://www.hockey-reference.com/leagues/NHL_2024_skaters.html"
file_name = "NHL_2024_Stats.csv"

scraper = Scraper(URL)
page = scraper.fetch()
table = Table(page)

writer = CSVWriter(file_name)
writer.write(table.getRows())
