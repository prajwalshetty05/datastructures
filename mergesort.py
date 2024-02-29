def mergesort(ls1,ls2):
    n1=len(ls1)
    n2=len(ls2)
    a=0
    b=0
    while(a<n1 and b<n2):
        if ls1[a]<ls2[b]:
            nwls.append(ls1[a])
            a+=1
        else:
            nwls.append(ls2[b])
            b+=1
    while(b<n2):
      nwls.append(ls2[b])
      b+=1
    while(a<n1):
        nwls.append(ls1[a])
    n=len(nwls)
    print(nwls)
nwls=[]
ls1=[]
n=int(input("enter number of elements"))
print("enter list 1 elements ")
for i in range(0,n):
    num=int(input())
    ls1.append(num)
ls2=[]
n=int(input("enter number of elements"))
print("enter list 2 elements ")
for i in range(0,n):
    num=int(input())
    ls2.append(num)
mergesort(ls1,ls2)