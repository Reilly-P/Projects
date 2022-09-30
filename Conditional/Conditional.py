#My name is Reilly Presott and this is my Conditionals program

def main():
    global a, b, c, d, e
    a = float(input("Input a number: ", ))
    b = float(input("Input a number: ", ))
    c = float(input("Input a number: ", ))
    d = float(input("Input a number: ", ))
    e = float(input("Input a number: ", ))
    global Five
    Five = [a, b, c, d, e]
    Sum()
    Product()
    Average()
    Largest()
    Smallest()
    again = input("Shall we go again? (Y/N) ", )
    if again == "Y":
        main()
    elif again == "N":
        print("Test Cases!")
        test()
        quit()

def test():
    global a, b, c, d, e
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    global Five
    Five = [a, b, c, d, e]
    print("a = 1, b = 2, c = 3, d = 4, e = 5")
    assert(Sum() == 15.0)
    assert(Product() == 120.0)
    assert(Average() == 3.0)
    assert(Largest() == 5.0)
    assert(Smallest() == 1.0)
    print("a = 13, b = 63, c = 22, d = 31, e = 5")
    a = 13
    b = 63
    c = 22
    d = 31
    e = 5
    Five = [a, b, c, d, e]
    assert(Sum() == 134.0)
    assert(Product() == 2792790.0)
    assert(Average() == 26.8)
    assert(Largest() == 63.0)
    assert(Smallest() == 5.0)

def Sum():
    sum = a+b+c+d+e
    print("The Sum is: ", sum)
    return sum
def Product():
    product = a*b*c*d*e
    print("The Product is: ", product)
    return product
def Average():
    average = (a+b+c+d+e)/5
    print ("The average is: ", average)
    return average
def Largest():
    for i in Five:
        if i >= a:
            if i >= b:
                if i >= c:
                    if i >= d:
                        if i >= e:
                            print("The largest number of the set is: ", i)
                            return i

def Smallest():
    for i in Five:
        if i <= a:
            if i <= b:
                if i <= c:
                    if i <= d:
                        if i <= e:
                            print("The smallest number of the set is ", i)
                            return i

main()