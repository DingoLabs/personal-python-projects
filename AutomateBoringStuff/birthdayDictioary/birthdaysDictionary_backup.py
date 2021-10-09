birthdays = {'angela': '29 jan 1986','ralph': '28 feb 1986','dave': '7 july 1986','philip': '13 sept 1986'}

while True:
    print('\nEnter a name: (leave blank to quit, "list" to show names, "printAll" to show all)')
    name = input()
    if name == '':
        print('k bye now')
        break
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

