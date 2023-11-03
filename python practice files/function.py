'''parameterized function
parameterless functn
default parameter func
positional argument functn
anonymous func
return type func - single value return type functn and multiple
recursion functn
.*functn
** kword funct
enumerator functn'''
#parameterized function
def add(x,y):
    z=x+y
    print(z)
x=int(input())
y=int(input())
add(x,y)
#parameterless default function
def add():
    x = 10
    y = 20
    z = x + y
    print(z)

add()  # Calling the function
##########---------
def show(id, name, lastname, salary):
    print("ID:", id)
    print("Name:", name)
    print("Last Name:", lastname)
    print("Salary:", salary)

# Call the function with specific values
show(123, 'Ravi', 'Sharma', 400)

# Redefine the function with default parameter
def show(id, name, lastname, salary=300000):
    print("ID:", id)
    print("Name:", name)
    print("Last Name:", lastname)
    print("Salary:", salary)

# Call the function without providing the salary (default value will be used)
show(123, 'Ravi', 'Sharma')
###########Postional argument funtn
def show(id,name,lastname,salary):
    print("id",id)
    print("name",name)
    print("Lastname",lastname)
    print("Salary",salary)
show(name='gaurav',salary=5000,id=123,lastname='tomar')

#####Anonymous function
# Regular function
def add(x, y):
    return x + y

result = add(3, 5)
print(result)  # Output: 8

# Anonymous function (lambda)
sum = lambda x, y: x + y

result = sum(3, 5)
print(result)  # Output: 8
#####--
l=[1,2,3,4]
l2=[4,5,6,7]
t=list(map(lambda x,y:x+y,l,l2))

#reduce
h="HKTIJUP"
t=sorted(h)
print(t)
from functools import reduce
list1=[1,2,3,4]
sum=reduce(lambda x,y: x+y,list1)
print(sum)

#
import functools

h = "HKTIJUP"
t = sorted(h)
n = functools.reduce(lambda x,y: x+y,t)
print(t)
# return type func
l=[1,4,57,4]
k=l.sort()
print(k)
t=l.count(4)
print(t)
def show(x,y):
    z=x+y
    return z
t=show(4,5)
print(t)

#recursion function
def facto(x):
    if(x==1):
        return 1
    else:
        return x-facto(x-1)
k=facto(5)
print(k)
#*arg fuctn

def add(*args):
    print(args)
    print(type(args))
l=[4,5,67,8]
add(*l)
#dicitionary
def show(**kwargs):
    print(kwargs)
show(id=123,name='gaurav',age=28,salary=9999)
#DECORATOR FUNCTION
def div(x,y):
    z=x/y
    print(z)
div(5,2)
def div(x,y):
    if(x<y):
        x,y=y,x
    z=x/y
    print(z)
#ENUMERATOR FUNCTN
l=['AVI','eva','ashu']
counter=0
for i in l:
    counter=counter+1
print(counter," ",i)
for i,j in enumerate(l):
    print(i," ",j)