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

#Write your code below this line 👇
ch = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors"))
if ch <= 2 and ch >= 0:
    ls = [rock, paper, scissors]
# print(ls[ch])
    ch1 = random.choice(ls)
# print(ch)
# if ls[ch] <=2:
    if ls[ch] == ls[0] and ch1 == ls[1]:
       print(f"your choice {ls[ch]}\n")
       print(f"computer choice {ch1}\n")
       print("Computer won")
    elif ls[ch] == ls[0] and ch1 == ls[2]:
      print(f"your choice {ls[ch]}\n")
      print(f"computer choice {ch1}\n")
      print("You won")
    elif ls[ch] == ls[1] and ch1 == ls[0]:
      print(f"your choice {ls[ch]}")
      print(f"computer choice {ch1}")
      print("You won")
    elif ls[ch] == ls[1] and ch1 == ls[2]:
       print(f"your choice {ls[ch]}")
       print(f"computer choice {ch1}")
       print("Computer won")
    elif ls[ch] == ls[2] and ch1 == ls[0]:
       print(f"your choice {ls[ch]}")
       print(f"computer choice {ch1}")
       print("Computer won")
    elif ls[ch] == ls[2] and ch1 == ls[1]:
       print(f"your choice {ls[ch]}")
       print(f"computer choice {ch1}")
       print("You won")
    elif ls[ch] == ch1:
       print(f"your choice {ls[ch]}")
       print(f"computer choice {ch1}")
       print("Match is Draw")
else:
   print("please enter the correct option")