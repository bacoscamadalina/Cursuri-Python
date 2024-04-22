'''
3.Create a class called Student, based on the data above. Read the JSON file you created, and load all the data into
a list of Student objects. Add a few more Student objects to the list, and then write the new list in a new JSON file.
'''
import json


class Student:
    def __init__(self, id, fname, lname, age, grade):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.age = age
        self.grade = grade


students = []

with open('students.json', 'r') as jsonfile:
    data = json.load(jsonfile)
    for student_data in data:
        student = Student(student_data['id'], student_data['fname'], student_data['lname'], student_data['age'],
                          student_data['grade'])
        students.append(student)

students.append(Student(7, 'Alina', 'Sandu', 31, 10))
students.append(Student(8, 'Sorin', 'Anton', 37, 9.4))

# Pregatim serializarea
student_data = []
for student in students:
    # convertim obiectul intr-un dictionar
    student_dict = {'id': student.id,
                    'fname': student.fname,
                    'lname': student.lname,
                    'age': student.age,
                    'grade': student.grade
                    }
    # adaugam dict in lista de student_data
    student_data.append(student_dict)

with open('students.json','a') as jsonfile:
    json.dump(student_data,jsonfile,indent=4)