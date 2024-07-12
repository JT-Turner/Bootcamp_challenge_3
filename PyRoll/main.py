file = r"Resources\election_data.csv"
df2 = pd.read_csv(file)
votes_cast = df2.shape[0]
candidates = df2.iloc[:, 1]
candidate_counts = candidates.value_counts()

total_votes = candidate_counts.sum()
votes_percentage = (candidate_counts / total_votes) * 100
winner = candidate_counts.idxmax()
results = pd.DataFrame({
    'Votes': candidate_counts,
    'Percentage': votes_percentage
})
for candidate, row in results.iterrows():
    print(f"{candidate}: {row['Votes']} votes ({row['Percentage']:.2f}%)")
print(f'Winner: {winner}')
results.to_csv(r"Analysis\pyroll_results.csv", index=False)
