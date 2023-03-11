# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "S":
  cost = 15
  if add_pepperoni == "Y":
    cost_pep = cost + 2
  else:
    cost_pep = cost
  if extra_cheese == "Y":
    cost_cheese = cost_pep + 1
  else:
    cost_cheese = cost_pep
  print(f"Your final bill is {cost_cheese}")
elif size == "M":
  cost = 20
  if add_pepperoni == "Y":
    cost_pep = cost + 3
  else:
    cost_pep = cost
  if extra_cheese == "Y":
    cost_cheese = cost_pep + 1
  else:
    cost_cheese = cost_pep
  print(f"Your final bill is {cost_cheese}")
elif size == "L":
  cost = 25
  if add_pepperoni == "Y":
    cost_pep = cost + 3
  else:
    cost_pep = cost
  if extra_cheese == "Y":
    cost_cheese = cost_pep + 1
  else:
    cost_cheese = cost_pep
  print(f"Your final bill is {cost_cheese}")

