# My name is Reilly and this is my progam for executing numerous math functions with prompted numbers and two test cases with predetermined numbers. I think I did that right.

import math
def Addition():
    print("Here are the two numbers added:", a+b)
def Subtraction():
    print("Here is the first number subtracted from the second: ", b-a)
def Multiplication():
    print("Here are the two numbers multiplied: ", a*b)
def Division():
    print("Here is the first number divided by the second: ", a/b)
def Remainder():
    print("Here is the remainder of the first number divided by the second: ", a%b)
def Exponent():
    print("Here is the first number to the power of the second: ", a**b)
def Root():
    print("Here is the square root of the first number followed by the square root of the second: ",math.sqrt(a),", ",math.sqrt(b))
def Greater():
    print("Here is the greater of the two numbers: ")
    if a>b:
        print(a)
    elif b>a:
        print(b)
    else:
        print("They are equal")

a = float(input("Input a number: "))
b = float(input("Input another number: "))

Addition()
Subtraction()
Multiplication()
Division()
Remainder()
Exponent()
Root()
Greater()

input("Press enter to see test cases")

def Test_Function():
    print("a =", a, "b =", b)
    Addition()
    Subtraction()
    Multiplication()
    Division()
    Remainder()
    Exponent()
    Root()
    Greater()

a = 10
b = 15
Test_Function()
input("Press enter to continue")
a = 4
b = 23
Test_Function()
