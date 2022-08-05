import sys
import pandas as pd
from uuid import uuid4
from pandas import DataFrame
from typing import Set, Any

# Get file name from command line
inFile = sys.argv[1]

# Open file
with open(inFile, 'r') as i:
    # Create dataframe
    dataframe = pd.read_csv(i)

df = DataFrame(dataframe)


def remove_columns(df: DataFrame, columns: Set[Any]):
    """
    Remove columns from a DataFrame

    :param df: DataFrame
    :param columns: Set of columns to keep
    :return: DataFrame
    """
    cols_total: Set[Any] = set(df.columns)
    diff: Set[Any] = cols_total - columns
    df.drop(diff, axis=1, inplace=True)


# Specify columns to keep
columns_to_keep = {"email", "first name", "last name", "zipcode", "userstate", "usercity", "ethnicity", "email_source", "email_preference", "cellphone", "sms_status",
                   "permission_status", "parental_status", "utm_source", "messenger user id", "advocacy_feed", "advocacy", "parenting_feed", "parenting_engagement", "signed up", "gender", "timezone"}

remove_columns(df, columns_to_keep)

# Create new file name
new_id = str(uuid4())
newcsv = f'{new_id}.csv'

# Write new file
df.to_csv(newcsv, index=False, encoding='utf-8')


"""
Lower case the values of column "email"
df["email"] = df["email"].str.lower()
print(df)
"""
