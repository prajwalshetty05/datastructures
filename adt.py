class student:
    def __init__(self,name,regno,age,phno):
        self.name=name
        self.regno=regno
        self.age=age
        self.phno=phno
    def accept(self,name,regno,age,phno):
        obj=student(name,regno,age,phno)
        ls.append(obj)
    def display(self,obj):
        print(obj.name)
        print(obj.regno)
        print(obj.age)
        print(obj.phno)
    def search(self,rn):
        for i in range(ls.__len__()):
            if(ls[i].regno==rn):
                return i
    def delete(self,rn):
        i=obj.search(rn)
        del ls[i]
    def update(self,rn,ag):
        i=obj.search(rn)
        ls[i].age=ag
ls=[]
obj=student(' ',' ',0,0)
for i in range(0,2):
    name=input("enter name")
    regno=input("enter regno")
    age=int(input("enter age"))
    phno=int(input("enter phno"))
for i in range(ls.len()):
    obj.display(ls[i])
ser=input("enter regno to search")
s=obj.search(ser)
obj.display(ls[s])
dl=int(input("enter reg no you want to delete"))
obj.delete(dl)
for i in range(ls.len()):
    obj.display(ls[i])
rn=input("enter regno of student to be updated")
ag=int(input("enter age you want to change"))
obj.update(rn,ag)
for i in range(ls.len()):
    obj.display(ls[i])

