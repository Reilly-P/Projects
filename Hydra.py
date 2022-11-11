3,3
1,3
2,1
0,1
2,0
0,0


H = 3
T = 3

def One():
    global H
    pass
def Two():
    global T
    T = T + 1 
def Three():
    global T
    global H
    T = T - 2
    H = H + 1
    
def Four():
    global T
    global H
    H = H - 2
    

def kill():
    if H % 2 == 0:
        Four()

    if H % 2 != 0: 
        if T >= 3 and T % 2 == 0:
            Three()
        else:
            Two()
        if T <= 3 and T % 2 != 0:
            Two()
        else:
            Three()
    
    if H == 0: 
        if T >= 3 and T % 2 == 0:
            Three()
        elif T <= 3 and T % 2 != 0:
            Two()
        elif T <= 3 and T % 2 == 0:
            Two()
while H != 0 and T != 0:
    kill()
    print(H, T)



#    if H % 2 != 0: 
#        if T >= 3 and T % 2 == 0:
#            Three()
#        elif T >= 3 and T % 2 != 0:
#            Two()
#        if T <= 3 and T % 2 == 0 :
#            if H == 0:
#                Two()
#            elif H != 0:
#                Three()
#        elif T <= 3 and T % 2 != 0:
#            Two()