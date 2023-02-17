from ArrayStack import ArrayStack
def infixToPostfix(expression):
    stack = ArrayStack()
    doc = {
        "*": 2,
        "/": 2,
        "+": 1,
        "-": 1,
    }
    strRe = ""
    for i in expression:
        if i not in doc:
            strRe += i
        else:
            # i is great more top of stack
            if stack.size() > 0 and doc[i] > doc[stack.stackTop()]:
                stack.push(i)
            # i is low more top of stack
            elif stack.size() > 0 and doc[i] <= doc[stack.stackTop()]:
                while not(stack.isEmpty()):
                    strRe += stack.pop()
                    if stack.size() > 0 and doc[i] > doc[stack.stackTop()]:
                        stack.push(i)
                        break
                    elif stack.isEmpty():
                        stack.push(i)
                        break
            else: #stack is empty
                stack.push(i)
    # end expression and have data in stack
    while not(stack.isEmpty()):
        strRe += stack.pop()
    return strRe

exp = "A+B*C/D-F"
# exp = "A+B*C-D/E"
x = infixToPostfix(exp)
print("Postfix of", exp, "is", x)