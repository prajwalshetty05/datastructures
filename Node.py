class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linklist:
    def __init__(self):
        self.head=None
    def append(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=newnode
    def display(self):
        last=self.head
        while(last):
            print(last.data)
            last=last.next
    def push(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def removingnode(self,target):
        prednode=None
        currnode=self.head
        while(currnode is not None and currnode.data!=target):
            prednode=currnode
            currnode=currnode.next
        if(currnode is not None):
            if(currnode is self.head):
                self.head=currnode.next
            else:
                prednode.next=currnode.next
    def search(self,x):
        current=self.head
        while(current is not None):
            if current.data==x:
                print("Found")
                return
            current=current.next
        print("not found")
        return
    def insertafter(self,prev,insert):
            last=self.head
            newnode=Node(insert)
            while(last and last.data!=prev):
                last=last.next
            newnode.next=last.next
            last.next=newnode
            
        
    
        
        
        
l1=linklist()
l1.append(5)
l1.append(2)
l1.append(1)
l1.append(9)
l1.display()
print("push")
l1.push(7)
l1.display()
print("removing node")
l1.removingnode(7)
l1.display()
print("insertafter")
l1.insertafter(2,10)
l1.display()
print("search")
l1.search(20)

        