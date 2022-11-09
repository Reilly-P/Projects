pieces = int(input())  #How many numbers are in the list


def Potsplit():
    numbers = [int(x) for x in input().split()]  #What are the numbers
    numbers.sort(reverse=True) #Sort the numbers from greatest to least
    alice_pot = 0
    bob_pot = 0

    for i in range (0, pieces, 2):
        alice_pot += int(numbers[i]) #Give Alice the greatest number
        if i < (pieces-1):
            bob_pot += int(numbers[i+1]) #Give Bob the next greatest number

    print(str(alice_pot)+' '+str(bob_pot))
    return(str(alice_pot)+' '+str(bob_pot))

Potsplit()





def Potsplit1():
    numbers.sort(reverse=True)
    alice_pot = 0
    bob_pot = 0

    for i in range (0, pieces, 2):
        alice_pot += int(numbers[i])
        if i < (pieces-1):
            bob_pot += int(numbers[i+1])

    print(str(alice_pot)+' '+str(bob_pot))
    return(str(alice_pot)+' '+str(bob_pot))

print("\nTest cases")

pieces = 5
numbers = [1, 2, 3, 4, 5]
assert(Potsplit1() == "9 6")

pieces = 4
numbers = [2, 2, 3, 3]
assert(Potsplit1() == "5 5")

pieces = 1
numbers = [7]
assert(Potsplit1() == "7 0")