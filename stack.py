stack=[]
n=int(input("enter number of elements"))
for i in range(0,n):
    ele=int(input("enter elements to insert"))
    stack.append(ele)
print("append operation")
for element in stack:
    print(element)
print("pop operation")
for i in range(0,n):
    print(stack.pop())
    
    