import csv
import os
# create the relative path to the csv file
input_path = os.path.join("PyBank/Resources/budget_data.csv")
total_months = 0
total_profit_loss = 0

total_changes = 0
# open the csv file (similar to opening the text file)
with open(input_path) as raw_file:
    budget_reader = csv.reader(raw_file)
    #establish the header row. Even though 'next' appears, it will actually be the first row. 'Next' moves the cursor down
    header = next(budget_reader)
    for row in budget_reader:
        total_months = total_months + 1
        current_profit_loss = int(row[1])
        
        total_profit_loss = current_profit_loss + total_profit_loss
        

        
    print("Financial Analysis")
    print("____________________")
    print(f"Total Months: {total_months}")
    print(f"Total: {total_profit_loss}")
    print(total_changes)