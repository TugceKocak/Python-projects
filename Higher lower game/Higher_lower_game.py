from random import randint

import art
import game_data

score=0
print(art.logo)

def compare(A,B):
    if A['follower_count']>B['follower_count']:
        return 'A'
    else: return 'B'

while True:
    A=game_data.data[randint(0,len(game_data.data)-1)]
    B=game_data.data[randint(0,len(game_data.data)-1)]

    print(f"Compare A:{A['name']},{A['description']},{A['country']}")
    print(art.vs)
    print(f"Against B:{B['name']},{B['description']},{B['country']}")
    user_answer=input("Who has more followers? Type 'A' or 'B':").upper()
    answer=compare(A,B)
    if user_answer==answer:
        score+=1
        print(f"You're right! Current score: {score}")
        print("---------------------------------------------")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break

