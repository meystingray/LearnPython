import random


def getWinner(choice1,choice2):
    if choice1 == 1 and choice2 == 3:
        return(1)
    elif choice1 == 1 and choice2 == 2:
        return(2)
    elif choice1 == 2 and choice2 == 1:
        return(2)
        

def main():
    seq = ("Rock","Paper","Scissors")
    computerChoice = random.choice(list(range(1,len(seq)+1)))
    userChoice = int(input("Let's play Rock, Paper Scissors! \n"
                       "Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))
    
    
    print("Computer: ",seq[computerChoice-1])
    print("User: ",seq[userChoice-1])
    
    if computerChoice == userChoice:
        print("Tie")
    elif computerChoice == 1 and userChoice = 2:
        print("Computer Wins!")
    else:
        print("User Wins!")
   
# 1 beats 3
# 2 beats 1
# 3 beats 2

main()