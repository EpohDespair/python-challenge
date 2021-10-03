# PyBank
# Analyzing financial records

# Import modules
import os
import csv

# set path for pile
csvpath = os.path.join("Resources","budget_data.csv")

# lists to organize data 
months = []
revenue = []
revenue_change = []

# open csv file
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    row = next(csvreader)

    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))

# calculate  months
total_months=len(months) 

# set variables for revenue calculations
total_revenue = 0
month_count = 0
current_month_rev = 0
prev_month_rev = 0
total_change = 0

# loop through revenue and calculate variables
for r in range(len(revenue)):
    #total revenue
    total_revenue += revenue[r]
    # calculating change in revenue
    current_month_rev = int(revenue[r])
    total_change += current_month_rev
    month_count += 1
    if month_count == 1:
        prev_month_rev = current_month_rev
    else:
        total_change = current_month_rev - prev_month_rev
        revenue_change.append(total_change)
        prev_month_rev = current_month_rev
# greatest increase and decrease in revenue change
    #for x in range(total_change):
        # print(greatest_increase)
        # greatest_decrease = min(total_change)
        # print(greatest_decrease)
        # if revenue[x] == greatest_increase:
        #     increase_month = months[x]
        # elif revenue[x] == greatest_decrease:
        #     decrease_month = months[x]
#sum and avg change in revenue
sum_changes = sum(revenue_change)
avg_change = round(sum_changes/total_months, 2)

#print out deliverables
print("Financial Analysis")
print("-------------------")  
print("Total months:" + str(total_months))
print("Total:" + str(total_revenue))   
print("Average Change:" + str(avg_change))  
# print("Greatest Increase:" + str(increase_month) + " " + str(greatest_increase))
# print("Greatest Decrease:" + str(decrease_month) + " " + str(greatest_decrease))
# output file
output = os.path.join("Analysis", "PyBank_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output, 'w') as textfile:
    output.write("Financial Analysis")
    output.write("----------------------")
    output.write("Total months:", str(total_months))
    output.write("Total:", str(total_revenue))
    print("Average Change:", str(avg_change))