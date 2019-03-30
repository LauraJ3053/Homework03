import os
import csv

file_to_load = os.path.join("Resources","election_data.csv")
file_to_output = "Resources/election_analysis.txt"
print(file_to_load)

cwd = os.getcwd()
print(cwd)

#Varibles to Track
total_votes = 0
candidates = []
perc_cand_vote = float
sum_cand_vote = 0
cand_options = {}

with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)



    for row in reader:
        print(f"{row}")
        total_votes = total_votes+ 1
        candidates = row["Candidates"]

        if row["Candidates"] not in candidate:

            candidate.append(row["Candidates"])

            candidate_options[row["Candidates"]] = 1

        else:
            candidate_options[row["Candidates"]] = candidate_options[row["Candidates"]] + 1

#----------------------------------------------------------------------------------------
    # Determine the Winner:
    #if (votes > winner_votes[2]):
     #   greatest_increase[1] = revenue_change
      #  greatest_increase[0] = row["Candidate"]
#----------------------------------------------------------------------------------------

    print()
    print()
    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(total_votes))
    print("-------------------------")
#results
    for candidates in candidate_options:
        print(candidate + " " + str(round(((candidate_options[candidates]/total_votes)*100))) + "%" + " (" + str(candidate_options[candidates]) + ")")
        candidate_results = (candidates + " " + str(round(((candidate_options[candidates]/total_votes)*100))) + "%" + " (" + str(candidate_options[candidates]) + ")")

candidate_votes

winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

#results
print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")





# Output Files
with open(file_to_output, "w") as txt_file:

    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    #txt_file.write(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
    txt_file.write(str(winner))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[0]))
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(votes))
