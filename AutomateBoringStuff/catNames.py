print('CAT LIST MAKER!\ntype stop to end\ntype list to print list')

catName = []

while True:
    print('\nenter a cat name for cat ' + str(len(catName) + 1))
    name = input()
    if name == 'list':
        print('')
        print('----- cat names -----')
        for name in catName:
            print(name)
        print('')
    elif name == 'stop':
        break
    else:
        catName = catName + [name]

print('well... that was fun.')
