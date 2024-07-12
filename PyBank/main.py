import pandas as pd
import numpy as np

# Reading the budget data
file_path = r"Resources/budget_data.csv"
df = pd.read_csv(file_path)
total_months = df.shape[0]
total_value = df.iloc[:, 1].sum()
average = total_value / total_months

changelist = []
for i in range(1, len(df)):
    monthly_change = df.iloc[i, 1] - df.iloc[i - 1, 1]
    changelist.append(monthly_change)

bp = []
bl = []
maxprof = np.max(changelist)
minprof = np.min(changelist)
for i in range(1, len(df)):
    if (df.iloc[i, 1] - df.iloc[i - 1, 1]) == maxprof:
        bp.append(df.iloc[i, 0])
    elif (df.iloc[i, 1] - df.iloc[i - 1, 1]) == minprof:
        bl.append(df.iloc[i, 0])


print(f'Total number of months: {total_months}')
print(f'Total value: ${total_value}')
print(f'Average change: ${average}')
print(f'The biggest profit change was in {bp} with the amount of ${maxprof}')
print(f'The biggest loss change was in {bl} with the amount of ${minprof}')
results = pd.DataFrame({
    'total months': total_months,
    'Total Value': total_value,
    'Average change' : average,
    'biggest profit' : bp,
    'biggest loss' : bl,  
})
  results.to_csv(r"Analysis/Pybank_results.csv", index=False)

