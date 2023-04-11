import csv

total_volume = 0

with open('budget_data.csv', encoding="utf8") as f:
        csv_reader = csv.reader(f)
# skip the header
        next(csv_reader)
# calculate total whatever        
for line in csv_reader:
                total_volume += float(line[1])