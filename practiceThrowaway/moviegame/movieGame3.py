import random
import time

""" Movie Actor Challange
    5 movies and 5 actors
    match the actor to the movie
"""


def print_movielist(movies_actors):
    """
    1) terminator               6) taxi driver
    2) mission impossible       7) drive
    3) taken                    8) indiana jones: the lost ark
    4) speed                    9) zorro
    5) rambo                    10) iron man
    """
    
    for index in range(0, len(movies_actors), 2):
        movie_actor1 = str(index + 1) + ") " + movies_actors[index][0]
        movie_actor2 = str(index + 2) + ") " + movies_actors[index + 1][0] 
        print(movie_actor1.ljust(20), end='')
        print(movie_actor2.ljust(20), end='')
        print()

def game(movies_actors):


    print(
        """
    **************************************************
    *        MOVIE ACTOR MATCHING CHALLENGE          *
    *  can you match the actor to the correct movie? *
    *         5 movies, 5 actors. have fun           *
    **************************************************

    """
    )

    player_score = 0
    answer = 0
    movie_num = list(range(1, len(movies_actors) + 1))
    random.shuffle(movie_num)
    question_count = 1

    for i in movie_num:
        print("question number " + str(question_count))
        print_movielist(movies_actors)
        actor_choice = movies_actors[i - 1][1]

        print("what movie is " + actor_choice + " in?")

        
        while True:
            answer = input("what is your answer: ")
            try:
                answer = int(answer)
                break
            except ValueError:
                print(f"Invalid input, received: {answer}, expected a number")
                continue

        answer = int(answer)
        if answer == i:
            print("\nCORRECT!!!")
            player_score += 1
        else:
            print("\nsorry, that is incorrect")
        print("current score: " + str(player_score))
        print("\n- - - - - - - - - - - - - - - - - - - - - - \n")
        question_count += 1
        time.sleep(2)

    return player_score


def final_score(score):
    print("your final score is " + str(score) + " / 10\n")
    match score:
        case 10:
            print("perfect score! you really know your movies")
        case 9 | 8 | 7:
            print("you know your movies!")
        case 4 | 5 | 6:
            print("not too bad, could do better...")
        case 1 | 2 | 3:
            print("you need to watch more movies...")
        case 0:
            print("are you even trying???")


def play_again():
    print("\ndo you want to play again?")
    answer = input("y/n: ")

    if answer == "n":
        quit()
    elif answer == "y":
        game_loop()
    else:
        print("thats not an option...")
        play_again()


def game_loop():
    movies_actors = [
        ["terminator", "arnold schwarznegger"],
        ["mission impossible", "tom cruise"],
        ["taken", "liam neeson"],
        ["speed", "keanu reeves"],
        ["rocky", "sylvester stallone"],
        ["taxi driver", "robert de niro"],
        ["drive", "ryan gosling"],
        ["indiana jones: the lost ark", "harrison ford"],
        ["zorro", "antonio banderas"],
        ["iron man", "robert downey jr"],
    ]
    player_score = game(movies_actors)
    final_score(player_score)
    play_again()


game_loop()