# Module for reading csv file

import os
import csv
from pathlib import Path 

#Set path for files
election_data_csv=os.path.join("python-challenge/PyPoll/Resources/election_data.csv")

# Declare variables
total_votes=0
k_votes=0
c_votes=0
li_votes=0
o_votes=0

# Open csv in default mode 
with open (election_data_csv, newline="", encoding="utf-8") as elections:

    #Store data under the csv reader variable
    csvreader=csv.reader(elections, delimiter=",")

    #Skip the header to get to actual values
    header=next(csvreader)
    #Go through each row in csv
    for row in csvreader:

            #Count voter ID and create variable
            total_votes +=1

            #Count times that name appears and store in list
            if row[2]== "Khan":
                k_votes +=1
            elif row[2] == "Correy":
                c_votes +=1
            elif row[2] =="Li":
                li_votes +=1
            elif row[2] == "O'Tooley":
                o_votes +=1


# Dictionary to hold candidates names

candidates =[
    "Khan",
    "Li", 
    "Correy", 
    "O'Tooley"]

# Dictionary to hold votes 
votes = [
    k_votes,
    c_votes,
    li_votes,
    o_votes]

#Zip the list of candidate (key) and the total votes (value)
dict_candidates_and_votes=dict(zip(candidates,votes))

#Find winner with max function
key= max (dict_candidates_and_votes, 
key=dict_candidates_and_votes.get)


#Print summary of analysis
khan_percent = (k_votes/total_votes) *100
correy_percent = (c_votes/total_votes) *100
li_percent = (li_votes/total_votes) *100
otooley_percent = (o_votes/total_votes) *100



# Output files
output_file= os.path.join("poll_analysis_summary.txt")

with open(output_file, "w") as file:

#Write methods to print to Analysis

    file.write ("Election Results")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_percent: .3f}% ({k_votes})")
    file.write("\n")
    file.write(f"Correy:{correy_percent: .3f}% ({c_votes})")
    file.write("\n")
    file.write(f"Li: {li_percent: .3f}% ({li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({o_votes})")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"---------------------------")


