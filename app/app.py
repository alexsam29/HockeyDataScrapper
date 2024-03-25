from utils.csv_reader import CSVReader
from table import Table
from utils.csv_writer import CSVWriter
from scraper import Scraper
import matplotlib.pyplot as plt
import numpy as np

URL = "https://www.hockey-reference.com/leagues/NHL_2024_skaters.html"
file_name = "NHL_2024_Stats.csv"

scraper = Scraper(URL)
page = scraper.fetch()
table = Table(page)

writer = CSVWriter(file_name)
writer.write(table.getRows())

reader = CSVReader(file_name)
csv_stats = reader.read()

# Plotting the data
for i in range(len(csv_stats)):
    plt.scatter(csv_stats['GP'][i], csv_stats['G'][i])  # Plot each point
    plt.text(csv_stats['GP'][i], csv_stats['G'][i], csv_stats['Player'][i])  # Label each point
    
plt.title('Goals per Game')
plt.xlabel('Games Played')
plt.ylabel('Goals')
plt.savefig("GPG.png")  # Save the plot as a PNG file
plt.show()
