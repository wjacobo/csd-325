"""
Name: Walter Jacobo
Course: CSD325 Advanced Python
Assignment: Module 4.2 - High/Low Temperatures
File: sitka_high_low_wj.py
Description: Display Sitka's 2018 high or low temperatures from a CSV file.

Changes made to the original sitka_highs.py:
- Added a menu with Highs, Lows, and Exit choices.
- Read both high (TMAX) and low (TMIN) temperatures from the CSV file.
- Added a blue graph for low temperatures and kept highs red.
- Added a loop so the user can view multiple graphs before exiting.
- Added a goodbye message and a message for invalid menu choices.
"""

import csv
from datetime import datetime
from pathlib import Path
from matplotlib import pyplot as plt


# Keep the data file in the same folder as this program.
filename = Path(__file__).resolve().parent / 'sitka_weather_2018_simple.csv'

# Read the dates and both temperature columns from the supplied CSV file.
dates, highs, lows = [], [], []
with open(filename, newline='', encoding='utf-8') as weather_file:
    reader = csv.reader(weather_file)
    header_row = next(reader)

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        highs.append(int(row[5]))
        lows.append(int(row[6]))


# Show a graph for the selected temperature type.
def show_temperatures(temperatures, label, color):
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, color=color)

    # Format the graph using the style of the original program.
    ax.set_title(f'Daily {label.lower()} temperatures - Sitka, 2018', fontsize=18)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Temperature (F)', fontsize=12)
    fig.autofmt_xdate()
    ax.tick_params(axis='both', which='major', labelsize=10)
    plt.tight_layout()
    plt.show()


# Keep showing the menu until the user chooses Exit.
print('Sitka, Alaska: 2018 Weather')
print('Choose Highs to see daily high temperatures,')
print('Lows to see daily low temperatures, or Exit to quit.')

while True:
    print('\nMenu: Highs | Lows | Exit')
    choice = input('WJ: ').strip().lower()

    if choice in ('highs', 'high', 'h'):
        show_temperatures(highs, 'High', 'red')
    elif choice in ('lows', 'low', 'l'):
        show_temperatures(lows, 'Low', 'blue')
    elif choice in ('exit', 'quit', 'e'):
        print('Thanks for viewing Sitka weather. Goodbye!')
        break
    else:
        print('Please enter Highs, Lows, or Exit.')
