passwordFile = open('secretfile.txt')
password = passwordFile.read()
print(password)
print('enter password')
myPass = input()
print(myPass)
if myPass == password:
  print('correct!')
else:
  print('WRONG')
