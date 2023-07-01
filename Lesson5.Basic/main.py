# import time
# from tracemalloc import start

# a = (1,2,3,4,5)


# b = [1,2,'text', True]

# start = time.time()
# for i in b:
#     print(type(i))

# end = time.time()
# print(end - start) # 0.00006246566772460938


# start = time.time()
# for i in a:
#     print(type(i))

# end = time.time()
# print(end - start) #0.00005245208740234375


# a = 10


# def func(argument):
#     argument += 1
#     print(argument)

# func(a)


# students = {

#     'number_of_students': 2,

#     'pupils': {
#         'John': {
#             'name': 'John',
#             'age': 20,
#                     'marks': [10, 9, 8, 7, 6]
#         },
#     }

# }


# print(students['pupils']['John']['age'])


# a = {
#     'name': 'John',
#     'age': 20,
#     'marks': [10, 9, 8, 7, 6]
# }

# a['surname'] = 'Nykolyak'
# print(a)

# print(a['name'])
# print(a.get('name'))


# print(a.keys())
# print(a.values())


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "colors": ["red", "white", "blue", ["black", "yellow"]]
# }

# print(thisdict["colors"][-1][-1])


# year = thisdict["year"]
# print(year)


# a = dict(name="Oleksandr", age=28)

# print(a)

# a = (1,2,3,4,5)

# my_dict = {
#     (1,2,3,4,5) : ['Bob', 'Alice', 'Mary'], # key hash -5659871693760987716
# }


# a = [i for i in range(1, 101)]

# for i in range(1, 101):
#     a.append(i)


# print(a)

from string import ascii_lowercase as alphabet


my_dict = {i: z for i, z in zip(range(1, 100), alphabet[::-1])}


print(my_dict)


# a = [1, 2, 3]
# b = ['a', 'b', 'c']
# d = [True, False, True]

# c = zip(a,b, d)
# print(list(c))

