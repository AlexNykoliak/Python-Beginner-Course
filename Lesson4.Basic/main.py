# from time import time
# a = [1, 2, 3]

# a.append(4)
# print(a)

# a.insert(0, 0)
# print(a)

# a.remove(3)

# o = a.pop(0)
# print(o)


# # list, ordered, changeable(mutable), duplicates
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9]

# # tuple   ordered, unchangeable(immutable), duplicates
# my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 11)

# if 11 in my_tuple:
#     print("Yes")
# else:
#     print("No")


# my_text = 'Hello Students'

# if 'students' in my_text.lower():
#     print('There is this word')
# else:
#     print('There is no such word')


# a = 10
# a = float(a)

# students = ('John', 'Bob', 'Alice', 'Mary')
# print(type(students))

# students = list(students)
# print(type(students))
# students.append('Kate')
# print(students)
# students = tuple(students)
# print(type(students))


# start = time()
# my_list = [i for i in range(1000000)]
# end = time()
# print(end - start, 'seconds')  # 0.035776376724243164 seconds


# start = time()
# my_tuple = (i for i in range(1000000))
# end = time()
# print(end - start, 'seconds')  # 0.00002384185791015625 seconds


# f = [1, 2, 3]

# g = (1, 2, 3)
# h = 1, 2, 3

# print(hash(h))
# print(hash(g))  # 529344067295497451

# a, b, c = (1, 2, (3, 4, 5))

# print(a, b, *c)


# a = (1, 2, 3)
# print(type(a))

# a = (1,)
# print(type(a))

# b = ([1, 2, 3],)
# print(type(b))


# a = ([1, 2, 3], [4, 5, 6], [7, 8, 9])

# a[-1].append(10)

# print(a)


# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits
# print(*red)


# fruits = ("apple", "banana", 10, "cherry", "strawberry",
#           1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1, "raspberry")

# for i in fruits:
#     if type(i) == str:
#         print('Єдині елементи цифри це:', i)


# a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ['Roman', 'Ivan', 'Petro'])

# for i in a:
#     try:
#         print(*i)
#     except TypeError:
#         print(i)


# a = ([1, 2, 3, 4], ['Roman', 'Ivan', 'Petro'])


# for i in a:
#     if 'Ivan' in i:
#         print('This person is in the list', 'the index is', i.index('Ivan'))


# tuple1 = ("a", "b", "c")
# tuple2 = (1, 2, 3)


# tuple3 = tuple1 + tuple2
# print(tuple3)

# print(tuple3 * 3)

# a = 'Hello'


# tuple1 = (1, 2, 3, 4, 50, 3, 2, 3, 2)
# print(tuple1.count('a'))
# print(tuple1.index('a'))


# print(len(tuple1))


# a = [('str', 10, 1.0), ('str', 10, 1.0), ('str', 10, 1.0)]


# for i in a:
#     i = list(i)
#     for z in i:
#         if type(z) == float:
#             z = int(z)
#         print(z, end=' ')


# unpacking

a = [1,2]
b = [3,4]
c = [5,6]


fruits =[*c, *b, *c]

print(fruits)




