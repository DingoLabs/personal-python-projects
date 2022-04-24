import pprint

# name = input("what is your name: ")
# print ("nice to meet you", name)
# print ("your name has " + str(len(name)) + " letters in it.")
# age = input("what is your age: ")
# year_born = 2022 - int(age)
# print("you were born in the year" + str(year_born))

name = "Zophie a car"
print(name)
new_name = name[0:7] + 'the' + name[8:12]
print(new_name)

myCat = {'size': 'fat', 'color':'gray' ,'disposition': 'loud'}
print("my cat has " + (myCat['color']) + " fur.") 

bdays = {'alice': 'april 1' , 'aubrey': 'feb 1', 'angela': 'march 1'}

while True:
    name = input('enter a name: (blank to quit) ')
    if name == '':
        break

    if name in bdays:
        print(bdays[name] + ' is the bday of ' + name)
    else:
        print('i dont know that persons bday.')


spam = {'color' : 'red' , 'age' : '35' }
for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)
for i in spam.items():
    print(i)

picnicItems = {'apples': 5, 'cups':'2'}
print("I am bring " + str(picnicItems.get('cups', 0)) + ' cups')

message = 'it was a bzzzzzzright cold day in april, and the clocks were striking thirtee.'
counter = {}

for character in message:
    counter.setdefault(character, 0)
    counter[character] = counter[character] + 1

pprint.pprint(counter)

theBoard = {'top-L': '0', 'top-M':'0', 'top-R':'0','mid-L': '0', 'mid-M':'0', 'mid-R':'0','low-L': '0', 'low-M':'0', 'low-R':'0',}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] + '|')
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'] + '|')
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'] + '|')
printBoard(theBoard)