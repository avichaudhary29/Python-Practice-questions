'''Arithmetical Operator
Arithmetical Operators:
These operators are used for basic arithmetic operations.

+ (Addition)
- (Subtraction)
* (Multiplication)
/ (Division)
% (Modulus - remainder of division)
// (Floor Division - division with rounding down)
** (Exponentiation)'''
a = 10
b = 4

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulus = a % b
floor_division = a // b
exponentiation = a ** b

print(addition, subtraction, multiplication, division, modulus, floor_division, exponentiation)
'''Relational Operator
These operators are used to compare values and determine relationships.

== (Equal to)
!= (Not equal to)
< (Less than)
> (Greater than)
<= (Less than or equal to)
>= (Greater than or equal to)'''
x = 5
y = 7

is_equal = x == y
not_equal = x != y
less_than = x < y
greater_than = x > y
less_than_equal = x <= y
greater_than_equal = x >= y

print(is_equal, not_equal, less_than, greater_than, less_than_equal, greater_than_equal)
'''Conditional operator
Python has a conditional operator for concise if-else statements.

x if condition else y'''

age = 18
status = "Minor" if age < 18 else "Adult"
print(status)


'''Logical Operator
These operators are used to perform logical operations.

and (Logical AND)
or (Logical OR)
not (Logical NOT)'''

p = True
q = False

logical_and = p and q
logical_or = p or q
logical_not = not p

print(logical_and, logical_or, logical_not)

'''Assignment Operator
These operators are used to assign values to variables.

= (Assignment)
+= (Add and assign)
-= (Subtract and assign)
*= (Multiply and assign)
/= (Divide and assign)
%= (Modulus and assign)
//= (Floor divide and assign)
**= (Exponentiate and assign)'''

x = 10
x += 5  # x = x + 5
x -= 3  # x = x - 3
x *= 2  # x = x * 2
x /= 4  # x = x / 4

print(x)


'''Binary operator
Binary operators work on binary (bit-level) representations of data.

& (Bitwise AND)
| (Bitwise OR)
^ (Bitwise XOR)
<< (Left shift)
>> (Right shift)'''
num1 = 10  # 1010 in binary
num2 = 5   # 0101 in binary

bitwise_and = num1 & num2
bitwise_or = num1 | num2
bitwise_xor = num1 ^ num2
left_shift = num1 << 1  # Shift left by 1 bit
right_shift = num1 >> 1  # Shift right by 1 bit

print(bitwise_and, bitwise_or, bitwise_xor, left_shift, right_shift)

'''Identity operator
These operators are used to compare the memory addresses of two objects.

is (True if both variables point to the same object)
is not (True if both variables do not point to the same object)'''

a = [1, 2, 3]
b = a
c = [1, 2, 3]

is_same_a_b = a is b
is_same_a_c = a is c
is_not_same_a_c = a is not c

print(is_same_a_b, is_same_a_c, is_not_same_a_c)


'''membership operator
These operators check for membership in a sequence (like lists, strings, tuples).

in (True if value is found in the sequence)
not in (True if value is not found in the sequence)'''
my_list = [1, 2, 3, 4, 5]

is_in_list = 3 in my_list
is_not_in_list = 6 not in my_list

print(is_in_list, is_not_in_list)


'''special operator
This isn't a specific category, but it might refer to operators like the identity and membership operators mentioned earlier.'''
x = 10
y = 20

result = x if x > y else y
print(result)


'''comparison operator
Comparison operators are part of the relational operators and are used to compare two values.

== (Equal to)
!= (Not equal to)
< (Less than)
> (Greater than)
<= (Less than or equal to)
>= (Greater than or equal to)'''

x = 10
y = 20

result = x if x > y else y
print(result)
