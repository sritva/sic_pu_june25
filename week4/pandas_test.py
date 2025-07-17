import pandas as pd

def read_csv_file():
    file_path = './spotify-2023.csv'  
    df = pd.read_csv(file_path, encoding='latin1') 

    print("Column counts (non-null values):\n", df.count())
    print("\nFirst 5 rows:\n", df.head())
    print("\nLast 5 rows:\n", df.tail())

def read_csv_file1():
    file_path = './spotify-2023.csv'
    df = pd.read_csv(file_path, encoding='latin1')
    for index, row in df.iterrows():
        print(row[0], "  ", row[1])

def read_csv_file2():
    file_path = './spotify-2023.csv'
    df = pd.read_csv(file_path, encoding='latin1')
    for row in df.iterrows():
        print(row[1][0], row[1][1])

read_csv_file()
