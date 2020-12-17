import pygame
import random

pygame.init()

input_number = -1
correct_number = random.randint(0, 1000)
number_of_tries = 0

while input_number != correct_number:
    number_of_tries += 1
    user_input = input("Guess the number from 0 to 1000:\n   > ")
    try:
        input_number = int(user_input)
    except:
        print("That is not a number dumbass try again lolololxdxdddxd")
        continue
    
    if input_number == correct_number:
        print("Congratulations you guessed the right number in " + str(number_of_tries) + " tries. It was " + str(correct_number)) + "."
    elif abs(input_number - correct_number) < 8:
        print("Uhhhhh veeery vaaaaaaaarm right now")
    elif abs(input_number - correct_number) < 50:
        if input_number > correct_number:
            print("Ehh its a bit lower")
        if input_number < correct_number:
            print("Its higher than " + str(input_number) + ", but lower than " + str(correct_number + random.randint(0, 30)))
    elif abs(input_number - correct_number) < 100:
        if input_number > correct_number:
            print("Lower!")
        if input_number < correct_number:
            print("Higher!")
    elif abs(input_number - correct_number) < 300:
        if input_number > correct_number:
            print("Bruh youre bad at guessing. Its a lot lower.")
        if input_number < correct_number:
            print("The correct number is higher. A lot higher.")
    else:
        print("Bruh moment.")