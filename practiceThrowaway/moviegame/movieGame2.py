import random
import time


"""  
Goal
Movie Actor Challange
5 movies and 5 actors
match the actor to the movie
"""





def game():

    movies = ["terminator","mission impossible","taken","speed","rocky","taxi driver","drive","indiana jones: the lost ark","zorro","iron man",]
    actors = ["arnold schwarzenegger","tom cruise","liam neeson","keanu reeves","sylvester stallone","robert de niro","ryan gosling","harrison ford","antonio banderas","robert downey jr"]

    print_movie_list = """
    1) terminator               6) taxi driver
    2) mission impossible       7) drive
    3) taken                    8) indiana jones: the lost ark
    4) speed                    9) zorro
    5) rambo                    10) iron man
    """

    print("""
    **************************************************
    *        MOVIE ACTOR MATCHING CHALLENGE          *
    *  can you match the actor to the correct movie? *
    *         5 movies, 5 actors. have fun           *
    **************************************************

    """)

    player_score = 0
    answer = 0
    movie_num = [1,2,3,4,5,6,7,8,9,10]
    random.shuffle(movie_num)
    question_count = 1

    for i in movie_num:
        print("question number " + str(question_count))
        print(print_movie_list)
        actor_choice = actors[i -1]
    
        print("what movie is " + actor_choice + " in?")

        answer = input("what is your answer: ")
        answer = int(answer)
        if answer == i:
            print("\nCORRECT!!!")
            player_score += 1
        else:
            print('\nsorry, that is incorrect')
        print('current score: ' + str(player_score))
        print("\n- - - - - - - - - - - - - - - - - - - - - - \n")
        question_count += 1
        time.sleep(2)

    return player_score



def final_score(score):
    print("your final score is " + str(score) + ' / 10\n')
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
            print(" you even try???")
    

def play_again():
    print('\ndo you want to play again?')
    answer = input('y/n: ')
    
    if answer == "n":
        quit()
    elif answer == "y":
        game_loop()
    else:
        print('thats not an option...')
        play_again()
        
def game_loop():
    player_score = game()
    final_score(player_score)
    play_again()

game_loop()
