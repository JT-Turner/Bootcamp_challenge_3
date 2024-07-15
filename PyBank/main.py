import csv

# Reading the budget data
file_path = r"Resources/budget_data.csv"
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    data = list(reader)

total_months = len(data)
total_value = sum(int(row[1]) for row in data)
average = total_value / total_months

changelist = []
for i in range(1, total_months):
    monthly_change = int(data[i][1]) - int(data[i - 1][1])
    changelist.append(monthly_change)

maxprof = max(changelist)
minprof = min(changelist)
bp = [data[i][0] for i in range(1, total_months) if int(data[i][1]) - int(data[i - 1][1]) == maxprof]
bl = [data[i][0] for i in range(1, total_months) if int(data[i][1]) - int(data[i - 1][1]) == minprof]

print(f'Total number of months: {total_months}')
print(f'Total value: ${total_value}')
print(f'Average change: ${average}')
print(f'The biggest profit change was in {bp} with the amount of ${maxprof}')
print(f'The biggest loss change was in {bl} with the amount of ${minprof}')

results = [
    ["Total months", total_months],
    ["Total Value", total_value],
    ["Average change", average],
    ["Biggest profit", bp, maxprof],
    ["Biggest loss", bl, minprof]
]

with open(r"Analysis/Pybank_results.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Metric", "Value"])
    for result in results:
        writer.writerow(result)
