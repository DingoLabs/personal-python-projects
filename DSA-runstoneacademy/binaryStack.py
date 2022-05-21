
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # check if the stack is empty
        return not bool(self.items)

    def push(self, item):
        # add an item to the stack
        self.items.append(item)

    def pop(self):
        # return an item from the stack
        return self.items.pop()
    
    def peek(self):
        # get valuse of the top item in the stack
        return self.items[-1]

    def size(self):
        # get number of items in stack
        return len(self.items)


def divide_by_2(decimal_num):
    rem_stack = Stack()

    while decimal_num > 0:
        rem = decimal_num % 2
        rem_stack.push(rem)
        decimal_num = decimal_num // 2

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())

    return bin_string

print(divide_by_2(42))
print(divide_by_2(64))