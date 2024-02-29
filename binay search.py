def binarysearch(target, ls):
    low = 0
    high = len(ls) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == ls[mid]:
            print("Found", mid + 1)
            return
        elif target < ls[mid]:
            high = mid - 1
        else:
            low = mid + 1
    print("not found")

ls = []
n = int(input("Enter the number of elements: "))
print("Enter elements:")
for i in range(0, n):
    lsele = int(input())
    ls.append(lsele)
target = int(input("Enter searching element: "))
binarysearch(target, ls)