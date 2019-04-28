# Insert at the beginning of the list
class Node:
    def __init__(self, dataval=None):
        self.dataval=dataval
        self.nextval=None

class SLinkedList:
    def __init__(self):
        self.headval=None

# Traverse linked list
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval

# Insert node at the beginning of the list
    def atbeginningofnode(self, newdata):
        newnode = Node(newdata)
        # Update the new node next val to the existing node
        newnode.nextval = self.headval
        self.headval = newnode

list = SLinkedList()
list.headval = Node("Monday")
e2 = Node("Tuesday")
e3 = Node("Wednesday")
list.headval.nextval=e2
e2.nextval=e3
list.atbeginningofnode("Sunday")
list.listprint()
