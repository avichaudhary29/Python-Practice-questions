'''If statement
if[conditional expression]:
    [statement(s) to execute]   #agr condition true hue to output ae ga vrna nhi ae ga jo likhe ge us mai ek space ae ga
'''  
a=int(input("Enter the value :"))
if a%2==0:
    print(a,"even number")
#if else jb use krte h jb ya to if true ho ya else true ye dono ke liye use hota h
#if[conditional expression]:
#    [statement to execute]
#else:
#    [alternate statement to execute]        

a=int(input("Enter the value :"))
if a%2==0:
 print(a,"even number")
else:
     print("odd number")

#if elif else (jb ek se jada camparision krne ho)
#if[condition 1]:
#        [statement 1]
#elif[condition 2]:
#         [statement 2]
#elif[condition 3]:
#       [statement 3]
#else:
#        [statement when if and elif(s) are false]
per=int(input("Enter the value: "))
if per>=60:
    print("First Div")
elif per>=48:
    print("second div")
elif per>=35:
    print("third div")
else:
    print("fail")            