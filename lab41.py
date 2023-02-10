from ArrayStack import *
def isParenthesesMatching(expression):
    check = ArrayStack()
    for i in expression:
        if i == "(":
            check.push("(")
        elif i == ")":
            x = check.pop()
            if x == None:
                break
    if check.isEmpty() == False or x == None:
        print("Parentheses in",expression ,"are unmatched")
        return False
    else:
        return True

str = "(((A-B)*C))"
result = isParenthesesMatching(str)
print(result)
