
def round():

    rock="""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """


    paper="""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """


    scissors="""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """

    choice=int(input("Enter your choice 0 for rock,1 for paper,2 for scissors:::"))
    if choice==0:
        print("your choice is",rock)
    elif choice==1:
        print("your choice is",paper)
    elif choice==2:
        print("your choice is",scissors)
    else:
        print("select valid option")

    import random
    list = [rock, paper, scissors]
    computer = random.choice(list)
    if choice in(0,1,2):
        print("Computer choice is" ,computer)

    if choice==0 and computer==list[0]:
        print("The game is Draw")
    elif choice==0 and computer==list[1]:
        print("Computer won")
    elif choice==0 and computer==list[2]:
        print("You won")
    elif choice==1 and computer==list[0]:
        print("You won")
    elif choice==1 and computer==list[1]:
        print("The game is Draw")
    elif choice==1 and computer==list[2]:
        print("Computer won")
    elif choice==2 and computer==list[0]:
        print("Computer won")
    elif choice==2 and computer==list[1]:
        print("You won")
    elif choice==2 and computer==list[2]:
        print("The game is Draw")


no_of_turns=int(input("Enter How many rounds you need to play::"))
for i in range(no_of_turns):
    round()


