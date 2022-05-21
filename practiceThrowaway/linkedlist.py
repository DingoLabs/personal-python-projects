class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

#  a -> b -> c -> d -> None

def print_list(head):
    current = head
    while current is not None:
        print(current.val)
        current = current.next

print_list(a)


#recursive answer

# def print_list(head):
#     if head in None:
#         return
#     print(head.val)
#     print_list(head.next)





    