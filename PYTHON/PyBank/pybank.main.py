import os
import csv

#path
csvpath = os.path.join('budget_data.csv')

#initializing the variables 
total_months = 0
total_revenue =0
changes =[]
date_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

#OpenCSV
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    row = next(csvreader)
    
#totals
    previous_profit = int(row[1])
    total_months = total_months + 1
    total_revenue = total_revenue + int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    for row in csvreader:
        #The total number of months included in the dataset
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])
        
        #The net total amount of "Profit/Losses" over the entire period
        #The average of the changes in "Profit/Losses" over the entire period
        change = int(row[1]) - previous_profit
        changes.append(change)
        previous_profit = int(row[1])
        date_count.append(row[0])
        
        #The greatest increase in profits (date and amount) over the entire period
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        #The greatest decrease in losses (date and amount) over the entire period
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
      
    #average and date
    average_change = sum(changes)/len(changes)

    high = max(changes)
    low = min(changes)

    #print
    print("Financial Analysis")
    print("Total Months:" + str(total_months))
    print("Total Amount:" + str(total_revenue))
    print(average_change)
    print(greatest_increase_month, max(changes))
    print(greatest_decrease_month, min(changes))

    PyBank = open("output.txt","w+")
    PyBank.write("Financial Analysis") 
    PyBank.write('\n' +"Total Months" + str(total_months)) 
    PyBank.write('\n' +"Total Amount" + str(total_revenue)) 
    PyBank.write('\n' +"Average" + str(average_change)) 
    PyBank.write('\n' +greatest_increase_month) 
    PyBank.write('\n' +str(high))
    PyBank.write('\n' +greatest_decrease_month) 
    PyBank.write('\n' +str(low)) 
    



