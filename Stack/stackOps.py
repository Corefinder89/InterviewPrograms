# Push elements to stack
class Stack():
    def __init__(self):
        self.stack = []

    # Add element to a Stack
    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    # Check for the first element in the Stack
    def peek(self):
        return self.stack[-1]

    # Pop elements from the Stack
    def pop(self):
        if len(self.stack)<=0:
            return("No element in the stack")
        else:
            return self.stack.pop()

    # Check elements in the list
    def check_elements(self):
        print("Elements in the list are")
        for i in self.stack:
            print(i)

stack = Stack()
print("Adding element to the stack")
stack.add("Monday")
stack.add("Tuesday")
stack.add("Wednesday")

print("Peeking ...")
print(stack.peek())

print("Adding element back to the stack again")
stack.add("Thursday")
print(stack.peek())

print("Pop element from the stack")
print(stack.pop())
