# imports
from tdas.node import Node


class LinkedList:

    def __init__(self) -> None:
        self.head: Node = None
        self.size = 0

    # append a value to the list
    def append(self, value):
        if self.head is None:
            self.head = Node(value, self.size)
        else:
            aux = self.head
            while aux.next is not None:
                aux = aux.next
            aux.next = Node(value, self.size)

        self.size += 1

    # get the value
    def get_node(self, index):
        aux = self.head
        while aux is not None:
            if aux.pos == index:
                return aux.value
            aux = aux.next
        return None

    # delete the first node with a given value
    def delete(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current:
                if current.value == value:
                    break
                prev = current
                current = current.next
            if current is None:
                return
            prev.next = current.next
            current = None

    # print
    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

