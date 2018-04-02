
class node():
    def __init__(self, number):
        self.number = number
        self.left = None
        self.right = None
            
    def addLeftNode(self, n):
        if self.left is None:
            self.left = n
        else:
            self.left.number = n.number


    def addRightNode(self, n):
        if self.right is None:
            self.right = n
        else:            
            self.right.number = n.number

        
class Tree():
    root = None

    def __init__(self,n):
        if (self.root is None):
            self.root = node(n)
            self.s = 0
            self.path = []

    def printAll(self, current_node):
        if current_node is not None:
            print(current_node.number)
            if current_node.left is not None and current_node.right is not None:
                if current_node.left.number > current_node.right.number:
                    self.s += current_node.left.number
                    self.printAll(current_node.left)
                else:
                    self.s += current_node.right.number
                    self.printAll(current_node.right)
        
        

root = node(75)
t = Tree(root)

root.addLeftNode(node(95))
root.addRightNode(node(64))
root.left.addLeftNode(node(17))
root.left.addRightNode(node(47))
root.right.addLeftNode(node(47))
root.right.addRightNode(node(82))
root.left.left.addLeftNode(node(18))
root.left.left.addRightNode(node(35))
root.left.right.addLeftNode(node(35))
root.left.right.addRightNode(node(87))
root.left.left.left.addLeftNode(node(20))
root.left.left.left.addRightNode(node(4))

root.left.right.left.addLeftNode(node(4))
root.left.right.left.addRightNode(node(82))



t.printAll(root)
print("S = ", t.s)
