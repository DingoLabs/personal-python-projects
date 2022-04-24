sentence = "the quick fox dog jumps over the lazy dog"

words = sentence.split()
newlist = []

for word in words:
    if word != "the":
        newlist.append(word)
print(newlist)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

new_num_List = []
for number in numbers:
    if number > 0:
        new_num_List.append(int(number))
print(new_num_List)        