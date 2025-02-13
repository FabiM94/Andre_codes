import pandas as pd

## Load the data from the Excel file
df = pd.read_excel('Schedule_DM34.xlsx', header=None, skiprows=1)  # header=None if there's no header row

#Takes the last column values (Date)
last_column = df.iloc[:, -1]
last_column_transposed = pd.DataFrame(last_column).T

# Omit the last column
df = df.iloc[:, :-1]

## Transpose the DataFrame to work with columns as rows
df_transposed = df.T

## Group every 4 rows (original columns) and calculate the mean
df_grouped = df_transposed.groupby(df_transposed.index // 4).mean()

# Transpose back to original orientation (columns as columns)
#df_grouped = df_grouped.T
df_grouped_full_power=pd.concat([last_column_transposed,df_grouped])
# Reset index if desired
df_grouped_full_power.reset_index(drop=True, inplace=True)

# Save the result to a new Excel file
df_grouped_full_power.to_excel('output_hourly_Power_DM34.xlsx', index=False, header=False)


######Para el archivo de aFRR up #######

## Load the data from the Excel file
df = pd.read_excel('aFRRup_DM34.xlsx', header=None, skiprows=1)  # header=None if there's no header row

#Takes the last column values (Date)
last_column = df.iloc[:, -1]
last_column_transposed = pd.DataFrame(last_column).T

# Omit the last column
df = df.iloc[:, :-1]

## Transpose the DataFrame to work with columns as rows
df_transposed = df.T

## Group every 4 rows (original columns) and calculate the mean
df_grouped = df_transposed.groupby(df_transposed.index // 4).mean()

# Transpose back to original orientation (columns as columns)
#df_grouped = df_grouped.T
df_grouped_full_up=pd.concat([last_column_transposed,df_grouped])
# Reset index if desired
df_grouped_full_up.reset_index(drop=True, inplace=True)

# Save the result to a new Excel file
df_grouped_full_up.to_excel('output_hourly_aFRRup_DM34.xlsx', index=False, header=False)


######Para el archivo de aFRR down #######

## Load the data from the Excel file
df = pd.read_excel('aFRRdown_DM34.xlsx', header=None, skiprows=1)  # header=None if there's no header row

#Takes the last column values (Date)
last_column = df.iloc[:, -1]
last_column_transposed = pd.DataFrame(last_column).T

# Omit the last column
df = df.iloc[:, :-1]

## Transpose the DataFrame to work with columns as rows
df_transposed = df.T

## Group every 4 rows (original columns) and calculate the mean
df_grouped = df_transposed.groupby(df_transposed.index // 4).mean()

# Transpose back to original orientation (columns as columns)
#df_grouped = df_grouped.T
df_grouped_full_down=pd.concat([last_column_transposed,df_grouped])
# Reset index if desired
df_grouped_full_down.reset_index(drop=True, inplace=True)

# Save the result to a new Excel file
df_grouped_full_down.to_excel('output_hourly_aFRRdown_DM34.xlsx', index=False, header=False)
