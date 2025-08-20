
print("welcome to my bookstore! anything that you want?")

name = input("what is your name?  ")

print("hello",name)

book = input("what book would you like?  ")

print("ok",name,"we have that book in stock!")

quantity =int( input("How many copies would you like?"))

print("ok,i will now calculate the bill for you")

cost = 6.70

amount = cost * quantity

print("your total bill is",amount,"euros")