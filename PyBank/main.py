# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources","budget_data.csv")

# Empty lists
sum_month = []
sum_profit = []
profit_change_in_month = []
 
# Open the CSV
with open(csvpath,newline="", encoding="utf") as budget_data:

    csvreader = csv.reader(budget_data,delimiter=",") 
    header = next(csvreader)  
    for row in csvreader: 
        sum_month.append(row[0])
        sum_profit.append(int(row[1]))
    for i in range(len(sum_profit)-1):
        profit_change_in_month.append(sum_profit[i+1]-sum_profit[i])
        
# Calculte the max and min
max_increase = max(profit_change_in_month)
max_decrease = min(profit_change_in_month)
max_increase_month = profit_change_in_month.index(max(profit_change_in_month)) + 1
max_decrease_month = profit_change_in_month.index(min(profit_change_in_month)) + 1 

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(sum_month)}")
print(f"Total: ${sum(sum_profit)}")
print(f"Average Change: {round(sum(profit_change_in_month)/len(profit_change_in_month),2)}")
print(f"Greatest Increase in Profits: {sum_month[max_increase_month]} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {sum_month[max_decrease_month]} (${(str(max_decrease))})")

# Output path
output = os.path.join("analysis","Financial_Analysis_Summary.txt")
with open(output,"w") as file:
    
# Write the results to the text file 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(sum_month)}")
    file.write("\n")
    file.write(f"Total: ${sum(sum_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(profit_change_in_month)/len(profit_change_in_month),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {sum_month[max_increase_month]} (${(str(max_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {sum_month[max_decrease_month]} (${(str(max_decrease))})")


