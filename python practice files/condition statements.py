# If Statement:
# The basic if statement allows you to execute a block of code only if a certain condition is true.

age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
#If-Elif-Else Statement:
#This structure allows you to handle multiple conditions sequentially.

score = int(input("Enter your test score: "))
if score >= 90:
    print("You got an A.")
elif score >= 80:
    print("You got a B.")
elif score >= 70:
    print("You got a C.")
else:
    print("You need to improve.")

#Nested If Statements:
#You can use if statements inside other if statements to create more complex conditions.
num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

#Ternary Operator:
#A compact way to express a simple if-else statement.

age = int(input("Enter your age: "))
message = "You are an adult." if age >= 18 else "You are a minor."
print(message)

#Switch Statement (Using Dictionary):
#Python doesn't have a built-in switch statement, but you can emulate it using dictionaries.

def switch_case(case):
    switch_dict = {
        'case1': "This is case 1",
        'case2': "This is case 2",
        'case3': "This is case 3"
    }
    return switch_dict.get(case, "Invalid case")

case_input = input("Enter a case: ")
result = switch_case(case_input)
print(result)
