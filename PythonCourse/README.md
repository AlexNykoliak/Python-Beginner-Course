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



# Python Beginner Tasks

A list of beginner-friendly tasks related to the Python programming language. Please follow along and try to complete these tasks.

## Tasks

1. **Hello, World!**: Write a program to print "Hello, World!".

2. **Basic Arithmetic**: Perform and print the result of the following operations: `8+2`, `8-2`, `8*2`, `8/2`, `8**2`, `8//2`, and `8%2`.

3. **String Concatenation**: Create a program that concatenates and prints two strings.

4. **Data Types**: Create variables of each type (`int`, `str`, `float`, `bool`) and print their types using the `type()` function.

5. **Comparisons**: Write a program to compare two numbers using all comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`).

6. **Functions**: Define a function that returns the number `100` and another function that prints the number `100`. Call both functions and observe the output.

7. **Function with Arguments**: Write a function that takes two numbers as input and returns their sum.

8. **String Indexing**: Experiment with Python's string indexing. Create a string and print the character at each index from 0 to the length of the string minus 1.

9. **String Reverse**: Create a string and print it in reverse order using slicing.

10. **Uppercase Conversion**: Take a user's name as input and print it in uppercase.

11. **Lowercase Conversion**: Take a sentence as input and print it in lowercase.

12. **Whitespace Removal**: Create a string with leading and trailing whitespace, and then use the `strip()` method to remove it.

13. **String Replace**: Use the `replace()` method to change all occurrences of a specific letter in a string to another letter.

14. **String Formatting**: Use the `format()` method to create and print a sentence that includes variable values.

15. **List Creation**: Create a list that contains at least one integer, one float, one boolean, and one string. Print the list.

16. **List Indexing**: Use list indexing to print the last item in your list.

17. **Nested List Indexing**: Use list indexing to print the first item in a list that's embedded in your list.

18. **List Slicing**: Create a list of numbers from 1 to 10 and use slicing to print the first half of the list.

19. **List Slicing**: Create a list of numbers from 1 to 10 and use slicing to print the last half of the list.

20. **List Slicing**: Create a list of numbers from 1 to 10 and use slicing to print every other number.

21. **List Concatenation**: Create two lists of numbers and use the `+` operator to concatenate them. Print the result.

22. **Sum Function**: Define a function that takes a list of numbers as input and returns their sum.

23. **String Concatenation Function**: Define a function that takes a list of strings as input and returns a single string that's the result of concatenating all the input strings.

24. **Type Conversion**: Write a program that converts a float to an integer, then to a string, and then back to a float. Print the result at each step.

25. **User Input**: Write a program that uses the `input()` function to take a number as input from the user, doubles the number, and prints the result.

Remember, practice is key when learning a new programming language. Try to understand what each line of code is doing in each task. Don