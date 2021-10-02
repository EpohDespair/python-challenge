#PyBank
#Analyzing financial records

#Import modules
import os
import csv

#set path for pile
csvpath = os.path.join("Resources","budget_data.csv")

#Declare variables
# total_months=0
total_revenue=0
prev_revenue_change=0
revenue_change_list=[]
month_change_list=[]
greatest_increase=0
greatest_decrease=0

#open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    print("Financial Analysis")
    print("-------------------")  
    ## THIS IS THE BUG. IF I leave it as is I get the months, but the total goes away. Comment it out and I get total but 0 months. 
    total_months=len(list(csvreader)) 
    print("Total Months:" + str(total_months))
    print("Total:" + str(total_revenue) )  
    index=0
    for row in csvreader:
       if (index==0):
        #    total_months+=1
           total_revenue = total_revenue + int(row[1])
           prev_revenue_change = int(row[1])
           month_change_list = month_change_list + [row[0]]
           index+=1
           continue
      

#   The total number of months included in the dataset
    
   
#   * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
   

#   * The greatest increase in profits (date and amount) over the entire period
    #for row in csvreader:
        

#   * The greatest decrease in profits (date and amount) over the entire period


# Specify the file to write to
output_path = os.path.join("Analysis", "Pybank_analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w') as csvfile:

#     # Initialize csv.writer
#     csvwriter = csv.writer(csvfile, delimiter=',')

#     # Write the first row (column headers)
#     csvwriter.writerow(['Financial Analysis'])

#     # Write the second row
#     csvwriter.writerow(['Total Months', 'Total', 'Average Change','Greatest Increase in Profits','Greatest Decrease in Profits'])      