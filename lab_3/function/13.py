#Guess the Number Game
import random

def guess_the_number():
    name = input("Привет! Как тебя зовут?\n")
    print(f"Ну что, {name}, я загадываю число от 1 до 20.")
    
    number = random.randint(1, 20)
    guesses = 0
    
    while True:
        guess = int(input("Угадай число.\n"))
        guesses += 1
        
        if guess < number:
            print("Твое число слишком маленькое.")
        elif guess > number:
            print("Твое число слишком большое.")
        else:
            print(f"Отлично, {name}! Ты угадал число за {guesses} попыток!")
            break
