# deque 

# double ended queue add items or remove items from both sides

#      rear                                     front
#      -----------------------------------------------
# add to rear                                 add to front
# remove rear                                 remove front
#      -----------------------------------------------
#

class Deque:

    def __init__(self):
        self.items = []


    def add_front(self, num):
        self.items.append(num)

    def add_back(self, num):
        self.items.insert(0, num)

    def remove_front(self):
        return self.items.pop()

    def remove_back(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return not bool(self.items)
    

def palindrome_checker(a_string):
    d = Deque()

    for char in a_string:
        d.add_back(char)
    
    while d.size() > 1:
        first = d.remove_front()
        last = d.remove_back()

        if first != last:
            return False
        
    return True

print(palindrome_checker('asklfjklsadfjsakl'))
print(palindrome_checker("radar"))

