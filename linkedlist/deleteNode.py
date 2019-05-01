# Deleting a node from a list

class Node():
    def __init__(self, dataval=None):
        self.dataval=dataval
        self.nextval=None

class SLinkedList():
    def __init__(self):
        self.headval=None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval

    def Atbegining(self, datain):
        NewNode = Node(datain)
        NewNode.next = self.headval
        self.headval = NewNode

    def RemoveNode(self, removeNode):
        HeadVal = self.headval
        if (HeadVal is not None):
            if (HeadVal.dataval == removeNode):
                self.headval = HeadVal.next
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.dataval == removeNode:
                break
            prev = HeadVal
            HeadVal = HeadVal.next
        if (HeadVal == None):
            return
        prev.next = HeadVal.next
        HeadVal = None

llist = SLinkedList()
llist.Atbegining("Mon")
llist.Atbegining("Tue")
llist.Atbegining("Wed")
llist.Atbegining("Thu")
llist.RemoveNode("Tue")
llist.listprint()
