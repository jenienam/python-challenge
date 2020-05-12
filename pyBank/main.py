import os
import csv

months = []
profit_loss = []
budget_change = 0
total = 0 



# Your task is to create a Python script that analyzes the records to calculate each of the following:
pybank_csv = os.path.join('budget_data.csv')
with open(csvpath, newline='', encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(pybank_csv, None)
    for row in csv_reader:
    months.append(row[0])
    profit_loss.append(int(row[1]))
# The total number of months included in the dataset
    total_months = len(months)
# The net total amount of "Profit/Losses" over the entire period
    for profit_losses in profit_loss:
        total +=profit_losses
# The average of the changes in "Profit/Losses" over the entire period
    for i in range len(profit_loss):
        budget_change.append(profit_loss[i]- profit_loss[i-1])
    average_change = budget_change/(len(budget_change))
# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period

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

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.


# Define the function and have it accept the 'wrestler_data' as its sole parameter
def print_totals(budget_data):
    # For readability, it can help to assign your values to variables with descriptive names
    dates = int(budget_data[0])
    profit_losses= int(budget_data[1])

# The total number of months included in the dataset
total_months = wins
   
# The net total amount of "Profit/Losses" over the entire period

    # Win percent can be found by dividing the the total wins by the total matches and multiplying by 100
    total_percent = sum(losses)

    # Loss percent can be found by dividing the total losses by the total matches and multiplying by 100
    loss_percent = (losses / total_matches) * 100

    # Draw percent can be found by dividing the total draws by the total matches and multiplying by 100
    draw_percent = (draws / total_matches) * 100

    # If the loss percentage is over 50, type_of_wrestler is "Jobber". Otherwise it is "Superstar".
    if loss_percent > 50:
        type_of_wrestler = "Jobber"
    else:
        type_of_wrestler = "Superstar"

    # Print out the wrestler's name and their percentage stats
    print(f"Stats for {name}")
    print(f"WIN PERCENT: {str(win_percent)}")
    print(f"LOSS PERCENT: {str(loss_percent)}")
    print(f"DRAW PERCENT: {str(draw_percent)}")
    print(f"{name} is a {type_of_wrestler}")


# Read in the CSV file
with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if name_to_check == row[0]:
            print_percentages(row)

