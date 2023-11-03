x=int(input("enter the age"))
y=int(input("Enter the number"))
if(x>y):
    print("X is largest number ")
else:
    print("Y is largets number ")


#nested if
x = int(input("Enter the value: "))
if x >= 10 and x <= 50:
    if x % 2 == 0:
        print("x is even number")
    else:
        print("x is odd number")
else:
    print("Number is out of range")

#ladder if
x=int(input('Enter the value'))
if(x==1):
    print("Sunday")
elif(x==2):
    print("Monday")
elif(x==3):
    print("Tuesday")
else:
    print("Wrong number")

#3
print("1 add")
print("2 mul")
print("3 sub")
print("4 exit")
x=int(input("Enter the choice"))
a=int(input("Enter the value"))
b=int(input("Enter the second value"))

if (x==1):
    c=a+b
    print(c)
elif(x==2):
    c=a*b
    print(c)
elif(x==3):
    c=a-b
    print(c)
else:
    print("wrong")

    #4
# First loop: Counting from 0 to 19 with a step size of 1 (default)
for i in range(0, 20):
    print(i)

# Second loop: Same as the first loop, unnecessary to specify step size
for i in range(0, 20, 1):
    print(i)

# Third loop: Counting from 0 to 18 with a step size of 2
for i in range(0, 20, 2):
    print(i)

    #5
    # First loop: Counting from 1 to 10
    for i in range(1, 11):
        print(i)

    # Second loop: Counting from 10 to 1 in reverse
    for i in range(10, 0, -1):
        print(i)

    # Third loop: Multiplying i by a constant (let's assume x is 5)
    x = 5  # Define the constant
    for i in range(1, 11):
        print(x * i)
#6
x = 0  # Initialize x with 0
while x <= 10:  # The loop condition checks if x is less than or equal to 10
    print(x)    # Print the current value of x
    x = x + 1   # Increment x by 1 in each iteration
#7
x = 15  # Initialize x with the value 15
while x >= 10 and x <= 50:  # Loop as long as x is within the range 10 to 50
    print(x)  # Print the current value of x
    x = x + 1  # Increment x by 1 in each iteration

# The loop will continue executing as long as x is between 10 and 50.
# In each iteration, x is printed and then incremented by 1.
# The loop will stop when x becomes greater than 50.
