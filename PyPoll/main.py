# Modules
import os
import csv 

# Set path for file
csvpath = os.path.join("Resources","election_data.csv")

# Define variable
Sum_of_Votes = 0 
Charles_Casper_Stockham_votes = 0
Diana_DeGette_votes = 0
Raymon_Anthony_Doane_votes = 0

# Open the CSV and store the data
with open(csvpath,newline="", encoding="utf-8") as election_data:
    csvdata = csv.reader(election_data,delimiter=",") 
    header = next(csvdata)     
    for row in csvdata: 
        Sum_of_Votes +=1
        if row[2] == "Charles Casper Stockham": 
            Charles_Casper_Stockham_votes +=1
        elif row[2] == "Diana DeGette":
            Diana_DeGette_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            Raymon_Anthony_Doane_votes +=1

 # Make Directory
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [Charles_Casper_Stockham_votes, Diana_DeGette_votes,Raymon_Anthony_Doane_votes]

# Find the winner 
candidates_and_votes = dict(zip(candidates,votes))
key = max(candidates_and_votes, key=candidates_and_votes.get)

# Vote percentage
Charles_Casper_Stockham_percent = (Charles_Casper_Stockham_votes/Sum_of_Votes) *100
Diana_DeGette_percent = (Diana_DeGette_votes/Sum_of_Votes) * 100
Raymon_Anthony_Doane_percent = (Raymon_Anthony_Doane_votes/Sum_of_Votes)* 100

# Print the results
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {Sum_of_Votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {Charles_Casper_Stockham_percent:.3f}% ({Charles_Casper_Stockham_votes})")
print(f"Diana DeGette: {Diana_DeGette_percent:.3f}% ({Diana_DeGette_votes})")
print(f"Raymon Anthony Doane: {Raymon_Anthony_Doane_percent:.3f}% ({Raymon_Anthony_Doane_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# Output path
output = os.path.join("analysis","Election_Results_Summary.txt")

with open(output,"w") as file:

# Write the results to the text file 
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {Sum_of_Votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {Charles_Casper_Stockham_percent:.3f}% ({Charles_Casper_Stockham_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {Diana_DeGette_percent:.3f}% ({Diana_DeGette_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {Raymon_Anthony_Doane_percent:.3f}% ({Raymon_Anthony_Doane_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")



