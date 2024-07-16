import csv

# Reading the election data
file_path = r"PyRoll/Resources/election_data.csv"
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    data = list(reader)

votes_cast = len(data)
candidates = [row[1] for row in data]

# Counting votes for each candidate
candidate_counts = {}
for candidate in candidates:
    if candidate in candidate_counts:
        candidate_counts[candidate] += 1
    else:
        candidate_counts[candidate] = 1

total_votes = sum(candidate_counts.values())
votes_percentage = {candidate: (count / total_votes) * 100 for candidate, count in candidate_counts.items()}
winner = max(candidate_counts, key=candidate_counts.get)

# Print the results
for candidate, votes in candidate_counts.items():
    percentage = votes_percentage[candidate]
    print(f"{candidate}: {votes} votes ({percentage:.2f}%)")
print(f'Winner: {winner}')

# Writing results to a CSV file
results_path = r"PyRoll/Results/Results.txt"
with open(results_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Metric", "Value"])
    writer.writerow(["Total Votes", total_votes])
    writer.writerow(["", ""])  # Empty row for separation
    writer.writerow(["Candidate", "Votes", "Percentage"])
    for candidate, votes in candidate_counts.items():
        percentage = votes_percentage[candidate]
        writer.writerow([candidate, votes, f"{percentage:.2f}"])
    writer.writerow(["", "", ""])  # Empty row for separation
    writer.writerow(["Winner", winner, ""])
