filename = './names.txt'
f = open(filename)
print(f.closed)
print(f.name)
print(f.mode)
f.close()
print(f.closed)