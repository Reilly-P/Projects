s = "This book is old. This piano is old. My parents are old."
print(s)
def Replace(s,old,new): 
    new = new.join(s.split(old))
    print(new)

Replace(s, "old", "new")