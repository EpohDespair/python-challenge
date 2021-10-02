#Pypoll
#In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

#Import modules
import os
import csv

#set path for pile
csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    #loop through looking for ....
    for row in csvreader:



# Specify the file to write to
output_path = os.path.join("Analysis", "PyPoll_analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Election Results'])

    # Write the second row
    csvwriter.writerow(['Total Votes', '', '','','Winner'])      