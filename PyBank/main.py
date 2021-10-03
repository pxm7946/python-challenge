# module for reading csv files

import os
import csv
from pathlib import Path

# Set path for files
budget_data_csv=os.path.join("python-challenge/PyBank/Resources/budget_data.csv")

#Declare variables
total_months = []
total_profit = []
profit_changes = 0
monthly_profit_change=[]
previous_value =0


# Open the CSV file
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header or otherwise will count it as another month
    csv_reader=next(csvreader)

    for row in csvreader:

#Total of months and profits/losses
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    print(len(total_months))

# The net total amount of "Profit/Losses" over the entire period

total_profits=[int(x) for x in total_profit]
total_profits_sum=sum(total_profits)
print (total_profits_sum) 

# Changes in "Profit/Losses" over the entire period

for i in range(len(total_profits)-1):

    # Difference between two months and append to monthly profit change
    monthly_profit_change.append(total_profit[i+1]-total_profit[i])

# Obtain the max and min of the monthly profit change list

max_increase_value= max(monthly_profit_change)
max_decrease_value =min(monthly_profit_change)

# Correlate max and min to the proper month list and index from max and min 
# Use plus 1 at the end since month associated with change is the next month

max_increase_month=monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month= monthly_profit_change.index(min(monthly_profit_change)) + 1

#Output files

output_file = os.path.join("financial_analysis_summary.txt")

with open(output_file, "w") as file:

# Write methods to print to Analysis

    file.write("Financial Analysis")
    file.write("\n")
    file.write("-------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits:{total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write (f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")