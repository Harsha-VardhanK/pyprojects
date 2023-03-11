

#Tip Calculator code below:
print("Welcome to the tip calculator")
tb = float(input("What was the total bill? $"))
tip = 1 + (float(int(input("What percentage tip would you like to give 8,10,12,15? "))) / 100)
# per = tip / 100
p = int(input("How many people to split the bill? "))
sp = (tb * tip) / p 
# ep = 
print(f" Each person should pay : ${round(sp,2)} ")

