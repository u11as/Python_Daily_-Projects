import random


rock =  '''

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

game_name = rock, paper, scissors

user_choice = int(input("what do you chose, type 0 for rock, 1 for paper, 2 for scissors .\n"))

if user_choice >= 0 and user_choice<= 2:
    print(game_name[user_choice])

computer_choice = random.randint(0, 2)
print("Computer choice")
print(game_name[computer_choice])

if user_choice >=3 or user_choice < 0:
    print("invalid numbers")

elif user_choice == 0 and computer_choice == 2:
    print("you have won the game")

elif computer_choice ==0 and user_choice == 2:
    print("you have lost the game ")

elif user_choice == 1 and computer_choice == 2:
    print("you have lost the game ")

elif user_choice == 2 and computer_choice == 1:
    print("you have won the game")

else:
    print("the game has drawn, means its equal")
