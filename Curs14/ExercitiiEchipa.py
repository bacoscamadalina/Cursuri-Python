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


def readfile(filename):
    with open(filename, 'r') as f:
        return f.readlines()


print(readfile('hello.txt'))

'''
Write a short program to append the following lines to “hello.txt” (you will use a list of strings and a for-loop):
Go                                                                                              
Kotlin
Swift
'''


def append(filename):
    lista = ['Aba\n', 'Kotlin\n,Swift\n']
    for i in lista:
        with open(filename, 'a') as f:
            f.writelines(i)


append('hello.txt')

'''
3. Write a short program that reads the “hello.txt” file and displays every other line (only odd lines).
'''


def read_odd_lines(filename):
    result = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for index, line in enumerate(lines, start=1):
            if index % 2 == 1:
                result.append(line.strip())
    return result


odd_lines = read_odd_lines('hello.txt')
print(odd_lines)

'''
4. Write a program that generates 26 text files, called `A.txt`, `B.txt`, … `Z.txt`. Each file will contain the sentences below:
My name is letter X.
I am the 24th letter of the alphabet.
Make sure you use the correct ending for the letter’s number (e.g. 1st, 2nd, 3rd, etc.)
'''

