def solve(a, b, c):
    # Find the maximum among a, b, and c
    max_val = max(a, b, c)

    # Calculate the sum of the two smaller integers
    sum_of_smaller = a + b + c - max_val

    # Calculate the result using the given formula
    # If the maximum is greater than (sum_of_smaller + 1) * 2, return -1
    # Otherwise, return the sum of a, b, and c
    return -1 if max_val > (sum_of_smaller + 1) * 2 else a + b + c


# Main function
def main():
    a = 10
    b = 3
    c = 1

    # Function Call
    ans = solve(a, b, c)
    print("length of the string is:", ans)


if __name__ == "__main__":
    main()

