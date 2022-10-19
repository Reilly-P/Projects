
def Blimps():
    FBIs = 0
    iterations = 0
    lines = ""
    for FBI in range(5):
            registrations = input("Enter some blimp names: ", )
            iterations += 1
            if "FBI" in registrations:
                FBIs += 1
                lines += str(iterations)
                lines += " "

    if FBIs == 0:
        print("HE GOT AWAY!")
    print(lines)

def Test_Blimps(): 
    FBIs = 0
    iterations = 0
    lines = ""
    for FBI in blimps:
            iterations += 1
            if "FBI" in FBI:
                FBIs += 1
                lines += str(iterations)
                lines += " "
    print(FBIs)

    if FBIs == 0:
        print("HE GOT AWAY!")
        return "HE GOT AWAY!"
    print(lines)
    return lines

Blimps()

blimps = ["FBIDave","Meow1!","FBInk","ILikeCats","Nyan"] 
assert Test_Blimps() == "1 3 "
blimps = ["NSA","Not_FBI","CIA","Pizza","FBIStinksLol"]
assert Test_Blimps() == "2 5 " 
blimps = ["Nah", "No", "Gov't", "Blimps", "Here"]
assert Test_Blimps() == "HE GOT AWAY!"