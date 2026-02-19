import sys

if len(sys.argv) != 3:
    print("Please provide exactly two numbers.")
    sys.exit()

try:
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])

    print("Add:", n1 + n2)
    print("Sub:", n1 - n2)
    print("Mul:", n1 * n2)

    if n2 != 0:
        print("Division:", n1 / n2)
    else:
        print("Division: Cannot divide by zero.")

except ValueError:
    print("Please enter valid integers:")
