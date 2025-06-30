# create a random otp should not contain zeroes
import random as r
import math as m
def random_opt(length):
    opt=""
    while len(opt)!=length:
        digits= m.floor(r.random()*10)
        if digits!=0:
            opt=opt+str(digits)
    return opt
length_size = int(input("Enter The Length Of OPT : "))
print("The Generated OPT:",random_opt(length_size))

# guess the number within 3 chances
numbers = [2,4,6,8,10,12,14]
given_chances = 3
number = r.choice(numbers)
print("Guess a Number Between Numbers List U have Only 3 Chances..!!")#game start
#
while given_chances > 0:
    guess = int(input("\n Guess The Number : ")) 
    
    if guess==number:
        print(f"Congratulations u guessed it correct ...{number}.!!!")
        break
    else:
        given_chances = given_chances - 1
        if given_chances>0:
            print(f"Try Again There is only {given_chances} chances  left ...!!")
        else:
            print(f"Oho Sorry Your Chances Is completed ...GameOver...!!the Correct Number is :{number}")
            
        
    




