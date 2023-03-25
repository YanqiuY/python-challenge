#import 
import os
import csv
from pathlib import Path

# filepath open
election_data = os.path.join("../python-challenge/PyPoll/Resources/election_data.csv")

#list to store data
voter_id=[]
Candidate =[]
total_votes=[]
percent_vote=[]
winner =[]

#initialize a variable to count votes of each
Stockham_count = 0
DeGette_count = 0
Doane_count = 0

#initialize a variable to count votes of each
Stockham_percent =0
DeGette_percent = 0
Doane_percent = 0
total_votes_count = 0

#with open() as csvfile
with open(election_data) as csvfile:
    
    #read file
    csvreader = csv.reader(csvfile, delimiter=",")

    #header row read
    total_votes_count += 1

    for row in csvreader :
        #add voter id
        voter_id.append(row[0])

        #add candidate
        Candidate.append(row[2])

        for i in row[2]:
        #set conditionals for candidates column
            if i == "Stockham":
                Stockham_count = 1
            elif i == "DeGette":
                DeGette_count += 1
            elif i == "Doane":
                Doane_count += 1

        #creat a dictionary for candidate
        mydict=dict((row[0],row[2]) for row in csvreader)
        
        #create a dictionary to store candiate name as key and votes
        Results = {"Stockham": Stockham_count, "DeGette": DeGette_count, "Doane": DeGette_count}


#results
print("Election Results")
print("---------------------")
#total votes
total_votes=len(mydict)
print(f"Total Votes: {total_votes}")
print("---------------------")
#percentage of each candidate
Stockham_percent = round((Stockham_count/total_votes_count)*100,2)
DeGette_percent = round((DeGette_count/total_votes_count)*100,2)
Doane_percent = round((Doane_count/total_votes_count)*100,2)
print(f"Charles Casper Stockham: {Stockham_percent}% ({Stockham_count})")
print(f"Diana DeGette: {DeGette_percent}% ({DeGette_count})")
print(f"Raymon Anthony Doane: {Doane_percent}% ({Doane_count})")
print("---------------------")
#winner
Winner = max(Results, key=Results.get)
print(f"Winner: {Winner}")
print("---------------------")

# txt file
outputfile = Path("../python-challenge/PyPoll/analysis/Pypollresults.txt")
with open(outputfile, "w") as file:
    file.write = ("Election Results")
    file.write = ("---------------------")
    file.write = (f"Total Votes: {total_votes}")
    file.write = (f"Charles Casper Stockham: {Stockham_percent}% ({Stockham_count})")
    file.write = (f"Diana DeGette: {DeGette_percent}% ({DeGette_count})")
    file.write = (f"Raymon Anthony Doane: {Doane_percent}% ({Doane_count})")
    file.write = ("---------------------")
    file.write = (f"Winner: {Winner}")
    file.write = ("---------------------")
