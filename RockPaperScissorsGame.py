import random

print("welcome to the rock paper scissors game! you will need to play 10 rounds of rock paper scissors against a bot")

tie = 0
win = 0
loss = 0

for i in range(10):
 bot = random.randint(1,3)
 
 guess = int(input("Enter the number 1 for rock, 2 for paper and 3 for scissors "))
 
 if bot == guess:
     tie = tie + 1
     print("tie!")

 if bot == 1 and guess == 2:
     win = win + 1
     print("round won!")  

 if bot == 1 and guess == 3:
     loss = loss + 1
     print("round lost!") 

 if bot == 2 and guess == 1:
     loss == loss + 1
     print("round lost!")

 if bot == 2 and guess == 3:
     win = win + 1
     print("round won!")

 if bot == 3 and guess == 1:
     win = win + 1
     print("round won!")
 
 if bot == 3 and guess == 2:
     loss = loss + 1
     print("round lost!")
print("you have won",win,"rounds, lost",loss,"rounds and tied",tie,"rounds")
     