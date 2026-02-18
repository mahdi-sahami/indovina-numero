from models import Game
from choices import UserInputChoices

game=Game()

print("Welcome to my game!")
print("in this game, first you have to choose a number from 0 to 100")
print("then, I start to guess your number, at each time, you just need to tell me whether it's your number, or your number is higher or lower")
print(f"if I guessed your number, enter: {UserInputChoices.user_number_is_guessed.value}")
print(f"if your number is higher than my guess, enter: {UserInputChoices.user_number_is_higher.value}")
print(f"if your's lower, then enter: {UserInputChoices.user_number_is_lower.value}")
while True:
    print(f"is your number: {game.guessed_number}")
    user_input:str=input("Enter your choice: ")
    try:
        user_input = UserInputChoices(user_input)
    except Exception as e:
        print(f"LOG: e: {e}")
        print(f"your input is wrong, chose among {UserInputChoices.get_all_visible_choices()}")
        continue

    game.apply_user_input(user_input=user_input)

    if game.is_game_finished:
        print("man bordam!")
        break