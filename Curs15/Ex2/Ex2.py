'''
2.Read again the information from the csv file above, store it all in a list of data, and then write a new file,
called “students.json”, which will contain a valid JSON object. Use the following format for each student
(and use Python’s standard JSON module):
[
	{
		"id": 1,
		"fname": "Maria",
		"lname": "Popescu",
		"age": 31,
		"grade": 7.5
	},
	...
]

'''
import csv
import json

students = []
with open('students.csv','r') as csvfile: # in csvfile se va
    reader = csv.DictReader(csvfile)
    for row in reader:
        student = {
            'id' : int(row['id']),
            'fname' : row['fname'],
            'lname' : row['lname'],
            'age' : int(row['age']),
            'grade': float(row['grade'])
        }    # preia si transforma cheia in int
        students.append(student)

with open('students.json','w') as jsonfile:
    json.dump(students,jsonfile,indent=4)

with open('students.json','r') as jsonfile:
    for student in students:
        print(student)
