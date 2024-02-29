def selectionsort(ls,n):
    for i in range(0,n):
        small=i
        for j in range(i+1,n):
            if ls[j]<ls[small]:
                small=j
        if small!=i:
            temp=ls[small] 
            ls[small]=ls[i]
            ls[i]=temp
ls=[]
n=int(input("enter no of elements"))
for i in range(0,n):
    lsele=int(input("enter element"))
    ls.append(lsele)
selectionsort(ls,n)
for i in range(0,n):
    print(ls[i])