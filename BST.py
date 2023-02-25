from BSTNode import *
class BST:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def insert(self, data):
        pNew = BSTNode(data)
        if self.isEmpty(): #ว่าง
            self.root = pNew
        else:
            start = self.root
            while start is not None:
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

            # leaf
            if (start.left is None) and (start.right is None):
                # root
                if data == self.root.data:
                    self.root = None
                # notRoot
                elif start.data < prev.data:
                    prev.left = None
                else:
                    prev.right = None

            # have 1 child
            elif (start.left == None) or (start.right == None):
                # notRoot
                if start.data != self.root.data:
                    if start.data < prev.data:
                        if start.left is not None:
                            prev.left = start.left
                        else:
                            prev.left = start.right
                    else:
                        if start.left is not None:
                            prev.right = start.left
                        else:
                            prev.right = start.right
                # root
                else:
                    if start.left is not None:
                        self.root = start.left
                    else:
                        self.root = start.right
            # have 2 child
            else:
                point = start
                start = start.left
                if start.right is not None:
                    while start.right is not None:
                        prev = start
                        start = start.right
                    point.data = start.data
                    if start.left is not None:
                        prev.right = start.left
                    else:
                        prev.right = None
                else:
                    point.data = start.data
                    if start.left is not None:
                        point.left = start.left
                    else:
                        point.left = None

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
