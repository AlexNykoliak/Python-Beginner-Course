import string
import random

print("Hello World")
print(10+10)  # Addition
print(10-10)    # Subtraction
print(10*10)    # Multiplication
print(10**10)   # Exponentiation
print(10/10)    # Division
print(10//10)   # Floor Division
print(10 % 10)    # Modulus
print("Hello World" + str(100))
print("Hello World" + "Hello World")    # Concatenation
print(100, 'Hello World')

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

print(10 == 10)  # Equal
print(10 != 10)  # Not Equal
print(10 > 10)  # Greater Than
print(10 < 10)  # Less Than
print(10 >= 10)  # Greater Than or Equal
print(10 <= 10)  # Less Than or Equal


""" This is a function which prints Hello World """

a = 1
b = ' '

print(id(a))
print(id(' '))
print(id(b))


numbers = string.digits
punctuation = string.punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
lower_case = string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
upper_case = string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
all_letters = string.ascii_letters

print(numbers)
print(punctuation)
print(lower_case)
print(upper_case)
print(all_letters)


symbols_for_password = numbers + punctuation + lower_case + upper_case

password = "".join(random.sample(symbols_for_password, 12))

print(password)


int()  # Integer
float()  # Float
str()  # String
bool()  # Boolean

a = 10
a = int(float(str(float(a))))

a = 100    # Integer
print(type(a))  # <class 'int'>
print(a)    # 100

a = float(a)    # 100.0
a = str(a)  # '100.0'
print(type(a))  # <class 'str'>
print(a)   # '100.0'
print(int(a) + 100)  # 200


a, b, c = 100, 200, 300


print(a)    # 100
print(b)    # 200
print(c)    # 300


*z, x, y = 100, 200, 300, 400, 500, 600

print(z)
print(x)
print(y)


a = b = c = f = 100

b = 200

print(a)
print(b)


def function():
    return 100


def function1():
    print(100)


print(function())
print('----------------------')
print(function1())


my_string = "HelloWorld"
print(my_string[0])     # H
print(my_string[1])     # e
print(my_string[-1])    # d
print(my_string[2:6])   # lloW
print(my_string[2:])    # lloWorld
print(my_string[:6])    # HelloW
print(my_string[:])     # HelloWorld
print(my_string[::2])   # Hlool
print(my_string[::-1])  # dlroWolleH


name = "denys"
name_upper = name.upper()
print(name_upper)  # DENYS

lastname = "KOVALENKO"
lastname_lower = lastname.lower()
print(lastname_lower)  # kovalenko


g = " something "
print(g)
g = g.strip()
print(g)   # something


f = "something"
f = f.replace("o", "O")
print(f)    # sOmething


price = '100$'
country = 'Ukraine'
quantity = 10


print("Price of this item is {} and it was made in {}. We have {} items at our shop.".format(
    price, country, quantity))


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, True, False, [1, 2, 3, 4, 5,
                                                    6, 7, 8, 9, [1, 2, 3, 4, 5, ['Hi']]], 100.10, 'Hello World']

# [1, 2, 3, 4, 5, 6, 7, 8, 9, True, False, [1, 2, 3, 4, 5, 6, 7, 8, 9], 100.1, 'Hello World']
print(my_list)
print(type(my_list))    # <class 'list'>
print(my_list[-1])   # Hello World

print(my_list[11])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[11][-1])    # 5
print(my_list[11][-1][-1][0])    # Hi
