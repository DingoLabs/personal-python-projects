import json
from sys import exit
import time
with open('birthdays.txt') as f:
    birthday = f.read()
birthdays = json.loads(birthday)
print(type(birthdays))

def Equit():
    print('would you like to save the changes? (y/n)')
    answer = input()
    if answer == "y":
        with open('birthdays.txt','w') as outfile:
            json.dump(birthdays, outfile)
            print('saving.')
            time.sleep(0.5)
            print('saving..')
            time.sleep(0.5)
            print('saving...')
            time.sleep(0.5)
            print('database updated. exiting.')
            exit()
    elif answer == "n":
        print('k bye now.')
        exit()
    else:
        Equit()


while True:
    print('\nEnter a name: ("quit" to exit, "list" to show names, "printAll" to show all)')
    name = input()
    if name == 'quit':
        Equit()
    elif name == 'list':
        print('\n *** Current names in database *** \n')
        for current_names in birthdays:
            print(current_names)
    elif name == 'printAll':
        for name in birthdays:
            print('\n' + name + ' | ' + birthdays[name])
    
    else:
        print('\n')
        if name in birthdays:
            print(name + "'s birthday is " + birthdays[name])
        else:
            print('I do not have a birthdate for ' + name)
            print('Please enter their birthdate')
            print('(date month year)')
            bday = input()
            birthdays[name] = bday
            print('Birthday database updated')
