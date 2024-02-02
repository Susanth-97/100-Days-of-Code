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

choice = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(choice[user_choice])

a= random.randint(0,2)
b = choice[a]
print(f"Computer Choice: {b}")


if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and a == 2:
  print("You win!")
elif a == 0 and user_choice == 2:
  print("You lose")
elif a > user_choice:
  print("You lose")
elif user_choice > a:
  print("You win!")
elif a == user_choice:
  print("It's a draw")
