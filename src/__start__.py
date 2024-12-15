# Initial Imports
import pandas as pd
import numpy as np

# Reading and Displaying CSV file
data_frame = pd.read_csv("files/clientes.csv")
print(data_frame)

# Converting values in "TotalGasto" into numeric data
data_frame["TotalGasto"] = pd.to_numeric(data_frame["TotalGasto"], errors="coerce")
    
print(data_frame.info())
 