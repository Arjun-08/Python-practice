# -*- coding: utf-8 -*-
"""python variables.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15O2wQ2V_ZTvkR9p39As5XxJGjxABE9FY
"""

a = 100  
b = a  
print(id(a)) 
print(id(b)) 
print(a)
print(a)
# Reassigned variable a  
a = 800  
print(id(a))
print(a)

name = "OOPCourse"  
Myage=Herage= 45       # Assigning single value to multiple variables
a=b=c=90  
a=b=c=4,5,6               
a,b,c=4,5,6            # Assigning multiple values to multiple variables:

print(name)  
print(Myage,Herage)  
print(a,b,c) 

name = "Test1"  
Name = "Test2"  
naMe = "Test3"  
NAME = "Test4"  
n_a_m_e = "Test5"  
_name = "Test6"  
name_ = "Test7"  
_name_ = "Test8"  
na80me = "Test9"  
print(name,Name,naMe,NAME)            # Print multiple values  
print(name,Name,naMe,NAME,n_a_m_e, NAME, n_a_m_e, _name, name_,_name, na80me)

# Declaring a function  
def Myadd():  
    # Defining local variables. They has scope only within a function  
    m = 40  
    n = 40  
    p = m + n 
    print("The sum is:", p)  
  
# Calling a function  
Myadd()  

# Accessing local variable outside the function. Gives an error   
print('m')

# Declare a variable and initialize it  
x = 200  
  
# Global variable in function  
def mFunction():  
    # printing a global variable  
    global x  
    print(x)  
    # modifying a global variable  
    x = 'Welcome To OOP'  
    print(x)  
  
mFunction()  
print(x)  

del x  
print('x')

c = 50000000000000000000000000000000000000000000  
c = c + 1  
print(type(c))  
print (c)