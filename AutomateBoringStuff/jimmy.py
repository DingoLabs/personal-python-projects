while True:
    print('pick a number: ')
    num = input()
    num = int(num)
    if num == 0:
        print('no not that number.')

    for i in range(int(num)):
        print('My name is ')
        print('Jimmy ' + str(num))
        num = int(num) - 1
