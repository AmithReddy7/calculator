import sys

if len(sys.argv) != 3:
    print("Please provide exactly two numbers.")
    sys.exit()

try:
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])

    print("Addition:", n1 + n2)
    print("Subtraction:", n1 - n2)
    print("Multiplication:", n1 * n2)

    if n2 != 0:
        print("Division:", n1 / n2)
    else:
        print("Division: Cannot divide by zero.")

except ValueError:
    print("Please enter valid integers.")
