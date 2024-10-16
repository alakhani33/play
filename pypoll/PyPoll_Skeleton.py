import csv
import os

input_file = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_votes = {}
winning_candidate = ""
winning_count = 0

with open(input_file) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    
    for row in reader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

with open(output_file, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )

    print(election_results)
    txt_file.write(election_results)

    for candidate, votes in candidate_votes.items():
        vote_percentage = (votes / total_votes) * 100

        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

        candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(candidate_results, end="")
        txt_file.write(candidate_results)

    winning_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )

    print(winning_summary)
    txt_file.write(winning_summary)
