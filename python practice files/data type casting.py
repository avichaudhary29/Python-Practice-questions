'''Data type casting, ya type conversion, ek programming concept hai jisme aap ek data type ko doosre data type mein convert karte hain. Isse aksar different data types ke values ko ek saath use karne mein madad milti hai. Data type casting do tariko se ho sakta hai: implicit (automatic) type casting aur explicit (manual) type casting.

Implicit Type Casting (Automatic Type Casting):
Implicit type casting, jab Python khud hi data types ko convert karta hai, bina aapke intervention ke, usse hota hai. Yeh kabhi-kabhi "coercion" ke roop mein bhi jaana jata hai. Implicit type casting generally data loss na ho, to wo automatic ho jata hai. Yeh example samjhne mein madad karega:
'''
num_int = 5    # Integer
num_float = 2.5  # Floating-point number

result = num_int + num_float  # Yahan num_int ko implicit cast kar ke float mein convert kar liya jata hai
print(result)  # Output: 7.5
'''Explicit Type Casting (Manual Type Casting):
Explicit type casting, jab aap khud manually ek data type ko doosre data type mein convert karte hain, usse hota hai. Ismein aap "type constructors" ya "casting functions" ka istemal karte hain. Is tarah ke casting mein data loss ho sakta hai, isliye dhyan se karna hota hai.

Kuch common explicit casting functions hain:

int(): Integer mein convert karta hai.
float(): Floating-point number mein convert karta hai.
str(): String mein convert karta hai.
'''
num_str = "10"  # String

num_int = int(num_str)  # Yahan num_str ko explicit cast kar ke integer mein convert kiya gaya hai
print(num_int + 5)  # Output: 15

######
x=int(input("enter value"))
print(x)
x=float(input("enter value"))
y=int(x)
print(y)