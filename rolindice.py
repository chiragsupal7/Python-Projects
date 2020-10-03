import random

def dice(a,b):
    while True:
        print("Rolling the dices...")
        print(f"Your number is {random.randint(a,b)}")
        answer= input("Do you want to roll it again?(y/n)")
        if(answer.lower()=="n"):
            break
dice(1,6)
