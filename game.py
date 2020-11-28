import random
attempts = 1
your_score = 0
comp_score = 0

lst = ["r", "p", "s"]
comp = random.choice(lst)

while(attempts<=10):
    inp = input("enter any one r for Rock , p for paper and s for scissor: ")
    inp = inp.lower()

    if comp == inp:
        print("both choose the same, no points consider")

    elif comp == "r" and inp == "p":
        your_score = your_score + 1
        print(f"you get one point cos computer choose {comp} and you choose {inp}")


    elif comp == "r" and inp == "s":
        comp_score = comp_score + 1
        print(f"comp get one point cos you choose {inp} and computer choose {comp}")  


    elif comp == "p" and inp == "s":
        your_score = your_score + 1
        print(f"you get one point cos computer choose {comp} and you choose {inp}")  


    elif comp == "p" and inp == "r":
        comp_score = comp_score + 1
        print(f"computer get one point cos you choose {inp} and computer choose {comp}")


    elif comp == "s" and inp == "r":
        your_score = your_score + 1
        print(f"you get one point cos computer choose {comp} and you choose {inp}")


    elif comp == "s" and inp == "p":
        comp_score = comp_score + 1
        print(f"computer get one point cos computer choose {comp} and you choose {inp}")

    else:
        print("invalid input")
    
    attempts = attempts+1
if attempts>10:
    print("Game Over")
    print(f"your score is {your_score} and computer score is {comp_score}")
    if comp_score>your_score:
        print("computer wins!!")
    elif comp_score<your_score:
        print("congo you win!!")
    else:
        print("game is tie")
