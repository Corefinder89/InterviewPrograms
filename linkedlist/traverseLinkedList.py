# Traversing a linked list

class Node:
    def __init__(self, dataval=None):
        self.dataval=dataval
        self.nextval=None

class SLinkedList:
    def __init__(self):
        self.headval=None

    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

list = SLinkedList()
list.headval = Node("Monday")
e2 = Node("Tuesday")
e3 = Node("Wednesday")

# Link the first node to the second node
list.headval.nextval = e2

# Link the second node to the third node
e2.nextval = e3

list.listprint()
