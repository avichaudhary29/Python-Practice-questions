#Loop - a sequence of elements using diff. variations of for loop.
#for loop - is used to iterate over a sequence(list,tuple,string)or other iterable objects.

numbers = [6,3,5,8,4,2,11]
sum = 0
for val in numbers:
    sum = sum+val
    print("Sum",sum)

# Using a for loop to iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using a for loop with range to iterate a specific number of times
for i in range(5):
    print(i)

#While Loop:
# A while loop is used to repeatedly execute a block of code as long as a certain condition is true.

# Using a while loop to count from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1
# Using a while loop to find the first power of 2 greater than 100
num = 1
power = 0
while num <= 100:
    num = 2 ** power
    power += 1
print(num)

#range()function- we can generate a sequence of number using this.

range(10)
print(list(range(2,8)))

print(list(range(2,8,3)))

# we can use the range() funcn in for loops to iterate through a sequence of numbers. It can be combined with len()funcn to iterate through a sequence using indexing.
genre = ['pop','rock','jazz']
for i in range (len(genre)):
    print("I Like" , genre[i])

# for loop with else

digits = [0,1,5]
for i in digits:
    if(i==5):
        print(i)
        break
else:
    print("item math")
#Break
for val in "String" :
    if val =="i":
        break
    print(val)
print("The end")
#contine
for val in "string":
    if val =="i":
        continue
    print(val)
print("The end")

#max. value in dictinary with key by using min () and max()
dict = {"avi" :29,"Ashu":27,"Ankit":12}
high = max(dict,key=dict.get)
print(high)

#pass -
for i in range(0,20):
    pass
print("hi")

