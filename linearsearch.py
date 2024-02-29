def linearsearch(target,ls):
    n=len(ls)
    for i in range(0,n):
        if target==ls[i]:
            print("Searching element found at position:",i+1)
            return
    print("Not Found")
ls=[]
n=int(input("Enter the number of element"))
print("enter elements")
for i in range(0,n):
    lsele=int(input())
    ls.append(lsele)
target=int(input("enter searching element"))
linearsearch(target,ls)