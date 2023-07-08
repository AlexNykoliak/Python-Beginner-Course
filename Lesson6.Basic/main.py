a = {1, 2, 3, (1, 2, 3), (1, 2, 3)}


b = ([1, 2, 3], [1, 2, 3, 4], 1, 2, 3)

b[0][-1] = 1

b = list(b)
b[-1] = 100

b = tuple(b)

print(b)


a = 100
print(id(a))

b = 100
print(id(b))

c = b = a

print(id(a) == id(b) == id(c))

a = 100.0
print(id(a) == id(b))


a = -999
b = 1000

if a < b:
    print('var a is less than b')
    if a < 0 and a < -1000:
        print('Also my a is less that 0')
    elif a < 0 and a > -1000:
        print('a i less that 0 and more that -1000')
elif a > b:
    print('var b is less')
else:
    print('Some other cases')


a = [1, 2, 3, 4, 5]

if type(a) == tuple:
    print('type a == tuple')
else:
    print('Type of a is not tuple, it is', type(a))


for i in range(0, 101):
    if i % 2 == 0:
        print('number is even', i)
    else:
        print('number is odd', i)

b = [i for i in range(1, 101) if i % 2 == 0]


a = []
b = [i for i in range(1, 101)]

for i in b:
    if i % 2 == 0:
        a.append(i)

print(a)
print(id(a) == id(b))


a = 'abcdefg'
b = [1, 2, 3, 4, 5]

a = iter(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


for i in a:
    print(i)


for i in range(15):
    if i == 5:
        continue
    elif i == 7:
        pass
    elif i == 8:
        continue
    elif i == 12:
        break
    print(i)


a = []

b = [1, 2, 3, 4, 5]

print(a)


def function(list1, list2):
    for i in list2:
        list1.append(i)


function(a, b)

print(a)


a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")

if a > b:
    print("A")
elif a == b:
    print("=")
else:
    print("B")

if 10 < 20 or type(10) == int:
    print('OK')
