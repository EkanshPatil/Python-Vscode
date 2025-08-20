print("Welcome to the leap year detector! please enter the year")

year = int(input("what year is it?"))

if year%4 == 0:
  print("this year is a leap year!")

elif year <=0 :
  print("invalid year entered")
  
else :
  print("this year is not a leap year")