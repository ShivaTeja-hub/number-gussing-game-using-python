import random
import math

lower=int(input("enter the lower bond number"))
upper=int(input("enter the upper bond number"))
x=random.randint(lower,upper)
print("\n \t you have only",round(math.log(upper-lower+1,2)),"number of chances only")
count=0
while count<math.log(upper-lower+1,2):
    count+=1

    gussing_number=int(input("enter the number you want to guess"))

    if(x==gussing_number):
        print("the gussed number is absolutely correct in ",count,"number of tries")
        break
    elif x>gussing_number:
        print("you gussed too small number")
    elif x<gussing_number:
        print("you gussed too large number")
    if count>math.log(upper-lower+1,2):
        print("\n the number could not be gussed so better luck next time")
