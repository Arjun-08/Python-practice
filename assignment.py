# -*- coding: utf-8 -*-
"""Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f-gIddNgjCu3Gi40i2uA6-YihKqDohFP
"""

''' The example below shows how different variables are assigned. 
The same variables are printed '''

#!/usr/bin/python

x = 30              # a whole number                   
f = 3.1415926      # a floating point number              
myName = "OOP using Python"    # a string variable - Camel casing
print(x)
print(f)
print(myName)
combination = myName + " " + myName
print(combination)
sum = f + f
print(sum)

# Problem 2     Python strings 
x = "Welcome to OOP Course"
print(x)
print(x[0])       # indexing starts from 0
print(x[1])
s = x[0:3]        # substring 
print(s)
t = x[8:10]     # indexing 
print(t)
s = "My lucky number is %d, what is yours?" % 7          # Combine numbers and text
print(s)
s = "My lucky number is " + str(7) + ", what is yours?"   # alternative method of combining numbers and text
print(s)

# Problem 3 - Use string functions
s = "OOP Course is offered in IIIT DWD"
s = s.replace("OOP","CS")
index = s.find("IIIT DWD")
if "IIIT DWD" in s:
    print("Institute found")
print(s,"\n", index)

# Problem 4 

# define strings                                                         
firstName = "OOP"
lastName = "Course"
words = ["How","are","you","learning ", "OOP " , "Course","?"]

sentence = ' '.join(words)
print(sentence)

# Problem 5 
s = "OOP course is easy to Learn"
words = s.split()        # splits sentence into list of words
print(words, len(s))

x = list(words[0])   # splits word in character
print(x)

# problem 6

import random

# Create a random floating point number and print it.
print(random.random())

# pick a random whole number between 0 and 10.
print(random.randrange(0,15))

# pick a random floating point number between 0 and 10.
print(random.uniform(0,10))

# problem 7

#!/usr/bin/env python3

name = input('What is your name? ')
print('Welcome to OOP Course ' + name)

qualification = input('What is your Qualification? ')
print(name + "'s" + ' 90Educational Qualification  is ' + qualification)

phoneNum = input('Give me pohone number? ')
print('Phone number is : ' + str(phoneNum))

# problem 8    interactive program

#!/usr/bin/env python3

gender = input("Gender? ")
gender = gender.lower()
if gender == "male":
    print(" cat is male")
elif gender == "female":
    print("cat is female")
else:
    print("Invalid input")
age = int(input("Age of your cat? "))

if age < 5:
    print("cat age is", age)
else:
    print("Your cat is adult.")

x = 3
if x == 2:
    print('two')
elif x == 3:
    print('three')
elif x == 4:
    print('four')
else:
    print('something else')

# Problem 9   
#!/usr/bin/env python3
# The first loop will repeat the print function for every item of the list.
# The second loop will do a calculation on every element of the list num and print the result.

city = ['Tokyo','New York','Toronto','Hong Kong']
print('Cities loop:')
for x in city:
    print('City: ' + x)

# problem 10

x = 3                              
while x < 10:
    print(x)
    x = x + 1

# problem 10 - functions without  parameters

def currentYear():
    print('2018')
currentYear()    


def f(x,y):     # with parameters
    return x*y
print(f(3,4))
result = f(3,4)   # return to a variable 
print(result)
print('\n')  # newline


num = [1,2,3,4,5,6,7,8,9]
print('x^2 loop:')
for x in num:
    y = x * x
    print(str(x) + '*' + str(x) + '=' + str(y))

# Python lists
pythonList = [ "New York", "Los Angles", "Boston", "Denver" ]

print(pythonList)     # prints all elements
print(pythonList[0])  # print first element
print(pythonList[-1])