import os
import csv

months = []
profit_loss = []
budget_change = [0]
total = 0 


# Your task is to create a Python script that analyzes the records to calculate each of the following:
pybank_csv = os.path.join('budget_data.csv')
with open(pybank_csv, newline='', encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    pybank_reader = next(csv_reader, None)
    for row in csv_reader:
        months.append(row[0])
        profit_loss.append(int(row[1]))

# The total number of months included in the dataset
    total_months = len(months)

# The net total amount of "Profit/Losses" over the entire period
    for profit_losses in profit_loss:
        total += profit_losses

# The average of the changes in "Profit/Losses" over the entire period
    for i in range(len(profit_loss)-1):
        budget_change.append(profit_loss[i]- profit_loss[i-1])
    average_change = sum(budget_change)/(len(budget_change)-1)
    
# The greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(profit_loss)
    index_g = profit_loss.index(greatest_increase)
    date1 = months[index_g]


# The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(profit_loss)
    index_d = profit_loss.index(greatest_decrease)
    date2 = months[index_d]



# print out

print("Financial Analysis"),
print("----------------------------"),
print(f"Total Months: {total_months}"),
print(f"Total: ${total}"),
print(f"Average Change: ${average_change}"),
print(f"Greatest Increase in Profits: {date1} (${greatest_increase})"),
print(f"Greatest Decrease in Profits: {date2} (${greatest_decrease})")

# As an example, your analysis should look similar to the one below:

# ```text
 # Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
 # Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
#  ```


