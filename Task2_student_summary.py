import pandas as pd

def read_and_summary():
    """Reads the CSV using pandas and prints the summary statistics."""

    df = pd.read_csv("student.csv")

    print("\n===== CSV Data Loaded =====\n")
    print(df)

    print("\n===== Summary Statistics (df.describe()) =====\n")
    print(df.describe())

read_and_summary()
