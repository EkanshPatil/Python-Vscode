print("hello, welcome to the grading bot! Please enter your grade (1-100) for the following subjects")

#math
math = int(input("what is your grade in math?"))
mathgrade = 0

if math >= 90 :
  mathgrade = "A"

elif math < 90 and math>= 75 : 
 mathgrade = "B"

elif math <75 and math>=60 :
  mathgrade = "C"

elif math <60 and math>=45 :
   mathgrade ="D"
   
elif math <45 :
  mathgrade = "FAIL"
  
print("your total in math is:",math,"/100 your percentage is:",math,"% and your grade is:",mathgrade)  

#english
english = int(input("what is your grade in english?"))
englishgrade = 0

if english >= 90 :
  englishgrade = "A"

elif english < 90 and english>= 75 : 
 englishgrade = "B"

elif english <75 and english>=60 :
  englishgrade = "C"

elif english <60 and english>=45 :
   englishgrade ="D"
   
elif math <45 :
  englishgrade = "FAIL"
  
print("your total in english is:",english,"/100 your percentage is:",english,"% and your grade is:",englishgrade)

#science
science = int(input("what is your grade in science?"))
sciencegrade = 0

if science >= 90 :
  sciencegrade = "A"

elif science < 90 and science>= 75 : 
 sciencegrade = "B"

elif science <75 and science>=60 :
  sciencegrade = "C"

elif science <60 and science>=45 :
   sciencegrade ="D"
   
elif science <45 :
  sciencegrade = "FAIL"
  
print("your total in science is:",science,"/100 your percentage is:",science,"% and your grade is:",sciencegrade)

#history
history = int(input("what is your grade in history?"))
historygrade = 0

if history >= 90 :
  historygrade = "A"

elif history < 90 and history>= 75 : 
 historygrade = "B"

elif history <75 and history>=60 :
  historygrade = "C"

elif history <60 and history>=45 :
   historygrade ="D"
   
elif history <45 :
  historygrade = "FAIL"
  
print("your total in history is:",history,"/100 your percentage is:",history,"% and your grade is:",historygrade)

#geography
geography = int(input("what is your grade in geography?"))
geographygrade = 0

if geography >= 90 :
  geographygrade = "A"

elif geography < 90 and geography>= 75 : 
 geographygrade = "B"

elif geography <75 and geography>=60 :
  historygrade = "C"

elif geography <60 and geography>=45 :
   geographygrade ="D"
   
elif geography <45 :
  geographygrade = "FAIL"
  
print("your total in geography is:",geography,"/100 your percentage is:",geography,"% and your grade is:",geographygrade)
