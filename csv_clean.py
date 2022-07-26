import sys
import pandas as pd
from pandas import DataFrame
from typing import Set, Any

inFile = sys.argv[1]
# outFile = sys.argv[2]


with open(inFile,'r') as i:
    dataframe = pd.read_csv(i)

df = DataFrame(dataframe)

def remove_others(df: DataFrame, columns: Set[Any]):
    cols_total: Set[Any] = set(df.columns)
    diff: Set[Any] = cols_total - columns
    df.drop(diff, axis=1, inplace=True)


# Keep columns specified in 2nd argument set
remove_others(df, {"email", "first_name"})

file = "editedfile.csv"

df.to_csv(file, index=False, encoding='utf-8')






"""
df["email"] = df["email"].str.lower()
print(df)
"""

# Export df to a new .csv file
# file = 'newfile.csv'
# dir = os.getcwd()
# dir1 = os.path.join(dir+file)
# df.to_csv(dir1, index=False, encoding='utf-8')