import pandas as pd
from pathlib import Path
import numpy as np

BASE_DIR = Path(__file__).parent
DATASET_PATH = BASE_DIR / 'data' / 'dirty_cafe_sales.csv'


def load(path : Path = DATASET_PATH) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["Transaction Date"])
    return df

def summerize(df : pd.DataFrame) -> None:
    
    print("first 5 rows")
    print(df.head(5), "\n")
    
    # print("all of the data")
    # print(df.to_string() , "\n")
    
    print("find all datatypes")
    print(df.dtypes, "\n")
    
    print("find rows,cols ")
    row,col = df.shape
    print(f"rows : {row} , cols : {col}")
    
    
    for col in df.columns:
        print(f"column : {col} value counts : ")
        print(df[col].value_counts())

def Standardize_missing_values(df : pd.DataFrame) -> pd.DataFrame:
    df = df.replace(["ERROR", "UNKNOWN"], np.nan)
    
    return df
    
def find_missing(df : pd.DataFrame) -> None:
    print("============== MISSING VALUES PER COLUMN ===================")
    print(df.isna().sum())
    
    
def trim_strings(df : pd.DataFrame) -> pd.DataFrame:
    for col in df.select_dtypes("object").columns:
        df[col] = df[col].str.strip()
    return df
        
    
def remove_duplicates(df : pd.DataFrame) -> None:
    
#     Check for fully duplicated rows.
#     df.duplicated().sum()

    print("Check for fully duplicated rows." , "\n")
    print(df.duplicated().sum())

    print("Check for duplicate Transaction IDs." , "\n")
    print(df["Transaction ID"].duplicated().sum())
    
    #found none dropped nth
    
    
def fixing_dtypes(df : pd.DataFrame) -> pd.DataFrame:
    numeric_cols = ["Quantity", "Price Per Unit", "Total Spent"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df["Transaction Date"] = pd.to_datetime(
    df["Transaction Date"],
    errors="coerce"
)
    return df

    
def fix_missing_values(df : pd.DataFrame) -> pd.DataFrame:
    
    cols = ["Transaction ID", "Item","Transaction Date"]
    df = df.dropna(subset= cols,axis = 0 ).copy()
    
    df["Total Spent"] = df["Total Spent"].fillna(df["Quantity"] * df["Price Per Unit"])
    
    numerical_cols = ["Quantity","Price Per Unit"]
    for col in numerical_cols:
        df[col] = df[col].fillna(df[col].mean())   
    return df


def normalize(df : pd.DataFrame, col : str) -> pd.DataFrame:
    # max scaling: x_new = x_old / x_max  -> values end up in [0, 1]
    df[f"{col} Normalized"] = df[col] / df[col].max()
    return df


def main():
    df = load(DATASET_PATH)
    summerize(df)
    df = Standardize_missing_values(df)
    find_missing(df)
    df = trim_strings(df)
    remove_duplicates(df)
    df = fixing_dtypes(df)
    df = fix_missing_values(df)
    df = normalize(df, "Total Spent")
    print(df[["Total Spent", "Total Spent Normalized"]].head())

if __name__ ==  '__main__':
    main()
    
