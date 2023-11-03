#(and) returns true if both statements are true 
x=10
y=20
print(x==10 and x<y and y==x) 
#(or) returns true if one of the statement is true != not equal to 10
print(x>y or y==20 or x!=10) 
#(not) reverse the result ,returns false if the result is true jo bhi ans ane wala h use reverse kr dega
not(x<10 and x<10)
print(not x!=10)

#Membership operator ( is mai in & not in ata h cheezo ko check krne keliye use hota loop chalane ki jarurat nhi)
#in - returns true if a sequence with the specified value is present in the object.
string1="Hello"
print('H' in string1 ) #kya is string mai H naam ka variable h 

#not in -returns true if a sequence with the specified value is not present in the object.

l=[10,20,30,40]
print(50 not in l)  # ye vha use hota h jha multiple value use hoti h

#Identity operators in python
# is return if both variables are the same object
x=10
y=10
print(x is y , x==y)
# is not returns true if both variables are not the same object
print (x is not y,x!=y )
# bitwise operators 1=true ,0=false
#&=AND x&y
x=10
y=8
print(bin(x))
print(bin(y))
print(x&y,bin(x&y) ,x&y) #0b1010 0b1000 &1000  8
#|=OR x|y
print(x|y,bin(x|y) ,x|y)
#^=XOR x^y
print(x^y,bin(x^y) ,x^y)
