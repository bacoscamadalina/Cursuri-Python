import pandas as pd
import csv

file_location = "Work.xlsx"
df = pd.read_excel("Work.xlsx", sheet_name="Sheet1")  # df = data frame
print(df)

with open('Workcsv.csv','r') as read_csv:   # se stocheaza in variabila read_csv
    csv_reader = csv.reader(read_csv)
    for row in csv_reader:
        print(row)

    