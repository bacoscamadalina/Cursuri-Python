'''
1. Create a csv file called “students.csv” and add the following text inside of it:
id,fname,lname,age,grade
1,Maria,Popescu,31,7.5
2,Andrei,Ionescu,26,8.0
3,Adriana,Marinescu,21,7.5
4,Matei,Gheorghescu,42,8.5
5,Eusebiu,Pop,33,9.5
6,Ioana,Popa,29,9.0
Read the file using Python’s `csv` standard library, and display it in the terminal as a table, using the options for string formatting from Python:

id	fname		lname		age	grade
---------------------------------------------------
1	Maria		Popescu		31	7.5
2	Andrei		Ionescu		26	8.0
3	Adriana		Marinescu		21	7.5
4	Matei		Gheorghescu	42	8.5
5	Eusebiu		Pop			33	9.5
6	Ioana		Popa			29	9.0

'''
import csv
import pandas as pd

data = [
    ["id", "fname", "lname", "age", "grade"],
    [1, "Maria", "Popescu", 31, 7.5],
    [2, "Andrei", "Ionescu", 26, 8.0],
    [3, "Adriana", "Marinescu", 21, 7.5],
    [4, "Matei", "Gheorghescu", 42, 8.5],
    [5, "Eusebiu", "Pop", 33, 9.5],
    [6, "Ioana", "Popa", 29, 9.0]
]

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)

# var 1 - citiea variantelor brute
with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# var 2 - formatam ca tabel
with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    # formatare header
    header = next(reader)  # next - citeste linei cu linie
    print(f'{header[0]:<6}{header[1]:<12}{header[2]:<12}{header[3]:<6}{header[4]:<6}')
    # header[0]:<6 -coloana "id" va fi aliniata la dreapta cu max 6 caractere
    # semnul < - aliniere la dreapta
    # semnul > - aliniere la stanga
    # semnul ^ - aliniere la centru
    print(60 * '-')
    # iteram prin randuri
    for row in reader:
        print(f'{row[0]:<6}{row[1]:<12}{row[2]:<12}{row[3]:<6}{row[4]:<6}')

# var 3 -folosim pandas
df = pd.read_csv('students.csv')         # data frame - in pandas orice excel este un df
print(df.to_string())