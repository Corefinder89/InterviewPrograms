# Program to reverse a string using stack

def stackCreate():
    stack = []
    return stack

def stackSize(stack):
    size = len(stack)
    return size

def stackEmpty(stack):
    if stackSize(stack) == 0:
        return true

def stackPush(stack, item):
    stack.append(item)

def stackPop(stack):
    if stackEmpty(stack): return
    return stack.pop()

def reverseString(string):
    n = len(string)

    stack = stackCreate()

    for i in range(0,n,1):
        stackPush(stack, string[i])

    string = ""

    for i in range(0,n,1):
        string+=stackPop(stack)

    return string

string = "GeeksforGeeks"
print reverseString(string)
