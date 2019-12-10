# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

print("Election Results")
print("----------------------------")

class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0
        self.percent = 0

with open(csvpath, 'r', encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    data = list(csvreader)
    total = len(data)
    #prepare the poll list
    poll = [Candidate("Khan"), Candidate("Correy"),Candidate("Li"),Candidate("O'Tooley")]
    #calculate votes
    for row in data:
        for candidate in poll:
            if(row[2] == candidate.name): candidate.votes += 1
    #calculate percentage
    for candidate in poll:
        candidate.percent = ((candidate.votes * 100) / total)
    #find winner
    winner = poll[0]        
    for candidate in poll:
        if (candidate.percent > winner.percent): winner = candidate 
        
print("Total Votes: " + str(total))
print("----------------------------")
for candidate in poll:
    print("{}: {:.3f}% ({:d})".format(candidate.name,candidate.percent,candidate.votes))
print("----------------------------")
print("Winner: " + winner.name)
print("----------------------------")
