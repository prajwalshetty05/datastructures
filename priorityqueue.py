start=None
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def insertend(data):
    global start
    if(start==None):
        newnode=Node(data)
        newnode.next=newnode.prev=newnode
        start=newnode
        return
    last=start.prev
    newnode=Node(data)
    newnode.next=start
    start.prev=newnode
    newnode.prev=last
    last.next=newnode
def insertbegin(data):
    global start
    last=start.prev
    newnode=Node(data)
    newnode.next=start
    newnode.prev=last
    last.next=start.prev=newnode
    start=newnode
def insertafter(value1,value2):
    global start
    newnode=Node(value1)
    temp=start
    while(temp.data!=value2):
        temp=temp.next
    next=temp.next
    temp.next=newnode
    newnode.next=next
    newnode.prev=temp
    next.prev=newnode
    
    
def display():
    global start
    temp=start
    print("forward traversal")
    while(temp.next!=start):
        print(temp.data,end=",")
        temp=temp.next
    print(temp.data)
    print("backward direction")
    last=start.prev
    temp=last
    while(temp.prev!=last):
        print(temp.data,end=",")
        temp=temp.prev
    print(temp.data)
if __name__ == '__main__':
    global start
    start=None
    insertend(5)
    insertbegin(4)
    insertend(7)
    insertend(8)
    insertafter(6,5)
    print("created doubly linked list")
    display()
    
        