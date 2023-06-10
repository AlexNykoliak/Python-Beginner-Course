# Lesson 2 for Python Students

This lesson covers a wide range of basic and intermediate topics in Python, including but not limited to variable types, operators, functions, strings, and lists. Here's the code for this lesson:

```python
import string
import random

# Basic Printing
print("Hello World")
print(10+10)  # Addition
print(10-10)  # Subtraction
print(10*10)  # Multiplication
print(10**10)  # Exponentiation
print(10/10)  # Division
print(10//10)  # Floor Division
print(10 % 10)  # Modulus
print("Hello World" + str(100))
print("Hello World" + "Hello World")  # Concatenation
print(100, 'Hello World')

# Variable types
a = 100     # Integer
b = "Hello World"  # String
c = 100.1   # Float
d = True    # Boolean
e = False   # Boolean

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# Comparisons
print(10 == 10)  # Equal
print(10 != 10)  # Not Equal
print(10 > 10)  # Greater Than
print(10 < 10)  # Less Than
print(10 >= 10)  # Greater Than or Equal
print(10 <= 10)  # Less Than or Equal

# Basic functions
def function():
    return 100

def function1():
    print(100)

print(function())
print('----------------------')
print(function1())

# String operations
my_string = "HelloWorld"
name = "denys"
name_upper = name.upper()
lastname = "KOVALENKO"
lastname_lower = lastname.lower()
g = " something "
g = g.strip()
f = "something"
f = f.replace("o", "O")
price = '100$'
country = 'Ukraine'
quantity = 10

print("Price of this item is {} and it was made in {}. We have {} items at our shop.".format(
    price, country, quantity))

# List operations
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, True, False, [1, 2, 3, 4, 5,
                                                    6, 7, 8, 9, [1, 2, 3, 4, 5, ['Hi']]], 100.10, 'Hello World']

print(my_list)
print(type(my_list))    # <class 'list'>
print(my_list[-1])   # Hello World

print(my_list[11])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[11][-1])    # 5
print(my_list[11][-1][-1][0])    # Hi
```

Each block represents a different concept in Python, and the comments should help guide you through what each block does.

Remember to practice these examples and modify them to understand how they work. Happy learning!