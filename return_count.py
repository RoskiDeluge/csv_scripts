import pandas as pd

# Read in the CSV file
df = pd.read_csv('/content/subscribed_ad5b97b235.csv')

# Define the date range
# Add these dates via argparse from cli, keep the 24:00:00 as it is
start_date = '2023-02-19 24:00:00'
end_date = '2023-02-27 24:00:00'

# Filter the data based on the date range and count the rows
# Add column name, or hard code OPTIN_TIME (o) and UNSUB_TIME (u) via argparse
filtered_df = df.loc[(df['OPTIN_TIME'] > start_date) & (df['OPTIN_TIME'] < end_date)]
count = filtered_df.shape[0]

# Print the result
print(f"The count of items between {start_date} and {end_date} is: {count}")