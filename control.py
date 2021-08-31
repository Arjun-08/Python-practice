# -*- coding: utf-8 -*-
"""control.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19DdvYTb2g2_fi8hS6x2ZFxTAhpZUIMDl
"""

# If the number is positive, we print an appropriate message

# Python if... Statement - 1 option
num = 30
if num > 0:
    print(num, "is a positive number.")
print("printed number status.")

# Python if...else Statement  - 2 option
if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")

# Python if...elif...else Statement - 3 Option
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

num = float(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [60, 25, 33, 85, 40, 22, 55, 43, 51]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
    sum = sum+val

print("The sum is", sum)

# Program to iterate through a list using indexing

music = ['pop', 'rock', 'jazz','classic']

# iterate over the list using index

for i in range(len(music)):
    print("I like", music[i])

#combined with the len() function to iterate through a sequence using indexing.

# program to display student's marks from record
student_name = 'Soyuj'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')


# Use of break statement inside the loop

for val in "string":
    if val == "i":
        break
    print(val)

print("The end")


# Program to show the use of continue statement inside loops

for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")

# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)


# While loop with else

'''Example to illustrate
the use of else statement
with the while loop'''

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")
