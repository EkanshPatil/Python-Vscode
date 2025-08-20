import random

num = random.randint(1,10)

value = True
  
while value:
 print("ladies and gentleman welcome to the GUESSING GAME!,to start please pick a number from 1 - 10")

 guess = int(input("Enter a number from 1 to 10"))

 if num == guess:
   print("YOU WIN! YOUR PRIZE IS AIR!")
   value = False
   
 if num < guess:
   print("GUESS LOWER!")
 
 if num > guess:
   print("GUESS HIGHER!")
  
 else :
   print("YOU LOSE! YOUR PUNISHMENT IS TO GUESS AGAIN")

