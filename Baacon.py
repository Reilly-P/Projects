N = int(input("input N: "))
lines = []
orders = {}

for i in range(N):
    lines = input().split()
    name = lines[0]
    for j in range((len(lines)-1)):
        if lines [j+1] in orders:
            orders[ lines[j+1] ].append(name)
        else:
            orders.update({lines[j+1]:name})

print(orders)