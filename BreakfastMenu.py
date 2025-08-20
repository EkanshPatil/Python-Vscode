print("welcome to restraunt Ekansh! ... oh sorry i forgot what day it is, can you please remind me?")

day = int(input("What day is it? ( type 1 for monday, 2 for tuesday, 3 for wednesday, 4 for thursday, 5 for friday, 6 for saturday and 7 for sunday)"))

if day == 1 :
  print("here is the breakfast menu for monday: Bacon and eggs, hash browns and orange juice")

if day == 2 :
  print("here is the breakfast menu for tuesday: omlette, beans and water")  
  
if day ==3 :
  print("here is the breakfast menu for wednesday: dosa, idli and mango lassi")
  
if day ==4 :
  print("here is the breakfast menu for thursday: medu vada, rava dosa and masala chai")
  
if day ==5 :
  print("here is the breakfast menu for friday: eggs, yougurt and milk")
  
if day ==6 :
  print("here is the breakfast menu for saturday: waffles, pancakes and coffee")
  
if day ==7 :
  print("here is the breakfast menu for sunday: avacado toast, muffins and smoothee")
  
if day >7 or day <= 0 :
  print("invalid number entered")