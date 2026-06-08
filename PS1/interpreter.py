"""Python already supports math, whereby you can write code to add, subtract, multiply, or divide values and even variables.
 But let's write a program that enables users to do math, even without knowing Python.
Implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a
floating-point value formatted to one decimal place. Assume that the user's input will be formatted as x y z,
with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.
"""

expression = input(
    "Enter an expression in the format x y z where x and z are operands and y is the operator: "
)
expression = expression.split()
if expression[1] == "+":
    print(float(expression[0]) + float(expression[2]))
elif expression[1] == "-":
    print(float(expression[0]) - float(expression[2]))
elif expression[1] == "*":
    print(float(expression[0]) * float(expression[2]))
elif expression[1] == "/" and float(expression[2]) == 0:
    print("Cant divide by zero")
elif expression[1] == "/" and float(expression[2] != 0):
    print(float(expression[0]) / float(expression[2]))
else:
    print("Wrong operator")
