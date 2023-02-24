class BST:
    def __init__(self):
        self.root = None
    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False
    def insert(self, data):
        pNew = BSTNode(data)
        if self.isEmpty():
            self.root = pNew
        else:
            start = self.root
            while start != None:
                prev = start
                if pNew.data < start.data:
                    start = start.left
                else:
                    start = start.right
            if pNew.data < prev.data:
                prev.left = pNew
            else:
                prev.right = pNew
            
    def delete(self, data):
        if self.isEmpty():
            return None
        else:
            start = self.root
            while start.data != data:
                prev = start
                if data < start.data:
                    start = start.left
                else:
                    start = start.right
            # print(start.data)

            # leaf
            if (data == self.root.data) and (start.left == None) and (start.right == None):
                self.root = None
            elif (start.left == None) and (start.right == None):
                if start.data < prev.data:
                    prev.left = None
                else:
                    prev.right = None
            # have 1 child
            elif (start.left == None) or (start.right == None):
                if start.data != self.root.data:
                    if start.data < prev.data:
                        if start.left != None:
                            prev.left = start.left
                        else:
                            prev.left = start.right
                    else:
                        if start.left != None:
                            prev.right = start.left
                        else:
                            prev.right = start.right
                else:
                    if start.left != None and start.right == None:
                        self.root = start.left
                    else:
                        self.root = start.right
            # have 2 child
            else:
                point = start
                start = start.left
                if start.right != None:
                    while start.right != None:
                        prev = start
                        start = start.right
                    point.data = start.data
                    if start.left != None:
                        prev.right = start.left
                    else:
                        prev.right = None
                else:
                    point.data = start.data
                    if start.left != None:
                        point.left = start.left
                    else:
                        point.left = None
            # return data

    def preorder(self, root):
        if (root != None):
            print("->", root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def inorder(self, root):
        if (root != None):
            self.inorder(root.left)
            print("->", root.data, end=" ")
            self.inorder(root.right)
    def postorder(self, root):
        if (root != None):
            self.postorder(root.left)
            self.postorder(root.right)
            print("->", root.data, end=" ")
    def traverse(self):
        print("Preorder ", end="")
        self.preorder(self.root)
        print()
        print("Inorder ", end="")
        self.inorder(self.root)
        print()
        print("Postorder ", end="")
        self.postorder(self.root)
        print()

    def findMin(self):
        start = self.root
        while start != None:
            prev = start
            start = start.left
        return prev.data
    def findMax(self):
        start = self.root
        while start != None:
            prev = start
            start = start.right
        return prev.data

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

myBST = BST()
myBST.insert(101)
myBST.insert(10)
myBST.insert(200)
myBST.insert(100)
myBST.insert(1)
# myBST.traverse()
myBST.delete(101)
myBST.traverse()
# 10 5 8 Error
# myBST.insert()

# print()
# print("Min:", myBST.findMin())
# print("Max:", myBST.findMax())
