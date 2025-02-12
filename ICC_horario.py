import pandas as pd

## Load the data from the Excel file
#df = pd.read_excel('Data/ICC_List.xlsx', header=None)  # header=None if there's no header row
## Load the data from the Excel file
df = pd.read_excel('Data/Heat_Demand.xlsx', header=None)  # header=None if there's no header row


#Takes the last column values (Date)
last_column = df.iloc[:, -1]
last_column_transposed = pd.DataFrame(last_column).T
data=df.iloc[:,:-1].T

# Omit the last column
df = df.iloc[:-1, :-1]

## Transpose the DataFrame to work with columns as rows
df_transposed = df.T


df_varnames=df.iloc[1,:].T
## Group every 4 rows (original columns) and calculate the mean
#df_grouped = df_transposed.groupby(df_transposed.index // 4).mean()

# Transpose back to original orientation (columns as columns)
#df_grouped = df_grouped.T
df_grouped_full_power=pd.concat([last_column_transposed,data])
# Reset index if desired
df_grouped_full_power.reset_index(drop=True, inplace=True)

# Save the result to a new Excel file
df_grouped_full_power.to_excel('output_ICC.xlsx', index=False, header=False)


