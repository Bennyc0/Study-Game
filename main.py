#My name is Kira Yoshikage
#Benny
#testing
#indira
#nour

def generate_ans(ans):
    
def add():
    ans = num1 + num2
    return 

def subtract():
    ans = num1 - num2
    return 

def divide():
    ans = num1 // num2
    return 

def multiply():
    ans = num1*num2
    return 
import random
score = 0
total = 0


answers_dict = {
    "1": ans1,
    "2": ans2,
    "3": ans3,
    "4": ans4
}


def check_ans():
    active = True
    
    while active:
        user_answer = input("What option do you choose?(1, 2, 3, or 4)>> ")
        print("\n")

        if user_answer.isdigit() and int(user_answer) <= 4:
            for answer in answers_dict
            if answer == user_answer:
                active = False
                user_answer = answers_dict.get(answer)
        else:
            print("Please type 1, 2, 3, or 4. \n")


    if user_answer == correct_ans:
        score += 1
        total += 1
        print("You got the right answer!")
    else:
        print(f"The answer was {correct_ans}.")
    


# ----------Game Start----------

print("Hello! \n")
print("Studying Math using a textbook is boring isn't it? \n")
print("Let's play a minigame! 😃 \n")

active = True
while active:
    checking_grade = True
    user_grade = input("What grade do you want to play as?(6, 7, or 8)>> ")
    print("\n")

    if user_grade.isdigit():
        if int(user_grade) >= 6 and int(user_grade) <= 8:
            while checking_grade:
                reply = input(f"Is your grade {user_grade}th grade?(Yes or No)>> ").lower()
                print("\n")

                if reply == "yes":
                    print(f"Ok! Your grade is {user_grade}th grade. \n")
                    active = False
                    checking_grade = False
                elif reply == "no":
                    checking_grade = False
                else:
                    print("Please type: Yes or No \n")
        
        else:
            print("Please type in a number from 6-8 as your grade. \n")


if user_grade == "6":
    print("The math topic this minigame will cover is: Exponents(Powers of whole numbers). \n")
elif user_grade == "7":
    print("The math topic this minigame will cover is: Operations using negative integers. \n")
elif user_grade == "8":
    print("The math topic this minigame will cover is: Numbers and operations, and solving equations with one unknown variable. \n")
else:
    print("How did you get this line??? \n")

