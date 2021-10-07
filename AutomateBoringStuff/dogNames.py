dogNames = []
while True:
    print('\nWhat are your dog names?')
    name = input()
    if name == 'list':
        print('\n-----Dog Names-----\n')
        for n in dogNames:
            print(n)
    elif name == 'stop':
        print('k bye!')
        break
    else:
        dogNames = dogNames + [name]


