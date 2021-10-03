#Pypoll
#In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

#Import modules
import os
import csv
from collections import Counter

#set path for pile
csvpath = os.path.join("Resources","election_data.csv")

# Empty lists for csvdata
voterid= []
county=[]
candidate=[]

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    row = next(csvreader)
    #loop through looking for ....
    for row in csvreader:
        voterid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

# Calculate total votes
total_votes=len(voterid)

# # function to get unique candidates
# candidate_unique = set(candidate)
# print(candidate_unique)

# total votes per candidates
candidate_count = {}
candidate_count = Counter(candidate)

# finding the winner
max_key = max(candidate_count, key=candidate_count.get)

# percent per candidates
percent = ({key: value/total_votes for key, value in candidate_count.items()})

#format percent
#combine candidate_count and percent
# merged = dict(candidate_count.items() + percent.items())
# print(merged)


#print items
print("Election Results")
print("----------------------")
print("Total Votes:"+ " " + str(total_votes))
print("----------------------")
for i in candidate_count:
    print(i, candidate_count[i])
print("----------------------")
print("Winner:" + " " + str(max_key))
print("----------------------")

# Output to text file
# Specify the file to write to
output = os.path.join("Analysis", "PyPoll_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output, 'w') as textfile:
    textfile.write("Election results:")
    textfile.write("\n")
    textfile.write("-------------------------------------")
    textfile.write("\n")
    textfile.write("Total Votes: " + str(total_votes))
    textfile.write("\n")
    textfile.write("-------------------------------------")
    textfile.write("\n")
    for i in candidate_count:
        textfile.write((i, candidate_count(i)))
        textfile.write("\n")
    textfile.write("-------------------------------------")
    textfile.write("\n")
    textfile.write("Winner is " + str(max_key))
    textfile.write("\n")
    textfile.write("-------------------------------------")