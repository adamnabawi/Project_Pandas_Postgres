import pandas as pd 

# Import File CSV   
df = pd.read_csv('Costumer_Master.csv', sep='|')

# Normalize Data
df['Count']=1
df.rename(columns=lambda x: x.strip(), inplace= True)
cols = df.select_dtypes(object).columns
df[cols] = df[cols].apply(lambda x: x.str.strip())

# Create Pivoted Table
pivoted = df[df['Service_Policy'] == 'Gold'].pivot_table(
    index="GM_Code", columns="Service_Policy", values="Count", aggfunc='count', fill_value=0)

# Sorted Pivot
sorted_pivoted = pivoted.sort_values(by=['Gold'], ascending=False)

# Print
print(sorted_pivoted)