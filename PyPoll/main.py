# naming dependencies
import os
import csv

# files to load
file_to_load = os.path.join("..","Resources","election_data.csv")
file_to_output = "Resources/election_analysis.txt"
print(file_to_load)

# checking pathway
#cwd = os.getcwd()
#print(cwd)

# varibles
total_votes = 0
candidates = []
perc_cand_vote = float
sum_cand_vote = 0
cand_options = {}

# reading files
with open(file_to_load) as election_data :
    reader = csv.DictReader(election_data)

# looping through data
    for row in reader:
        #print(f"{row}")

# calculating the totals
        total_votes = total_votes+ 1
        candidates = row["Candidate"]

# adding candiates to the list Candidates
        if row["Candidate"] not in candidates:

            candidates.append(row["Candidate"])

            candidate_options[row["Candidate"]] = 1

        else:
            candidate_options[row["Candidate"]] = candidate_options[row["Candidate"]] + 1


    # Determine the Winner:
        if (sum_cand_vote  > sum_cand_vote [2]):
            highest_vote[1] = Row(int(sum_cand_vote))
            highest_vote[0] = row["Candidate"]


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

sum_cand_vote

winner = sorted(candidate_votes.items(), key=get_item(1), reverse=True)

#results
print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")


# Print
with open(file_to_output, "w") as txt_file:

    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write(candidate + " " + str(round(((sum_cand_vote[candidates]/total_votes)*100))) + "%" + " (" + str(sum_cand_vote[candidates]) + ")")
    txt_file.write(str(winner))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[0]))
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(total_votes))
