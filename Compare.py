def compare(a,b):
    if a>b:
        print(1)
        return 1
    elif a == b:
        print(0)
        return 0
    elif a < b:
        print(-1)
        return -1

first = int(input("First number: ",))
second = int(input("Second number: ",))

compare(first, second)

print("Test cases:")
assert(compare(5, 4) == 1)
assert(compare(7, 7) == 0)
assert(compare(2, 3) == -1)
assert(compare(42, 1) == 1)