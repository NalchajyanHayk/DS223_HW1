import pandas as pd
import numpy as np

# Define the function for data processing
def load_smart_home_spending(file_path: str) -> pd.DataFrame:
    # Load the Excel file
    xls = pd.ExcelFile(file_path)
    
    # Load the 'Data' sheet into a DataFrame, skipping metadata rows
    df = pd.read_excel(xls, sheet_name='Data', skiprows=4, header=None)
    
    # Drop the first column if it contains only NaN values
    df = df.iloc[:, 1:]
    
    # Rename columns explicitly
    df.columns = ["Year", "Customer Spending"]
    
    # Drop any empty or irrelevant rows
    df = df.dropna().reset_index(drop=True)
    
    # Clean the "Year" column to remove any non-numeric characters
    df["Year"] = df["Year"].astype(str).str.extract(r'(\d+)').astype(int)
    
    # Convert "Customer Spending" to float
    df["Customer Spending"] = df["Customer Spending"].astype(float)
    
    # Limit to first 6 rows (as in original script)
    return df.head(6)

# Define the Bass Diffusion Model function
def bass_model(t, p, q, M):
    # Calculate the adoption based on the inputs
    adoption = M * (((p + q) ** 2 / p) * np.exp(-(p + q) * t)) / ((1 + (q / p) * np.exp(-(p + q) * t)) ** 2)
    return adoption
