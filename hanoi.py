def towerofhanoi(n,frm,to,aux):
    if n==0:
        return
    towerofhanoi(n-1,frm,aux,to)
    print("move disk",n,"from rod",frm,"to rod",to)
    towerofhanoi(n-1,aux,to,frm)
print("enter number number of disks")
n=int(input())
towerofhanoi(n,"A","C","B")
