a = [1,4,6,8]

for e in a:
    print(e)
total = 0
for f in a:
    total = total + f
print('total of the number are ' + str(total))

c=list(range(1,5))
print(c)

total2 = 0
for i in range(1,5):
    total2 += i
print(total)

total3=0
for i in range(1,8):
    if i % 3 == 0:
        total3+= i
print(total3)

print('hello'.center(10,'*'))
print('hello'.rjust(10,'-'))
print('hello'.ljust(10,'+'))