# My name is Reilly and this is my progam for executing numerous math functions with prompted numbers and two test cases with predetermined numbers. I think I did that right.

import math
def Addition():
    print("Here are the two numbers added:", a+b)
    return a+b
def Subtraction():
    print("Here is the first number subtracted from the second: ", b-a)
    return b-a
def Multiplication():
    print("Here are the two numbers multiplied: ", a*b)
    return a*b
def Division():
    print("Here is the first number divided by the second: ", a/b)
    return a/b
def Remainder():
    print("Here is the remainder of the first number divided by the second: ", a%b)
    return a%b
def Exponent():
    print("Here is the first number to the power of the second: ", a**b)
    return a**b
def Root():
    print("Here is the square root of the first number: ",math.sqrt(a),)
    return math.sqrt(a)
def Greater():
    print("Here is the greater of the two numbers: ")
    if a>b:
        print(a)
        return a
    elif b>a:
        print(b)
        return b
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
    global a
    global b
    a = 10
    b = 15
    print("a =", a, "b =", b)
    assert(Addition() == 25)
    assert(Subtraction() == 5)
    assert(Multiplication() == 150)
    assert(Division() == 0.6666666666666666)
    assert(Remainder() == 10)
    assert(Exponent() == 1000000000000000)
    assert(Root() == 3.1622776601683795)
    assert(Greater() == 15)

def Test_Function2():
    global a
    global b
    a = 4
    b = 23
    print("a =", a, "b =", b)
    assert(Addition() == 27)
    assert(Subtraction() == 19)
    assert(Multiplication() == 92)
    assert(Division() == 0.17391304347826086)
    assert(Remainder() == 4)
    assert(Exponent() == 70368744177664)
    assert(Root() == 2.0)
    assert(Greater() == 23)

Test_Function()
input("Press enter to continue")
Test_Function2()

