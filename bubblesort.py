def bubblesort(ls):
    n=len(ls)
    for i in range(0,n-1):
        for j in range(0,n-1):
            if ls[j]>ls[j+1]:
                temp=ls[j]
                ls[j]=ls[j+1]
                ls[j+1]=temp
ls=[]
n=int(input("enter the total elements"))
for i in range(0,n):
    num=int(input("enter element"))
    ls.append(num)
bubblesort(ls)
for i in range(0,n):
    print(ls[i])

    
    
    