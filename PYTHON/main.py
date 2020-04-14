import os
import csv

total_months = 0
net_amount = 0
monthly_change = 0
month_count = 0
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

csvpath = os.path.join('.', 'PyBank', 'Resources', 'budget_data.csv')

with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    row = next(csvreader)

total_months += 1
net_amount += int(row[1])
greatest_increase = int(row[1])
greatest_increase_month = row[0]
previous_row = int(row[1])

for row in csvreader:
        
#The total number of months included in the dataset
    total_months += 1

#The net total amount of "Profit/Losses" over the entire period
    net_amount += int(row[1])

#The average of the changes in "Profit/Losses" over the entire period
    revenue_change = int(row[1]) - previous_row
    monthly_change.append(revenue_change)
    previous_row = int(row[1])
    month_count.append(row[0])

#The greatest increase in profits (date and amount) over the entire period
if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]

#The greatest decrease in losses (date and amount) over the entire period
if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0] 
            