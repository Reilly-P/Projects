H, T = input().split()
S = 0

while (T > 1):
    H += 1
    T -= 2
    S += 1
    print (H, T)
while (H > 0):
    H -= 2
    S += 1 
    print (H, T)