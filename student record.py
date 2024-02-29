n=int(input("enter stu"))
ls=[' ',' ',0,0,' ' ]
for i in range(0,n):
    nm=input("enter name")
    rg=input("enter regno")
    ag=int(input("enter age"))
    phno=int(input("enter phno"))
    add=input("enter address")
print('*'*40)   
for i in range(0,n):
    print("name:",nm)
    print("regno:",rg)
    print("age",ag)
    print("phno",phno)
    print("address",add)
    print('*'*40)