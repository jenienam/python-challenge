import os
import csv

months = []
voter_ID = []
county= []
candidate = []
percentage_votes = []
count_votes= 0

pypoll_csv= os.path.join('election_data.csv')
with open(pypoll_csv, newline='', encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    pypoll_reader = next(csv_reader, None)

# The total number of votes cast
    for row in csv_reader
        count_votes += 1

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:
