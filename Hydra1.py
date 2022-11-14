H = int(input())
T = int(input())
def One():
    global T
    global H
    if H == 0 and T == 0:
        return
    pass
    print(H,T)
def Two():
    global T
    global H
    if H == 0 and T == 0:
        return
    T = T + 1
    print(H,T)
def Three():
    global T
    global H
    if H == 0 and T == 0:
        return
    T = T - 2
    H = H + 1
    print(H,T)
def Four():
    global T
    global H
    if H == 0 and T == 0:
        return
    H = H - 2
    print(H,T)

def Kill():
    if H % 2 != 0:
        Three()
    if T % 4 != 0:
        while True:
            Two()
            if T % 4 == 0:
                break
    if H % 2 == 0:
        Four()
    if T % 4 == 0:
        while True:
            Three()
            if T == 0:
                break
    if H >= T:
        while True:
            Four()
            if H < T:
                break
        
        
while H != 0 and T != 0:
    Kill()
    
    
    
