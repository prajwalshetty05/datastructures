class Node:
    def __init__(self, col, val):
        self.col = col
        self.val = val
        self.next = None

class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [None] * rows

    def set(self, row, col, val):
        if row < 0 or row >=self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of range")
        if val == 0:
            self.delete(row, col)
            return
        node = self.matrix[row]
        prednode = None
        while node and node.col < col:
            prednode = node
            node = node.next
        if node and node.col == col:
            node.val = val
        else:
            new_node = Node(col, val)
            if not prednode:
                self.matrix[row] = new_node
            else:
                prednode.next = new_node
            new_node.next = node

    def get(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of range")
        node = self.matrix[row]
        prednode = None
        while node and node.col < col:
            prednode = node
            node = node.next
        if node and node.col == col:
            return node.val
        else:
            return 0

    def delete(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of range")
        node = self.matrix[row]
        prednode = None
        while node and node.col < col:
            prednode = node
            node = node.next
        if node and node.col == col:
            if not prednode:
                self.matrix[row] = node.next
            else:
                prednode.next = node.next

    def print(self):
        for row in range(self.rows):
            node = self.matrix[row]
            printed = False
            for col in range(self.cols):
                if node and node.col == col:
                    print(node.val, end=" ")
                    node = node.next
                    printed = True
                else:
                    print(0, end=" ")
            if printed:
                print()

# Example usage
matrix = SparseMatrix(3, 3)

matrix.set(1, 2, 4)
matrix.set(0, 1, 2)
matrix.set(0, 2, 1)
matrix.set(1, 1, 5)

matrix.print()



