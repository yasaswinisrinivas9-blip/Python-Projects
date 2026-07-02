from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess,actual_answer,turns):
    if user_guess > actual_answer:
        print("Too High!")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low!")
        return turns -1
    else:
        print(f"The answer is correct! You got {actual_answer}. ")
        return turns 


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    


def game():

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")
    answer = randint(1,100)
    
    #print(f"Psss. The answer is {answer}")
    
    turns = set_difficulty()
    
    guess = 0
    
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,answer,turns)
        
        if guess == answer:
            print(f"Congratulations! You guessed the number {answer} correctly!")
            break
            
        if turns == 0:
            print("You've run out of guesses. You lose!")
            return
        
        print("Guess again.\n")
        

game()