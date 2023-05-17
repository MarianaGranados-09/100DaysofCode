#heads or tails code
import random #random module

HorT = random.randint(1,2)
#print(HorT)

if(HorT == 1):
    print("Tails!")
else:
    print("Heads!")

  
########################################################3
import random #random module

##random fruit generator
fruits = ["apple","grape","watermelon", "melon", "mango"]
length = len(fruits)
fruitChoice = random.randint(1,length-1)
print(f"Your fruit is: {fruits[fruitChoice]}")
