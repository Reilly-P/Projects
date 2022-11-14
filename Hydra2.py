H = int(input())
T = int(input())
S = 0
def Hydra():
    global T
    global H
    global S
    if H == 0 and T == 0:
        return
    if H*2==T:
        T -= 2
        H += 1
    if H % 2 != 0:
        T -= 2
        H += 1
        print(H,T)
        S += 1
    if T % 4 != 0:
        while True:
            T += 1
            print(H,T)
            S += 1
            if T % 4 == 0:
                break
    if H % 2 == 0:
        H -= 2
        print(H,T)
        S += 1
    if T % 4 == 0:
        while True:
            T -= 2
            H += 1
            print(H,T)
            S += 1
            if T == 0:
                break
    if H >= T:
        while True:
            H -= 2
            print(H,T)
            S += 1
            if H <= T:
                break
        
while H != 0 and T != 0:       
    Hydra()
if H == 0 and T == 0:
    print(S)