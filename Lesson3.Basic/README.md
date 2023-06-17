# Input and Arithmetic Operations
a = int(input('Please, enter something: '))
print(a * 2)

# Creating Tuple and Lists
a = 'str1', 'str2', 'str3' # This is a tuple
a = ['Oleksandr', 'Roman', 'Roman', True, False, 2, 10.9] # This is a list

# List Slicing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # It will print ['cherry', 'orange', 'kiwi']

# Replacing Elements in a List
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" # Replaces "banana" with "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"] # Replaces "banana" and "cherry" with "blackcurrant" and "watermelon"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:5] = ["blackcurrant", "watermelon"] # Replaces "banana", "cherry", "orange", and "kiwi" with "blackcurrant" and "watermelon"
print(thislist)

# Sorting Lists
thislist = ["apple", "ampple", "banana", "cherry", "orange", "kiwi", "mango"]
sorted_list = sorted(thislist) # Sorts the list in ascending order
print(sorted_list)

thislist.sort(reverse=True) # Sorts the list in descending order
print(thislist)

# List Methods
a = [1, 2, 3]
a.append(4) # Adds 4 to the end of the list
print(a)

a = [1, 1, 1]
a.append([1, 2, 3, 4]) # Appends a list at the end
print(a)

b = [1, 2, 3]
b.extend([1, 2, 3, 4]) # Extends the list by appending elements from the iterable
print(b)

b = [1, 2, 3]
b.clear() # Removes all items from the list
print(b)

c = b.copy() # Returns a copy of the list
print(c)

d = [1, 2, 3, 3, 3, 3]
print(d.count(3)) # Returns the number of times 3 appears in the list

a = [1, 2, 3]
a.index(3) # Returns the index of the first occurrence of 3
print(a)

t = [1, 2, 3]
t.insert(4, 100) # Inserts 100 at the 4th position
print(t)

a = [1, 2, 3]
element = a.pop(0) # Removes and returns the item at the given position
print(element)

b = [1, 22, 3]
b.remove(22) # Removes the first occurrence of 22 from the list
print(b)

a = [1, 2, 3]

# Python Beginner Tasks

A list of beginner-friendly tasks related to Python lists, list methods, and the input function. Please follow along and try to complete these tasks.

## Tasks

1. **User Input**: Write a program that asks the user to enter a number and then prints that number multiplied by 2.

2. **Tuple Creation**: Create a tuple with three string elements and print it.

3. **List Creation**: Create a list with the names of three people, two boolean values, one integer, and one float. Print the list.

4. **List Slicing**: Create a list of seven fruits. Print the third, fourth, and fifth fruits from the list using slicing.

5. **Replacing Elements**: Create a list of three fruits. Replace the second fruit with "blackcurrant" and print the list.

6. **Replacing Multiple Elements**: Create a list of six fruits. Replace the second and third fruits with "blackcurrant" and "watermelon" respectively. Print the list.

7. **Replacing Multiple Elements II**: Create a list of six fruits. Replace the second through fifth fruits with "blackcurrant" and "watermelon". Print the list.

8. **Sorting Lists**: Create a list of seven fruits. Sort the list in ascending order and print it.

9. **Sorting Lists in Reverse**: Create a list of seven fruits. Sort the list in descending order and print it.

10. **Appending to List**: Create a list of three integers. Use the append method to add the number 4 to the end of the list and print it.

11. **Appending a List to a List**: Create a list with three integers. Append another list containing four integers to the first list. Print the resulting list.

12. **Extending a List**: Create a list with three integers. Use the extend method to add four more integers to the end of the list and print it.

13. **Clearing a List**: Create a list with three integers. Use the clear method to remove all elements from the list and print it.

14. **Copying a List**: Create a list with three integers. Create a copy of the list using the copy method and print the copy.

15. **Counting Occurrences**: Create a list with four integers, where the number 3 appears three times. Use the count method to count how many times 3 appears and print the result.

16. **Finding an Element**: Create a list with three integers. Use the index method to find the position of the number 3 and print it.

17. **Inserting an Element**: Create a list with three integers. Use the insert method to add the number 100 at the fourth position and print the list.

18. **Popping an Element**: Create a list with three integers. Use the pop method to remove and print the first element.

19. **Removing an Element**: Create a list with three integers. Use the remove method to remove the number 2 from the list and print the list.

20. **Reversing a List**: Create a list with three integers. Use the reverse method to reverse the order of the elements in the list and print it.

21. **Sorting a List in Reverse**: Create a list with three integers. Use the sort method with the reverse argument to sort the list in descending order and print it.

22. **Nested List Indexing**: Create a nested list and print an element from one of the inner lists using indexing.

23. **Replacing an Element in a Nested List**: Create a nested list. Replace an element in one of the inner lists and print the whole list.

24. **Creating and Sorting a List**: Create a list of random numbers and sort it in ascending order.

25. **Creating and

 Reversing a List**: Create a list of random numbers and reverse its order.

26. **Creating and Clearing a List**: Create a list of random numbers, then clear it.

27. **Counting Occurrences in a List**: Create a list of random numbers, with one number repeating. Count how many times the repeating number occurs.

28. **Removing a Specific Element from a List**: Create a list of random numbers, then remove a specific number from the list.

29. **Copying and Extending a List**: Create a list of random numbers, copy it to a new list, and then add more numbers to the new list.

30. **Nested List Manipulation**: Create a list with several levels of nested lists, and modify one of the elements deep in the nested structure. Print the original list to verify your changes.

Remember, practice is key when learning a new programming language.