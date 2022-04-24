def printPicnic(items,lW,rW):
    print('Picnic item'.center(lW + rW, '-'))
    for k,v in items.items():
        print(k.ljust(lW, '.') + str(v).rjust(rW))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)


tableData = [['apples', 'oranges', 'cherries', 'banana'],              
['Alice', 'Bob', 'Carol', 'David'],              
['dogs', 'cats', 'moose', 'goose']]


print('test'.center(10, '-'))
for x in tableData:
    for y in x:
        print(y.rjust(10, '.') + ' -> ' + str(len(y)))
