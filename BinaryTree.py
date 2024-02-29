class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.value=key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.value==key:
            return root
        elif(root.value<key):
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)
def search(root,key):
    if root is None or root.value==key:
        print("element found")
        return root
    if root.value<key:
        return search(root.right,key)
    return search(root.left,key)
r=Node(50)
r=insert(r,30)
r=insert(r,20)
r=insert(r,40)
r=insert(r,70)
r=insert(r,60)
r=insert(r,80)
inorder(r)
r=search(r,10)
