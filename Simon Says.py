lines = input("How many instructions? ",)

for i in range(int(lines)):
    text = input("Input a command: ",)
    if "Simon says " in text:
        text = text.replace("Simon says ",'')
        print(text)
    else:
        if "Simon says " not in text:
            print("") 