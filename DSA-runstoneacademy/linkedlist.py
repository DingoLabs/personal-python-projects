# a node of a linked list

class Node:
    
    def __init__(self,node_data):
        self.data = node_data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, node_data):
        self.data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        return self.next

    def set_next(self, node_next):
        self.next = node_next

    next = property(get_next, set_next)

    def __str__(self):
        return str(self.data)


temp = Node(93)
temp.data

