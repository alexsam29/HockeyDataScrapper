from app.utils.csv_writer import CSVWriter

from app.utils.scraper import Scraper

URL = "https://www.hockey-reference.com/leagues/NHL_2024_skaters.html"
file_name = "NHL_2024_Stats.csv"

scraper = Scraper(URL)
page = scraper.fetch()

stats_table_header = page.find_all(name="thead")
stats_table_header_rows = stats_table_header[0].find_all(name="tr")
stats_table = page.find_all(name="tbody")
stats_table_rows = stats_table[0].find_all(name="tr")

header_row = []
for data in stats_table_header_rows[1].find_all(name="th"):
    if not data.text == "Rk":
        header_row.append(data.text)

rows = [header_row]
for row in stats_table_rows:
    data_row = []
    for data in row.find_all(name="td"):
        data_row.append(data.text)

    if data_row:
        rows.append(data_row)

writer = CSVWriter(file_name)
writer.write(rows)
