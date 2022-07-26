import sys
import pandas as pd
from pandas import DataFrame
from typing import Set, Any

inFile = sys.argv[1]
# outFile = sys.argv[2]


with open(inFile,'r') as i:
    dataframe = pd.read_csv(i)

df = DataFrame(dataframe)

def remove_columns(df: DataFrame, columns: Set[Any]):
    cols_total: Set[Any] = set(df.columns)
    diff: Set[Any] = cols_total - columns
    df.drop(diff, axis=1, inplace=True)


# Keep columns specified in 2nd argument set
columns_to_keep = {"email", "first name", "last name", "zipcode", "userstate", "usercity", "ethnicity", "email_source", "email_preference", "cellphone", "sms_status", "permission_status", "parental_status", "utm_source", "messenger user id", "advocacy_feed", "advocacy", "parenting_feed", "parenting_engagement", "signed up", "gender", "timezone"}
remove_columns(df, columns_to_keep)

file = "editedfile.csv"

df.to_csv(file, index=False, encoding='utf-8')


"""
Lower case the values of column "email"
df["email"] = df["email"].str.lower()
print(df)
"""
