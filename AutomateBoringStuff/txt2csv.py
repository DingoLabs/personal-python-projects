f = open('word_list.txt', 'r')
line = f.readlines()
new_line = []
f2 = open('new_word_list.txt', 'w')
for i in line:
    new_line = (i[:-1]) + ','
    f2.write(new_line)
f2.close()
