stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k,v in inventory.items():
        print(k + ": " + str(v))
        item_total = item_total + v
    print('total number of items: ' + str(item_total))

displayInventory(stuff)

myCat = {'size':'fat','color':'gray','meows':'loud'}

for x,y in myCat.items():
    print(x + y)
if 'fat' in myCat.values():
    print("yes your cat is fat")
else:
    print('no your cat is not fat')

if 'age' in myCat.keys():
    print('yes, age is a key')
else:
    print('no, age is not a key')