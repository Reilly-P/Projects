list = []
iterations = int(input("How many triangular numbers ",))

def print_triangular_numbers():
    print("\n")
    for i in range(0, iterations+1):
        list.append(i)
        print(i, " ", sum(list))
print_triangular_numbers()