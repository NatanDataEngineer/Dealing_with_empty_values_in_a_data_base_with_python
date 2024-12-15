# Initial Imports
import pandas as pd
import numpy as np

# Reading CSV file
df = pd.read_csv("files/clientes.csv")

def handling_empty_values(df):
    # Converting values in "TotalGasto" into numeric data
    df["TotalGasto"] = pd.to_numeric(df["TotalGasto"], errors="coerce")
    
    # Checking for missing values in each column
    missing_values = df.isna().sum()
    # print("Missing Values Sum: ", missing_values)

    # Replacing empty values "?" "_" with NaN
    df = df.replace({"?": np.nan, "_": np.nan})

    # Removing empty values
    df = df.dropna(how="any", axis=0)

    # Assigning fixed values to the NaN cells
    mean = df["MesesComoCliente"].mean()
    df["MesesComoCliente"] = df["MesesComoCliente"].fillna(mean)
    
    # Assigning values to the NaN cells with pprevious or following values
    df["MesesComoCliente"] = df["MesesComoCliente"].fillna(method="bfill")

    # Interpolating
    df["MesesComoCliente"] = df["MesesComoCliente"].interpolate()

    # Checking for missing values
    print(f"Missing Value Check: {df.isna().sum()}")

    # Printing Data Frame
    print(df)

handling_empty_values(df)