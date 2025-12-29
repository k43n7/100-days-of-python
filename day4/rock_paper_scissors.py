import random

rock = '''
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


## After watching tutorial

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? 0 for rock, 1 for paper, 2 for scissors: "))
if user_choice >= 0 and user_choice <= 2:
    print("\nplayer chose: ")
    print(game_images[user_choice])
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])


if user_choice >=3 or user_choice <= 0:
    print("you entered an invalid number. you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
elif computer_choice == 0 and user_choice == 0:
    print("you lose!")
elif computer_choice > user_choice:
    print("you lose!")
elif user_choice > computer_choice:
    print("you win!")
elif user_choice == computer_choice:
    print("it's a draw!")


"""

First Time Try without seeing solution!

rock_paper_scissors = [rock, paper, scissors]

player = input("please chose one of these options: '1' for rock, '2' for paper, '3' for scissors: ")
player = rock_paper_scissors[int(player) - 1]
computer = random.choice(rock_paper_scissors)
print(f"\nplayer chose {player}")
print (f"computer chose {computer}")

# player = rock
if player == rock_paper_scissors[0]:
    if computer == rock_paper_scissors[0]:
        print ("it's a tie!")
    elif computer == rock_paper_scissors[1]:
        print("computer wins!")
    elif computer == rock_paper_scissors[2]:
        print("player wins!")

# player = paper
if player == rock_paper_scissors[1]:
    if computer == rock_paper_scissors[0]:
        print ("player wins!")
    elif computer == rock_paper_scissors[1]:
        print("it's a tie!")
    elif computer == rock_paper_scissors[2]:
        print("computer wins!")

# player = scissors
if player == rock_paper_scissors[2]:
    if computer == rock_paper_scissors[0]:
        print ("computer wins!")
    elif computer == rock_paper_scissors[1]:
        print("paper wins!")
    elif computer == rock_paper_scissors[2]:
        print("its a tie!")

"""
