names = [
    "alice",
    "aubrey",
    "angela"
]

names2 = [
    "alice\n",
    "aubrey\n",
    "angela\n"
]
numbers = [1,2,3]

filename = './names2.txt'
f = open(filename, 'w')

f.write('catdog\n')
f.write('courage\n')
f.write('ed\n')

for name in names:
    f.write(name + '\n')


f.writelines(names2)

f.write(str(1) + "\n")
f.write(str(numbers))


f.close()