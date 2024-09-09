import random

print("Welcome to Guess the number!")
print("I'm thinking of a number between 1 and 100!")

number=random.choice(range(1,100))
difficulty=input("Choose a difficulty. Type 'easy' or 'hard':")

attempt=0
if difficulty=='easy': attempt=10
elif difficulty=='hard': attempt=5
print(f"You have {attempt} attempts remaining to guess the number.")

guess=-1
while guess!=number:
    guess = int(input("Make the guess:"))
    if guess>number:
        print("Too high!\n Guess again.")
        attempt-=1
    elif guess<number:
        print("Too low!\n Guess again.")
        attempt-=1
    else:
        print(f"You got it! The answer was {number}.")
        break
    print(f"You have {attempt} attempts remaining to guess the number.")
    if attempt==0:
        print("You run out of guesses, you lose!")
        break
