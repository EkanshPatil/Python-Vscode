import random

print("Welcome to the password generator!")

upper = ["A","B","C","D","E","F","G","H","I","J","K","L"]
lower = ["m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
symbols = ["!","@","#","%",">","^","*","~","&","$","£","?","<"]
numbers = [1,2,3,4,5,6,7,8,9,0]


raupper = random.choice(upper)
ralower = random.choice(lower)
rasymbol = random.choice(symbols)
ranumbers = random.choice(numbers)
ralower2 = random.choice(numbers)

password = "your password is: {}{}{}{}{}{}".format(ranumbers,ranumbers,rasymbol,rasymbol,ralower,ralower2)
print(password)

while True:
    change = input("type 1 to re-generate a diffrent password!")

    if change == 1:
        raupper = random.choice(upper)
        ralower = random.choice(lower)
        rasymbol = random.choice(symbols)
        ranumbers = random.choice(numbers)

    print("your password is:",raupper,rasymbol,ralower2,ranumbers,raupper,ralower,rasymbol,rasymbol,ranumbers,ranumbers,raupper,ranumbers)

