class ArrayStack:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.data)

    def push(self, data):
        self.data.append(data)
        return self.data

    def pop(self):
        if len(self.data) == 0:
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            out = self.data.pop()
            return out

    def stackTop(self):
        return self.data[-1]

    def printStack(self):
        print(self.data)

# myStack = ArrayStack()
# myStack.push(10); myStack.push(20); myStack.push(30)
# myStack.printStack()
# x = myStack.pop()
# print(x)
# myStack.pop()
# myStack.printStack()
# myStack.pop()
# print(myStack.isEmpty())
# myStack.pop()
