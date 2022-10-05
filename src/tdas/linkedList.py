# imports
from tdas.node import Node

# this class is going to work as LIFO, FIFO and linkedList
# LIFO to managed active desk
# FIFO to managed clients in the tail


class LinkedList:

    def __init__(self) -> None:
        self.head: Node = None
        self.size = 0

    # append a value to the list
    # this append at the end
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
    # get first node -> to FIFO
    def get_first(self):
        head = self.head
        self.head = self.head.next
        self.size -= 1
        return head.value

    # get last node -> LIFO
    def get_last(self):
        current = self.head
        next = current.next
        while next is not None:
            current = next
            next = current.next
        return current.value

    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    # print
    def print_client_value(self):
        current = self.head
        while current:
            print(current.value.print_client())
            current = current.next

    def print_client_name(self):
        current = self.head
        clients = ''
        while current:
            clients += f'C_{current.value.dpi}[label="{current.value.name}"]\n'
            current = current.next
        return clients
# if __name__ == '__main__':
#     listaBanco = LinkedList()
#     listaBanco.print()
#     listaBanco.append('Alvaro')
#     listaBanco.append('Kevin')
#     listaBanco.append('Samuel')
#     listaBanco.print()
#     last = listaBanco.get_last()
#     print(f'Se ha sacado al ultimo que entro -> {last}')

#     listaBanco.print()
