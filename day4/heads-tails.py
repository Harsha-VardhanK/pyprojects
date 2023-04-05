import random

ht = random.randint(0,1)
if ht == 0:
    print("Heads")
else:
    print("Tails")
    
a = ['Heads', 'Tails']
print(random.choice(a))
