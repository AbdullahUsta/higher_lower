from art import logo, vs
import random
from game_data import data
print(logo)

score = 0
wrong_entered = False

while not wrong_entered:

    choice1, choice2 = random.sample(data, 2)


    answer = input(
        f"Who has more followers? \nA: {choice1['name']} {vs} \nB: {choice2['name']} \nEnter your answer (a or b): ").lower()


    if answer == "a":
        if choice1['follower_count'] > choice2['follower_count']:
            print("Correct! Next one.")
            score += 1
            print(f"Your score is now {score}.")
        else:
            print("False, you lose.")
            wrong_entered = True

    elif answer == "b":
        if choice2['follower_count'] > choice1['follower_count']:
            print("Correct! Next one.")
            score += 1
            print(f"Your score is now {score}.")
        else:
            print("False, you lose.")
            wrong_entered = True

    else:
        print("Please enter a valid option (a or b).")

print(f"Game over! Your final score is {score}.")