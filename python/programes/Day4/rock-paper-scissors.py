import random

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

computer_choose = random.randint(0, 2)

if user_choose > 2 or user_choose < 0:
    print("Wrong number, You lose!")
else:
    choose_image = [rock, paper, scissors]
    print(choose_image[user_choose])
    print("Computer choose:")
    print(choose_image[computer_choose])

    if user_choose == 2 and computer_choose == 0:
        print("You lose!")
    elif user_choose == 0 and computer_choose == 2:
        print("You win!")
    elif user_choose == computer_choose:
        print("Draw!")
    elif user_choose > computer_choose:
        print("You win!")
    else:
        print("You lose!")
