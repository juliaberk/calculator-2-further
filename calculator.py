"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

# from arithmetic import *
from arithmetic_list import *


while True:

    user_input = raw_input("> ")

    tokenized = user_input.split(',')

    for item in tokenized:
        item = item.strip(']')
        item = item.strip('[')
    split_t = tokenized[1:]
    int_list = []
    operator = tokenized[0]

    for item in split_t:
        int_list.append(int(item))

    if len(int_list) > 0:
        num1 = int_list[0]
        if len(int_list) > 1:
            num2 = int_list[1]

    if user_input.lower() == 'q':
        break

    else:

        if operator == "+":
            solution = add(num1, num2)

        elif operator == "-":
            solution = subtract(num1, num2)

        elif operator == "*":
            solution = multiply(num1, num2)

        elif operator == "/":
            solution = divide(float(num1), num2)

        elif operator == "square":
            solution = square(num1)

        elif operator == "cube":
            solution = cube(num1)

        elif operator == "pow":
            solution = power(num1, num2)

        elif operator == "mod":
            solution = mod(num1, num2)

    print solution