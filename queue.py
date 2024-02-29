class Queue:
    def __init__(self,n):
        self.queue=[]
        self.front=0
        self.rear=0
        self.capacity=n
    def enqueue(self,data):
        if(self.rear==self.capacity):
            print("Queue is full")
        else:
            self.queue.append(data)
            self.rear+=1
    def dequeue(self):
        if self.front==self.rear:
            print("Queue is empty")
        else:
            self.queue.pop(0)
            self.rear-=1
    def display(self):
        if(self.front==self.rear):
            print("Queue is empty")
        for i in self.queue:
            print(i)
q=Queue(4)
print("enqueue")
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.display()
print("dequque")
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.display()
            