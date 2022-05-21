# stack
# ordered collection of items where addition and removal happens at the same end
# ends referred as top or base

#LIFO - last in first out

# example - a stack of books, a stack of cafe trays

# good for reversal of items

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


s = Stack()
print(s.is_empty())
print(s.size())
s.push(1)
s.push(45)
s.push("philip")
s.push("dog")
print(s.peek())
print(s.size())
print(s.pop())

def parChecker(symbol_string):
    s2 = Stack()
    for symbol in symbol_string:
        if symbol == "(":
            s2.push(symbol)
        else:
            if s2.is_empty():
                return False
            else:
                s2.pop()
    return s2.is_empty()

print(parChecker("((()))"))
print(parChecker("((())"))
print(parChecker(")))"))


def balanceCheck(symbol_string):
    s3 = Stack()
    for symbol in symbol_string:
        print(symbol)
        if symbol in "([{":
            s3.push(symbol)
        else:
            if s3.is_empty():
                return False
            else:
                if not matches(s3.pop(), symbol):
                    return False

    return s3.is_empty()




def matches(sym_l, sym_r):
    all_l = "([{"
    all_r = ")]}"
    return all_l.index(sym_l) == all_r.index(sym_r)

#print(balanceCheck('[][]'))
print(balanceCheck('[{()()}]'))
