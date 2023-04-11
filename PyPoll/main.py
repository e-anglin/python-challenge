import csv
import os
input_path = os.path.join("PyPoll/Resources/election_data.csv")
Charles = 0
Diana  = 0
Raymon = 0
with open(input_path) as raw_file:
    polling_reader = csv.reader(raw_file)
    #establish the header row. Even though 'next' appears, it will actually be the first row. 'Next' moves the cursor down
    header = next(polling_reader)
    for row in polling_reader:
        Charles = Charles + 1
print("Election Results")
print(Charles)