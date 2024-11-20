import random


def rps_game():
    print("******Welcome to RPS Game ****")
    print()

    print('''~~Winning Rules~~
    Rock vs Paper =Paper wins
    Paper vs Scissor=Scisssor wins
    Scissor vs Rock=Rock wins
    ''')
    print()

    User_score=0
    Computer_Score=0
    tie=0


    for a in range(0,5):
        print()
        print('''Choices are:
        1.paper
        2.Scissor
        3.Rock
        ''')
        Choice=int(input("Enter Your Choice(1-3):"))

        while Choice>3 or Choice<1:
            Choice=int(input("Enter valid input "))

        if Choice==1:
            User_choice="Paper"
        elif Choice==2:
                User_choice="Scissor"
        elif Choice==3:
                User_choice="Rock"


        Computer=random.randint(1,3)
        if Computer==1:
           Computer_choice="Paper"
        elif Computer==2:
            Computer_choice="Scissor"
        elif Computer==3:
            Computer_choice="Rock"

        print("Your choices are:",User_choice)
        print("Computer choices are:",Computer_choice)

        if (User_choice=="Paper" and Computer_choice=="Rock") or( User_choice=="Rock" and Computer_choice=="Paper"):
            print("Paper wins")
            final="Paper"
        elif(User_choice=="Scissor" and Computer_choice=="Paper")or(User_choice=="Paper" and Computer_choice=="Scissor"):
            print("Scissor wins")
            final="Scissor"
        elif(User_choice=="Rock" and Computer_choice=="Scissor")or(User_choice=="Scissor" and Computer_choice=="Rock"):
            print("Rock wins")
            final="Rock"
        elif User_choice==Computer_choice:

            final="Tie"

        if final==User_choice:
            print("you wins this round")
            User_score+=1

        elif final==Computer_choice:
            print("computer wins in this round ")
            Computer_Score+=1

        elif final=="Tie":
            print("It's tie")
            tie+=1


    print()
    print("****Scores are****")
    print("Your_Score are:",User_score)
    print("Computer_Score are:",Computer_Score)
    print("Tie:",tie)

    if User_score>Computer_Score :
        print(" *you are Winner*")
    elif Computer_Score>User_score:
        print("*Computer Winner*")
    elif User_score==Computer_Score:
        print("*It's tie*")

while True:
    rps_game()
    repeat = input("Do you want to play again? (yes/no): ").strip().lower()
    if repeat != "yes":
        print("Thanks for playing!")
        break
    print()
    print()



