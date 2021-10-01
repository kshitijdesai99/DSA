class Node:
    def __init__(self, data = None):
        self.data = data
        self.left_node = None
        self.right_node = None

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def inorder(self):
        if self.root == None:
            print("Tree is Empty..")
        else:
            self._inorder(self.root)
            
    def _inorder(self,current):
        if current:
            self._inorder(current.left_node)
            print(current.data,end=" ")
            self._inorder(current.right_node)
    
    def preorder(self):
        if self.root == None:
            print("Tree is Empty..")
        else:
            self._preorder(self.root)
            
    def _preorder(self,current):
        if current:
            print(current.data,end=" ")
            self._preorder(current.left_node)
            self._preorder(current.right_node)
    
    def postorder(self):
        if self.root == None:
            print("Tree is Empty..")
        else:
            self._postorder(self.root)
            
    def _postorder(self,current):
        if current:
            self._postorder(current.left_node)
            self._postorder(current.right_node)
            print(current.data,end=" ")
            
    def levelorder(self):
        if self.root == None:
            print("Tree is Empty..")
        else:
            self._levorder(self.root)
    
    def _levorder(self,current):
        queue = []
        queue.append(current)
        while len(queue)>0:
            node1 = queue.pop(0)
            print(node1.data,end=" ")
            if node1.left_node:
                queue.append(node1.left_node)
            if node1.right_node:
                queue.append(node1.right_node)
                    
    def addlevelorder(self,val):
        if(self.root == None):
            self.root = node(val)
        else:
            self._addlevelorder(self.root,val)
    
    def _addlevelorder(self,current,val):
        queue = []
        queue.append(current)
        while len(queue)>0:
            node1 = queue.pop(0)
            if node1.left_node:
                queue.append(node1.left_node)
            if node1.right_node:
                queue.append(node1.right_node)
            if node1.left_node == None:
                node1.left_node = Node(val)
                return
            elif node1.right_node  == None:
                node1.right_node = Node(val)
                return
    

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def inorder(self):
        if self.root == None:
            print("Tree is Empty..")
        else:
            self._inorder(self.root)
            
    def _inorder(self,current):
        if current:
            self._inorder(current.left_node)
            print(current.data,end=" ")
            self._inorder(current.right_node)
    
    def preorder(self):
        if self.root == None:
            print("Tree is Empty..")
        else:
            self._preorder(self.root)
            
    def _preorder(self,current):
        if current:
            print(current.data,end=" ")
            self._preorder(current.left_node)
            self._preorder(current.right_node)

    def postorder(self):
        if self.root == None:
            print("Tree is Empty..")
        else:
            self._postorder(self.root)
            
    def _postorder(self,current):
        if current:
            self._postorder(current.left_node)
            self._postorder(current.right_node)
            print(current.data,end=" ")
            
    def levelorder(self):
        if self.root == None:
            print("Tree is Empty..")
        else:
            self._levorder(self.root)
    
    def _levorder(self,current):
        queue = []
        queue.append(current)
        while len(queue)>0:
            node1 = queue.pop(0)
            print(node1.data,end=" ")
            if node1.left_node:
                queue.append(node1.left_node)
            if node1.right_node:
                queue.append(node1.right_node)
            
    def addNode(self,value):
        if(self.root == None):
            self.root = Node(value)
        else:
            self._addnode(self.root,value)
        
    def _addnode(self,current,val):
        if(current.data > val):
            if(current.left_node == None):
                current.left_node = Node(val)
            else:
                self._addnode(current.left_node,val)
        elif(current.data < val):
            if(current.right_node == None):
                current.right_node = Node(val)
            else:
                self._addnode(current.right_node,val)
        else:
            print("Value is already addded in the tree")


    
obj1 = BinaryTree()
first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth  = Node(6)
seventh = Node(7)
obj1.root = first
first.left_node = second
first.right_node = third
second.left_node = fourth
second.right_node = fifth
third.right_node = seventh
third.left_node = sixth
obj1.addlevelorder(8)
obj1.addlevelorder(9)

obj1.inorder()
print('\n')
obj1.preorder()
print('\n')
obj1.postorder()
print('\n')
obj1.levelorder()
print('\n')
obj2 = BinarySearchTree()
obj2.addNode(10)
obj2.addNode(5)
obj2.addNode(2)
obj2.addNode(15)
obj2.addNode(23)

obj2.levelorder()
