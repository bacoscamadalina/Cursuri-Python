"""
1. Create a text file called “hello.txt” and add the following text inside of it:
Python
Java
Javascript
C/C++/C#
PHP
Node.js
Write a short program to read and display the text file
"""
print('Ex.1')
lines = [
    'Python',
    'Java',
    'JavaScript',
    'C/C++/C#',
    'PHP',
    'Node.js'
]

with open('hello.txt', 'w') as file:  # cream fisierul
    for line in lines:
        file.write(line + "\n")

with open('hello.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip elimina spatiile albe

'''
2.Write a short program to append the following lines to “hello.txt” (you will use a list of strings and a for-loop):
Go                                                                                              
Kotlin
Swift
'''
print('EX. 2')
lines = [
    'Go',
    'Kotlin',
    'Swift'
]
with open('hello.txt', 'a') as file:
    for line in lines:
        file.write(line + '\n')

# o alta varianta de a deschide fisiere
f = open('hello.txt', 'r')
text = f.read()  # fisierul este deschis -> pb de securitate
# cum inchidem un fisier?
f.close()
print(text)

'''
3. Write a short program that reads the “hello.txt” file and displays every other line (only odd lines).
'''
print('EX. 3')
with open('hello.txt', 'r') as file:
    lines = file.readlines()  # citim linie cu linie
    for index, line in enumerate(lines, start=1):
        if index % 2 == 1:
            print(line.strip())

'''
4. Write a program that generates 26 text files, called `A.txt`, `B.txt`, … `Z.txt`. Each file will contain the sentences below:
My name is letter X.
I am the 24th letter of the alphabet.
Make sure you use the correct ending for the letter’s number (e.g. 1st, 2nd, 3rd, etc.)
'''