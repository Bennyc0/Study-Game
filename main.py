#My name is Kira Yoshikage
#Benny
#testing
#indira
#nour
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
        print("The answer was" + correct_ans)
    