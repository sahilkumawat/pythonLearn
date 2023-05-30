# Create a Linked List
class Node:
    data = ""
    next = None

    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    tail = None
    head = None

    def __init__(self):
        self.tail = None
        self.head = None

    def appendToBeginning(self, data):
        node = Node(data, self.head)
        if self.head is None:
            self.tail = node
        self.head = node

    def printList(self):
        while self.head.next:
            print(self.head.data)
            self.head = self.head.next
        print(self.head.data)

    def insertItem(self, previtem, data):
        current_item = self.head
        while current_item:
            if current_item.data == previtem:
                new_node = Node(data, current_item.next)
                current_item.next = new_node
            current_item = current_item.next

    def deleteItem(self, item):
        current_item = self.head
        if current_item.data == item:
            self.head = current_item.next
            return
        while current_item.next:
            if current_item.next.data == item:
                if current_item.next is self.tail:
                    self.tail = current_item
                    self.tail.next = None
                    return
                current_item.next = current_item.next.next
            current_item = current_item.next

nodes = LinkedList()

nodes.appendToBeginning(1)
nodes.appendToBeginning(2)
nodes.appendToBeginning(3)
nodes.appendToBeginning(4)
nodes.appendToBeginning(5)

nodes.insertItem(3, 2.5)

# nodes.deleteItem(3)
nodes.deleteItem(1)

nodes.printList()
