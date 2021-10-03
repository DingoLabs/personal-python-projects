def Collatz(number):
    while True:
        number1 = number % 2
        if number1 == 0:
            number = number // 2
            print(number)
        elif number1 == 1:
            number = 3 * number + 1
            print(number)
        else number == 1:
            break


print('pick a number:')
answer = int(input())
Collatz(answer)
