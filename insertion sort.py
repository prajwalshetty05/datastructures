def insertionsort(ls):
    n = len(ls)
    for i in range(0,n):
        value = ls[i]
        pos = i
        while pos > 0 and value < ls[pos-1]:
            ls[pos] = ls[pos-1]
            pos -= 1
        ls[pos] = value

ls = []
n = int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(0,n):
    lsele = int(input())
    ls.append(lsele)

insertionsort(ls)
print("Sorted sequence",ls)