import os
import csv
from pathlib import Path

filepath = open("budget_data.csv")

#list to store data
total_month= []
total_Profit_Losses= []
changes_over_period= []
average_of_change=[]
greatest_increase=[]
greatest_decrease=[]
Date =[]

# with open(budget_data.csv) as csvfile
with open("budget_data.csv") as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")

    #reading the header row
    header = next(csvfile)

    for row in csvreader:
        #add total month 
        total_month.append(row[0])
        #add total profit losses
        total_Profit_Losses.append(int(row[1]))

        #change over period 
    for i in range(len(total_Profit_Losses)-1):
        #using the same way as we did in VBA: difference between each row
        changes_over_period.append(total_Profit_Losses[i+1]-total_Profit_Losses[i])
    

#greatest decrease & increase
greatest_decrease = min(changes_over_period)
greatest_increase = max(changes_over_period)

#add the month of greatest decrease & increase 
greatest_decrease_month=changes_over_period.index(min(changes_over_period))+1 
decrease_date=total_month[greatest_decrease_month]     
greatest_increase_month=changes_over_period.index(max(changes_over_period))+1
increase_date=total_month[greatest_increase_month]

print("Financial Analysis")
print("------------------------")
#count month
total_month = len(total_month)
print(f"Total Month: {total_month}")
#total profit/losses
total_Profit_Losses = sum(total_Profit_Losses)
print(f"Total:${total_Profit_Losses}")
#average_of_change
average_of_change = round(sum(changes_over_period)/len(changes_over_period),2)
print(f"Average Change: {average_of_change}")
#greatest decrease
greatest_decrease = str(greatest_decrease)
print(f"Greatest decrease in Profits: {decrease_date} ${greatest_decrease}")
#greatest increase
greatest_increase = str(greatest_increase)
print(f"Greatest increase in Profits: {increase_date} ${greatest_increase}")
    
#output to txt.file
outputfile=Path("../PyBank/analysis/pybank_analysis.txt")

with open(outputfile, 'w') as file:

    file.write = ("Financial Analysis")
    file.write = ("------------------------")
    file.write = (f"Total Month: {total_month}")
    file.write = (f"Total:${total_Profit_Losses}")
    file.write = (f"Average Change: {average_of_change}")
    file.write6 = (f"Greatest decrease in Profits: {decrease_date} ${greatest_decrease}")
    file.write = ((f"Greatest increase in Profits: {increase_date} ${greatest_increase}"))