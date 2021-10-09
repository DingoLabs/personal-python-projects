import random
#import word_list.txt

f = open('new_word_list.csv','r')
for i in f:
    print(random.choice(i))

