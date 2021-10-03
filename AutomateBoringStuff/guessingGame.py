import random
secretNumber = random.randint(1,20)
print('guess my number')
i = 7
while i != 0:
    print ('you have ' + str(i) + ' left')
    i = i - 1
    print('guess?')
    guess = int(input())
    if guess < secretNumber:
        print('too low')
    elif guess > secretNumber:
        print('too high')
    else:
        break

if guess == secretNumber:
    print('you got it!')
else:
    print('incorrect. the number i was thinking about was ' + str(secretNumber))
