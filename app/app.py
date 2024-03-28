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

xAxis = input("Enter the stat you want for the x-axis: ").upper()
yAxis = input("Enter the stat you want for the y-axis: ").upper()

abbreviations = {
    "GAMES PLAYED": "GP",
    "GP": "GP",
    "GOALS": "G",
    "G": "G",
    "ASSISTS": "A",
    "A": "A",
    "POINTS": "PTS",
    "PTS": "PTS",
    "PLUS/MINUS": "+/-",
    "+/-": "+/-",
    "PENALTY MINUTES": "PIM",
    "PIM": "PIM",
    "POINT SHARES": "PS",
    "PS": "PS",
    "EVEN STRENGTH GOALS": "EV",
    "POWER PLAY GOALS": "PP",
    "PP": "PP",
    "SHORT HANDED GOALS": "SH",
    "SH": "SH",
    "GAME WINNING GOALS": "GW",
    "GW": "GW",
}

if xAxis in abbreviations:
    xAxis = abbreviations[xAxis]
if yAxis in abbreviations:
    yAxis = abbreviations[yAxis]

# Plotting the data
for i in range(len(csv_stats)):
    plt.scatter(csv_stats[xAxis][i], csv_stats[yAxis][i])  # Plot each point
    plt.text(csv_stats[xAxis][i], csv_stats[yAxis][i], csv_stats['Player'][i])  # Label each point
    
plt.title(yAxis + ' vs ' + xAxis)
plt.xlabel(xAxis)
plt.ylabel(yAxis)
plt.savefig(yAxis + '_vs_' + xAxis + '.png')  # Save the plot as a PNG file
plt.show()
