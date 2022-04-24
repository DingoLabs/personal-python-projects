filename = "./names.txt"
filename2 = "./fav_foods.txt"

foods = [
    'pizza',
    'sub',
    'fries',
    'pop'
]

with open(filename) as f:
    line = f.readline()
    print(line)

#print(f.readline())



with open(filename2, 'w') as f:
    for food in foods:
        f.write(food + '\n')

print(foods[0])