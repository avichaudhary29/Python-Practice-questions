l = [44, 12, 34, [], [], 33, 66, [], 6]
count = 0  # Initialize a variable to count the empty lists

# Iterate through each element in the list
for i in l:
    # Check if the current element is of type list (i.e., an empty list)
    if type(i) == list:
        count = count + 1  # Increment the count if the element is an empty list

# Print the final count of empty lists
print(count)

###########
s={3,4,5,6,7,1,2,3,3,3,3,4,'gaurav','ravi','sachin','gaurav','gaurav',55}
print(s)
s.add('kumar')
print(s)
s.clear()
print(s)
#####################operations######################
s={3,5,6,7,8}
s2={6,9,12,56,78}
print(s.union(s2))
print(s|s2) #for union we can use this method
print(s.issubset(s2)) #this method tells s is a subset of s2 or not
print(s.issuperset(s2)) #this method tells s is a superset of s2 or not
print(s.difference(s2))
#print(s+s2) this show error because sets is a object type elements , set have unindxed data
s.update(s2) # for this operation s is change
print(s)
print(s.union(s2))
print(s.intersection(s2))
print(s & s2)# for intersetion we can use this method also
print(s.difference(s2))
print(s-s2)  # another method for difference
print(s.symmetric_difference(s2))
print(s^s2)  # another method for symmentric dffernece
####for deletion and remove
s={3,5,16,17,18,78}
s.remove(17)
s.discard(3)
print(s)
s.pop() #this remove smallest value
print(s)

s={6,5,16,17,18,1,3,78}
s2={5,6,7,8,12,34,56}
print(s.isdisjoint(s2))
#user defined set
x=int(input("Enter size of sets"))
d=set()
for i in range(0,x):
    t=eval(input("Enter values"))
    d.add(t)
print(d)

#for imutable set
s={4,5,6,7}
t=frozenset(s)
print(s)
s={4,5,6,7,10}
s2={5,6,7,8,12}
s.difference_update(s2)
print(s)

#declare frozen set
fs=frozenset([1,2,3,4])
print(fs)