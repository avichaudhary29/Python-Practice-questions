#8
for i in range(6, 0, -1):  # Loop from 6 to 1 in reverse
    for j in range(0, i):  # Loop from 0 to i-1 (inclusive)
        print("*", end=" ")  # Print an asterisk followed by a space
    print()  # Move to the next line after printing each row
#9
for i in range(1, 7):  # Loop from 1 to 6
    for j in range(i):  # Loop from 0 to i-1 (inclusive)
        print("*", end=" ")  # Print an asterisk followed by a space
    print()  # Move to the next line after printing each row
#10
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)
#11Hollow Pyramid Pattern:
for i in range(1, 6):
    if i == 1 or i == 5:
        print("* " * i)
    else:
        print("* " + "  " * (i - 2) + "* ")
#12 Diamond Pattern:
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)

#13
alphabet = "abcdefghijklmnopqrstuvwxyz"
n = 5
for i in range(n):
    print(" ".join(alphabet[:i+1]))

#14 Numeric Right Triangle Pattern:

for i in range(1, 6):
    print(" ".join(map(str, range(1, i + 1))))
# 15 Alphabet Pyramid Pattern:
alphabet = 'abcdefghijklmnopqrstuvwxyz'
n = 5
for i in range(1, n + 1):
    spaces = " " * (n - i)
    chars = ""
    for j in range(i):
        chars += alphabet[j] + " "
    print(spaces + chars)

# 16 numeric
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + " ".join(map(str, range(1, i + 1))))
