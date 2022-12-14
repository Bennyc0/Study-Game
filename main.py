import random
import math
score = 0
total = 0
correct_ans = 0

num1 = random.randint(1,101)
num2 = random.randint(1,101)
num3 = random.randint(-100, -1)
num4 = random.randint(-100, -1)
num5 = random.randint(1, 15)
x = random.randint(1,100)


sum1 = num1*x+num2
dif1 = num2*x-num1
 
eigth_questions = {
    "question1": f"What is the greatest common factor of {num1} and {num2}?",
    "question2": f"{num1}x + {num2} = {sum1}. What is 'x'?",
    "question3": f"{num2}x - {num1} = {dif1}. What does 'x' equal to?"
}

seventh_questions = {
    "question1": f"What is {num4} minus {num3}?", 
    "question2": f"What is {num3} + {num4}?",
    "question3": f"{num4} divided by {num3}.",
    "question4": f"{num3} times {num4} equals: "
}

sixith_questions = {
    "question1": f"What is {num5} to the second power?",
    "question2": f"{num5} to the third power is: ",
    "question3": f"What is {num5} to the fourth power?"
}



def generate_question():
    if user_grade == "6":
        question = random.choice (list(sixith_questions.values()))
        return question
    elif user_grade == "7":
        question = random.choice (list(seventh_questions.values()))
        return question
    elif user_grade == "8":
        question = random.choice (list(eigth_questions.values()))
        return question

def eighth(question):
    global x
    if question == eigth_questions["question1"]:
        return math.gcd(num1, num2) 
    elif question == eigth_questions["question2"]:
        return x
    elif question == eigth_questions["question3"]:
        return x

def seventh(question):
    if question == seventh_questions["question1"]:
        return num4 - num3  
    elif question == seventh_questions["question2"]:
        return num3 + num4
    elif question == seventh_questions["question3"]:
        return num4 / num3
    elif question == seventh_questions["question4"]:
        return num3*num4

def sixith(question):
    if question == sixith_questions["question1"]:
        return num5**2   
    elif question == sixith_questions["question2"]:
        return num5**3
    elif question == sixith_questions["question3"]:
        return num5**4

ans_list = []

def generate_ans(question):
    global ans_list
    global correct_ans
    #question = generate_question()

    if user_grade == "6":
        correct_ans = sixith(question)
    elif user_grade == "7":
        correct_ans = seventh(question)
    elif user_grade == "8":
        correct_ans = eighth(question)

    extra_num1 = random.randint(-10, -1)
    extra_num2 = random.randint(1, 10)
    extra_num3 = random.randint(1, 10)

    ans1 = correct_ans+extra_num1+1
    ans2 = correct_ans
    ans3 = correct_ans+extra_num2 +1
    ans4 = correct_ans+extra_num3+1

    ans_list = [ans1, ans2, ans3, ans4]
    random.shuffle(ans_list)

    print(f"Option 1: {ans_list[0]} \nOption 2: {ans_list[1]} \nOption 3: {ans_list[2]} \nOption 4: {ans_list[3]}")



def check_ans():
    global score
    global total
    global correct_ans
    global ans_list
    active = True

    user_answer = ""
    
    while active:
        user_answer = input("What option do you choose?(1, 2, 3, or 4)>> ")
        print("\n")

        if user_answer.isdigit() and int(user_answer) <= 4 and int(user_answer) > 0:
            index = int(user_answer)-1
            user_answer = ans_list[index]
            active = False
        else:
            print("Please type 1, 2, 3, or 4. \n")

    if user_answer == correct_ans:
        score += 1
        total += 1
        print("You got the right answer! \n")
    else:
        print(f"The answer was {correct_ans}. \n")
        total += 1
    


# ----------Game Start----------

print("Hello! \n")
print("Studying for your math exams using a textbook is boring isn't it? \n")
print("Let's play a minigame! ???? \n")

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


while total < 10:
    num1 = random.randint(1,101)
    num2 = random.randint(1,101)
    num3 = random.randint(-100, -1)
    num4 = random.randint(-100, -1)
    num5 = random.randint(1, 15)
    x = random.randint(1,100)

    sum1 = num1*x+num2
    dif1 = num2*x-num1

    eigth_questions = {
        "question1": f"What is the greatest common factor of {num1} and {num2}?",
        "question2": f"{num1}x + {num2} = {sum1}. What is 'x'?",
        "question3": f"{num2}x - {num1} = {dif1}. What does 'x' equal to?"
    }

    seventh_questions = {
        "question1": f"What is {num4} minus {num3}?", 
        "question2": f"What is {num3} + {num4}?",
        "question3": f"{num4} divided by {num3}.",
        "question4": f"{num3} times {num4} equals: "
    }

    sixith_questions = {
        "question1": f"What is {num5} to the second power?",
        "question2": f"{num5} to the third power is: ",
        "question3": f"What is {num5} to the fourth power?"
    }

    question = generate_question()
    print(question)
    generate_ans(question)
    check_ans()


if total == 10 and score >= 7:
    print(f"Congratulations! ???????????? \nYou've completed the minigame for {user_grade}th grade! \nSince you scored {score} out of 10, you will be fine on any topic on exams that was covered in this minigame! \n") 
elif total == 10 and score < 7:
    print(f"Sorry, but it seems that you need to study a bit more. You only got {score} out of 10 questions correct. \nSuggested actions would be to try again and try to get your grade to where you are satisfied. Good Luck! \n")
else:
    print("Please finish the 10 questions first.(Also this isn't supposed to happen)")