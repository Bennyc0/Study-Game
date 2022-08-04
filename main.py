import random
score = 0
total = 0

num1 = random.randint(1,100)
num2 = random.randint(1,100)
num3 = random.randint(-100, -1)
num4 = random.randint(-100, -1)
num5 = random.randint(1, 15)
x = random.randint(-100, 100)

sum1 = num1*x+num2
dif1 = num2*x-num1


eigth_questions = {
    "question1": f"What is the greatest common factor of {num1} and {num2}?",
    "question2" :f"{num1}{x} + {num2} = {sum1}. What is 'x'?",
    "question3" : f"{num2}{x} - {num1} = {dif1}. What does 'x' equal to?"
}

seventh_questions = {
    "question1": f"What is {num4} minus {num3}?", 
    "question2": f"What is {num3} + {num4}?",
    "question3": f"{num4} divided by {num3}.",
    "question4": f"{num3} times {num4} equals: "
}

sixith_questions = {
    "question1": f"What is {num5} to the second power?",
    "question2": f"What is {num5} to the third power?",
    "question3": f"What is {num5} to the fourth power?"
}



def generate_question():
    pass
    
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
print("Studying for your math exams using a textbook is boring isn't it? \n")
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
    print("How did you get this line??? This isn't supposed to happen.\n")

