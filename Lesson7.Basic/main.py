import time
import itertools
a = [1, 2, 3, 4, 5]
print(a[0])
a.append(6)

b = {1, 2, 3, 4}
c = {5, 4, 3, 2}

c = b.union(c)

my_dict = {key: values for key, values in zip(a, b)}


print(my_dict)


i = 0

while i < 100:
    print(i)
    i = i + 2


while 100:
    print("Hello")
    break


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(id(a) == id([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


class Iterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        return result


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = iter(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


for element in a:
    print(element)

i = 0
while i < 10:
    if i == 5:
        continue
    print(i)
    i += 1


for i in range(10):
    if i == 5:
        continue
    print(i)


i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


fruits = ["apple", "banana", "cherry"]

for x in fruits:
    for i in x:
        i = i.upper()
        print(i, end="")


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in my_list:
    if i % 2 == 0:
        i = i ** 2
    print(i)


list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

a = 10
a = a + 1
a += 1


a[-1] = 10
a[-1] += 1


a = [1, 2, 3]

a = list(reversed(a))
b = tuple(reversed(a))
c = set(reversed(a))

print(a)
print(b)
print(c)


for letter in "banana":
    print(letter)


for i in range(10):
    print(i)

for i in range(10, 0, -1):
    print(i)

for _ in range(10):
    print("Hello")


for x in range(6):
    print(x)
else:
    print("Finally finished!")


for x in range(12, 0, -1):
    if x == 2:
        break
    print(x)
else:
    print("Finally finished!")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

start = time.time()
for x in adj:
    for y in fruits:
        print(x, y)
finish = time.time()

# time in seconds
print(finish - start)  # 0.00007772445678710938


start = time.time()
adj_fruits = list(itertools.product(adj, fruits))
print(adj_fruits)
finish = time.time()
print(finish - start)  # 0.000017404556274414062
