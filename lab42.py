from ArrayStack import *
def copyStack(stack1, stack2):
    stack3 = ArrayStack()
    while not(stack2.isEmpty()):
        stack2.pop()
    while not(stack1.isEmpty()):
        x = stack1.pop()
        stack3.push(x)
    while not(stack3.isEmpty()):
        x = stack3.pop()
        stack1.push(x)
        stack2.push(x)

s1 = ArrayStack()
s1.push(10); s1.push(20); s1.push(30)
s2 = ArrayStack()
s2.push(15)
s1.printStack()
s2.printStack()
copyStack(s1, s2)
s1.printStack()
s2.printStack()