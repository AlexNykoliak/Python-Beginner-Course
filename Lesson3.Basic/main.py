a = int(input('Введіть будь ласка щось: '))     # 100
print(a * 2)    # 200


a = 'srt', 'srt2', 'srt3'   # tuple
a = ['Oleksandr', 'Roman', 'Roman', True, False, 2, 10.9]   # list
a1 = 'Oleksandr'
a2 = 'Roman'
a3 = 'Roman'


thislist = ["apple", "banana", "cherry",
            "orange", "kiwi", "melon", "mango"]    # list
print(thislist[2:5])


thislist = ["apple", "banana", "cherry"]    # list
thislist[1] = "blackcurrant"
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]   # list
thislist[1:3] = ["blackcurrant", "watermelon"]
# ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
print(thislist)


thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]    # list
thislist1[1:5] = ["blackcurrant", "watermelon"]
print(thislist1)


thislist2 = ["apple", "ampple", "banana",
             "cherry", "orange", "kiwi", "mango"]  # list
sorted_list2 = sorted(thislist2)
print(sorted_list2)


thislist2 = ["apple", "ampple", "banana",
             "cherry", "orange", "kiwi", "mango"]  # list
thislist2.sort(reverse=True)
print(thislist2)


thislist3 = [4, 3, 2, 3, 4]
sorted_list3 = sorted(thislist3)
print(sorted_list3)

thislist3: list[int] = [4, 3, 2, 3, 4]
thislist3.sort(reverse=True)
print(thislist3)


a = [1, 2, 3]
a.append(4)
print(a)

a = [1, 1, 1]
a.append([1, 2, 3, 4,])
print(a)


b = [1, 2, 3]
b.extend([1, 2, 3, 4,])
print(b)

b = [1, 2, 3]
b.clear()
print(b)

c = b.copy()
print(c)

d = [1, 2, 3, 3, 3, 3]
print(d.count(3))

c = [1, 2, 3]
c.extend([4, 5, 6])
print(c)

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
c.extend(a)
c.extend(b)
print(c)


a = [1, 2, 3]
print(a.index(3))

t = [1, 2, 3]
t.insert(4, 100)
print(t)


a = [1, 2, 3]
element = a.pop(0)
print(element)

b = [1, 22, 3]
b.remove(22)
print(b)


a = [1, 2, 3]
a.reverse()
print(a)

a = [1, 2, 3]
a.sort(reverse=True)
element = sorted(a)
print(a)
print(element)


a = [1, 2, 3, 4, 5, [11, 22, 33], [
    44, [55, 55, 4444, [1000]], 55, 66, [77, 888, 99]]]   # list

print(a)
a[6][1][3][0] = 1

print(a)
