'''classes of collection
1.list
2.dictionary
3.set
4.tuples


---LIST---
collection of object type element
it is a dynamic
denoted by []
mutable (KISI mai change kiya jaye means dynamic object)follow ordering sequence'''
l=[2,4,5,'avi','ashu','ankit',2.3,45.9,4.3]
l.insert(3,'chaudhary')  # insertion
print(l)
#when we want to insert at the end of the list we use append
l.append('chaudhary')
print(l)
l2=['bhumi','prachi','somiya']
l.extend(l2)  #if we want to add or update a whole list we use extend or we also create new variablet=l+l2
print(l)

l1=[ ]
l1=l.copy()  #copy the content of above list
print(l1)
#remove
l2 = [2, 4, 5, 'avi', 'ashu', 'ankit', 2.3, 45.9, 4.3]
l2.remove('ankit')
print(l2)
print(l.index('avi'))  #index
#count for repetive values

l=[3,4,5,6,'siya','riya','ashish','siya','riya']
print(l.count('siya'))
l=['gaurav','ravi','govind','sachin','parul','sahil']
l.sort() #ascending
print(l)

l.sort()
l.reverse() #ascending order
print(l)
l.clear()
print(l)
