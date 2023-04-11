import csv
import os
input_path = os.path.join("Resources","budget_data.csv")
total_months = 0
total_profit_loss = 0
total_change = 0
previous_profit_loss = 0
average_change = 0
with open(input_path) as raw_file:
    budget_reader = csv.reader(raw_file)
    header = next(budget_reader)
    for row in budget_reader:
        total_months = total_months + 1
        current_profit_loss = int(row[1])
        total_profit_loss = current_profit_loss + total_profit_loss
        
        
       

    print("Financial Analysis")
    print("-------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: {total_profit_loss}")
    print(f"Average Change: {average_change}")