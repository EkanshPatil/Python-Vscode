import random
 
 
subjects = ["english","science","history","geography","maths","engineering","irish"]
hours = random.randint(6,1000)
choice = random.choice(subjects)
 
print("You will need to study",choice,"for",hours,"hours!")