
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
        return self            


    def addRightNode(self, n):
        if self.right is None:
            self.right = n
        else:            
            self.right.number = n.number
        return self
        
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
#                if current_node.left.number > current_node.right.number:
#                    self.s += current_node.left.number
                    self.printAll(current_node.left)
#                else:
 #                   self.s += current_node.right.number
                    self.printAll(current_node.right)
        
        

root = node(75)
t = Tree(root)


root.addLeftNode(node(95))  #root.left
root.addRightNode(node(64)) # root.right
root.left.addLeftNode(node(17)) #root.left.left
root.left.addRightNode(node(47)) #root.left.right , root.right.left
root.right.addRightNode(node(82)) #root.right.right
root.right.left = root.left.right
l_31 = root.left.left
l_32 = root.left.right
l_33 = root.right.right

l_31.addLeftNode(node(18))  #root.left.left.left
l_31.addRightNode(node(35)) #root.left.left.right
l_32.left = l_31.right
l_32.addRightNode(node(87)) #root.left.right.right
l_33.left = l_32.right
l_32.addRightNode(node(10)) #root.right.right.right

root.left.left.left.addLeftNode(node(20)) #root.left.left.left.left
root.left.left.left.addRightNode(node(4)) #root.left.left.left.right
root.left.left.left.right = root.left.left.right.left

t.printAll(root)
print("S = ", t.s)
