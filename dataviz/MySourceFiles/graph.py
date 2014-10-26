"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON-like form, visualize in graphs, and plot on Google Maps.

Part II: Take the data we just parsed and visualize it using popular
Python math libraries.
"""

from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np
import parse


MY_FILE = "../data/sample_sfpd_incident_all.csv"


def visualize_days(data_file):
    """Visualize data by day of week"""
    # Create couner, iterate through each row of parsed data, 
    # and count incidents per day of the week
    counter = Counter(item["DayOfWeek"] for item in data_file)

    # Separate out x-axis (days of the week) and y-axis (number of incidents)
    data_list = [ 
                counter["Monday"], 
                counter["Tuesday"], 
                counter["Wednesday"], 
                counter["Thursday"],
                counter["Friday"],
                counter["Saturday"],
                counter["Sunday"]
                ]
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # Assign y-axis data to matplolib plot
    plt.plot(data_list)
    # Create x-axis, and assign labels
    plt.xticks(range(len(day_tuple)), day_tuple)

    # Save the plot as a graph!
    # If you look at new-coder/dataviz/tutorial_source, you should see
    # the PNG file, "Days.png".  This is our graph!
    plt.savefig("Days.png")

    # Close file
    plt.clf()


def visualize_type(data_file):
    """Visualize data by category in a bar graph"""
    # Similar to visualize_days, this returns a dict where it sums the total
    # incidents per Category.
    
    #Create counter to iterate over each line in parsed data
    counter = Counter(item["Category"] for item in data_file)

    #Get labels from counter keys
    labels = tuple(counter.keys())

    #Set label location on x-axis
    xlocations = np.array(range(len(labels))) + 0.5

    #Set width of each bar in the plot
    width = 0.5

    #Assign data to the bar plot
    plt.bar(xlocations, counter.values(), width=width)

    #Assign labels and locations to x-axis
    plt.xticks(xlocations + width /2, labels, rotation=90)

    #Add spacing to avoid cutting off labels
    plt.subplots_adjust(bottom=0.4)

    #Make figure larger
    plt.rcParams['figure.figsize'] = 12,8

    #Save graph
    plt.savefig("Type.png")

    #Close plot file
    plt.clf()

def main():
    parsed_data = parse.parse(MY_FILE, ",")
    #visualize_days(parsed_data)
    visualize_type(parsed_data)


if __name__ == "__main__":
    main()
