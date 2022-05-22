import random

dic = {"Interstellar":"Cooper", "Inception":"Cobb","Ted":"Mark","Ted 2":"Bear","V for Vendetta":"V"}


random_actor = random.choice(list(dic.values()))

for i in dic:
    print(i)

guess = input(f"Which film starred {random_actor} ")

for title in dic:
    if dic[title] == random_actor:
        if guess == title:
            print("Correct!")
        else:
            print("Sorry, it is not correct")
