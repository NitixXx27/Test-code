class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self , newdata):
        if self.head is None:
            self.head = newdata
        else :
            self.head.next