strg = input()
new_str = ""
new_str += strg[0]
list_str = []
list_str.append(strg[0])

for i in range(1,len(strg)):
    if strg[i] != strg[i-1]:
        new_str = new_str + strg[i]

print(new_str)