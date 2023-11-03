l=[3,5,6,7,8,9,55,34,24]
l.pop()  # it is used for removing and returning the last element from a list in python
print(l)
print(l[::])
# to print  all the elements of list , u can use the syntax
l=[3,5,6,7,8,9,55,34,24]
print(l[3::5]) #To print every 5th element starting from index 3 in list 'l', you can use the syntax 'print(l[3::5])'.
l=[3,5,6,7,8,9,55,34,24,89,54,23,10]
print(l[0:4:-3]) #l[4:0:-3] starts at index 4, moves backward by 3 steps, and includes the element at index 4.

# swapping element of list
my_list = [1, 2, 3, 4, 5]
i1 = 1
i2 = 3
my_list[i1], my_list[i2] = my_list[i2], my_list[i1]

print(my_list)  # Output: [1, 4, 3, 2, 5]

#find missing value in list
my_list = [1, 2, 3, 5, 6, 7]
n = len(my_list) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(my_list)
missing_value = expected_sum - actual_sum
print("Missing value:", missing_value)  # Output: Missing value: 4
#remove duplicate value
#using set
my_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_list = list(set(my_list))
print(unique_list)  # Output: [1, 2, 3, 4, 5]

#Using a Loop to Remove Duplicates While Preserving Order:

my_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)  # Output: [1, 2, 3, 4, 5]
#Finding Missing Numbers in a List
l=[1,4,6,8,10]
t=l[-1]
for i in range(0,t):
    if(i not in l):
        print(i)


#Finding Index of an Element:
l=[2,6,8,8,7,8,5,10,12]
t=l[-1]
for i in range(0,t):
    if t in l:
        print(i)

#Printing Strings from a List:
l=[3,4,5,6,'avi','ravi',55,66,77]
for i in l:
    if(type(i) ==str):
        print(i)

'''creating
slicing
adding
removing elements from lists'''
l=[] #empty list
print(l)
l1=[1,2,34,5] # list of integers
print(l1)
l2=[2,3.4,5,'avi','vansh'] #list with mixed data types
print(l2)
#nested list
list=['mous',[8,4,6],['a']]
print(list)
#
h=5.6289
t="{:-2}".format(h)
print(t)

#List indexing
list=['p','r','o','h','e']
print(list[0])
print(list[2])
print(list[4])

#nested list
list=["Happy",[2,0,1,5]]
print(list[0][1])  #a
print(list[1][3])  #5
#print(list[4.0]) error
#2. negative indexing
list=['p','r','o','b','e']
print(list[-1]) #e
print(list[-5]) #p

#how to slice lists in python
#list slicing in python
list=['p','y','t','h','o','n','p','r','o']
#elements 3rd to 5th
print(list[2:5])
#elements beg to 4th
print(list[:5])
#elemnts 6th beg to end
print(list[5:])

#elemts beg to end
print(list[:])

#add/change list elemts
add=[1,4,6,8]
add[0]=2
print(add)
add[1:4]=[3,5,7]
print(add)

l=[1,3,5]
l.append(7)
print(l)
l.extend([9,11,13])
print(l)

l=[1,3,5]
print(l+[4,7,5])
print(["re"*3])

add=[1,9]
add.insert(1,3)
print(add)
add[2:2]=[5,7]
print(add)

#delete/remove

list=['p','r','o','b','l','e','m']
del list[2]
print(list)
del list[1:5]
print(list)

del list
print(list) #delete entire list

#<class'list'.
list=['p','r','o','b','l','e','m']
list[2:3]=[] # this will remove o
print(list)

list[2:5]=[] # this remove b,l,e
print(list)

#Python list method
# Define a list of numbers
list = [3, 8, 1, 6, 0, 8, 4]

# Find and print the index of the first occurrence of value 8 in the list
print(list.index(8))

# Count and print the number of occurrences of value 8 in the list
print(list.count(8))

# Sort the list in ascending order
list.sort()

# Print the sorted list
print(list)

# Reverse the order of elements in the list
list.reverse()

# Print the reversed list
print(list)

#list comprehensīon
list=[2** x for x in range(10)]
print(list)

#list membership test - which tell an item exist in a list or no
list=['o','p','l','r']
print('p'not in list)
#iterating through a list
for fruits in ['apple','banana','mango']:
    print("I like",fruits)
#user defined list
x=int(input("Enter the size of the list"))
l=[]

for i in range(0,x):
    y=eval(input("Enter the value: "))
    l.append(y)
print(l)

##########_______
l=[1,2,3,4,5,6,'avi','ashu','ankit',655,'a','b']
l2=['avi','ashu','ankit',66,55,22,33,12,6]
for i in l:
    if(i in l2):
        print(i)




