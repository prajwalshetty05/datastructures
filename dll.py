class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
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
        newnode.prev=last
        
        
    def display(self):
        last=self.head
        print("forward")
        while(last):
            print(last.data)
            node=last
            last=last.next
        print("backward")
        while(node):
            print(node.data)
            node=node.next
            
            
            
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
l1.removingnode(5)
l1.display()
print("insertafter")
l1.insertafter(7,10)
l1.display()
print("search")
l1.search(20)