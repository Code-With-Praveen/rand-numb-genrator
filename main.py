
import random
from random import randint
rand_numb = random.randint(0, 100)
def guess():
    choice()
def choice():
    user_choice = input("enter your choice: ")
    user_choice = int(user_choice)
    if user_choice in range(-1,101):
        user_choice = int(user_choice)
        if user_choice != rand_numb and user_choice > rand_numb:
            print("lower your number")
            choice()
        elif user_choice != rand_numb and user_choice < rand_numb:
            print("Higher your number")
            choice()
        elif user_choice == rand_numb :
            print("Congrats You Win")
            choice()
        else:print("i Found Some error")
        choice()
    else:print("I think we are out of range")
    choice()
guess()

