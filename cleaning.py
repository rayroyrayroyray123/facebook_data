import pandas as pd
import csv

# ---------------------remove the empty line-------------------
df = pd.read_csv('data1.csv', encoding='utf-16')

# 
df.dropna(how='all', inplace=True)

# 
df.to_csv('remove_empty_line.csv', index=False)

print("CSV has removed the empty line'remove_empty_line.csv'")

#-------------------------combine the lines------------------------------------------
 
file_path = 'remove_empty_line.csv'
df = pd.read_csv(file_path, header=None)

# 
merged_data = []

i = 0
while i < len(df):
    current_line = df.iloc[i, 0]
    combined_line = current_line

    while i + 1 < len(df) and not df.iloc[i + 1, 0][:9].isdigit():
        i += 1
        next_line = df.iloc[i , 0]
        combined_line += ' ' + next_line

    merged_data.append([combined_line])
    i += 1

# 
merged_df = pd.DataFrame(merged_data)

# 
output_file_path = 'combine_multiple_line.csv'
merged_df.to_csv(output_file_path, index=False, header=False)

print("Combine the lines")

#--------------------------replace the comma in the string with bar | ------------------------- 
import pandas as pd
import re

# Load the CSV file without headers and read all data as strings
data = pd.read_csv('combine_multiple_line.csv', header=None, dtype=str)

# Function to replace commas within quotes with bar |
def replace_commas_in_quotes(s):
    if pd.isna(s):
        return s
    # Regular expression to replace commas within quoted strings
    return re.sub(r'(".*?")', lambda m: m.group(0).replace(',', '|'), s)

# Apply the function to the entire DataFrame
processed_data = data.applymap(replace_commas_in_quotes)

# Save the processed DataFrame to a new CSV file
processed_data.to_csv('processed_data_step1.csv', index=False, header=False)

print("Done with the processed data 'processed_data_step1.csv'")










