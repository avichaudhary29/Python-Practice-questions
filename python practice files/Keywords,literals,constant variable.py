#Keywords=Predefined words
import keyword
print(keyword.kwlist)

import math
w=89
print(math.factorial(w))
#Literals=value of variables(we can not change value during execution time ,value can be integer, float,string)
x=21
y=21
z=x+y
print(z)
a='avi'
b='chaudhary'
c=a+b
print(c)
# Numeric literals
integer_literal = 42
float_literal = 3.14
scientific_literal = 2.5e3

# String literals
string_literal = "Hello, world!"

# Boolean literals
true_literal = True
false_literal = False

# None literal
none_literal = None

# Character literals (in some languages)
char_literal = 'A'

# Raw string literal
raw_string = r"This is a raw string"

# Escape sequences
escaped_string = "This is a new line:\nSecond line"

# Hexadecimal and Octal literals
hex_literal = 0x1F   # Hexadecimal value 31
oct_literal = 0o17   # Octal value 15

#variable=it is a name we can store single value at  atime
e=100
print(id(e)) #id =memory address
# constant=permanent
import math
print(math.pi)

PI = 3.14159
MAX_VALUE = 100
print(PI,MAX_VALUE)