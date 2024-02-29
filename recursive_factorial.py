def recursive_factorial(n):
    if n==1:
        return n
    else:
        return n*recursive_factorial(n-1)
print("enter a number")
num=int(input())
if num<0:
    print("invalid input")
elif num==0:
    print("factorial of 0 is 1")
else:
    print("factorial of number",num,"is:",recursive_factorial(num))