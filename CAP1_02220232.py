################################
# Dinesh Gurung
# BE.Instrumentation and Control Engineering (1ICE)
# 02220232
################################
# REFERENCES
#1.https://www.w3schools.com/python/python_variables_global.asp
#2.https://docs.python.org/3/tutorial/modules.html
#3.https://docs.python.org/3/tutorial/datastructures.html#more-on-conditions
#4.https://docs.python.org/3/tutorial/controlflow.html#if-statements
#5.https://docs.python.org/3/tutorial/inputoutput.html#the-string-format-method
################################
# SOLUTION
# Your Solution Score: 15
# Put your number here: 1-2-3 and opponent:C-C-B(Z+3)
################################
import random
max_round = int(input("Enter the maximum round you want to play: "))
score = 0
computer_score = 0
def read_input():
    file = open("input_2_cap1.txt", "r")
    computer = file.readlines()
    computer_input = random.choice(computer).split() # Use only the first two elements
    file.close()
    print("----------------------------------------------------------------------------")
    player_input = int(input("Make a choice: 1.Rock\t2.Paper\t3.Scissors\n--> "))
            
    return computer_input, player_input

def calculate_score(computer_input, player_input, attempt_left, initial_score):
                          ###########Details about the rule and score system of the game################         ########Special case##########
    computer = computer_input                   # 1 & A = Rock      Y = Have to Draw the game            # Win 6 points       extra point(s) if you meet 
    player = player_input                       # 2 & B = Paper     Z = Have to Win against Opponent     #Lose 0 points       opponent conditions to end game
    if (player_input > 0) and(player_input <=3):# 3 & C = Scissors  X = Have to lose               # Draw 3 points      Refer game rule for conditions 
        if computer[0] == 'A':
            if player == 1:
                if computer[1] == 'Y':
                    initial_score += 4                                                                # computer = computer random choice
                    print("4 points: (Rock vs Rock): Opponent chose to end with Draw:(+1) ")          # player = player_input
                else:
                    initial_score += 3
                    print("3 points: (Rock vs Rock):")
            elif player == 2:
                if computer[1] == 'Z':
                    initial_score += 8
                    print("8 points: (Rock vs Paper): opponent chose you to enf with Win:(+2) ")
                else:
                    initial_score += 6
                    print("6 points: (Rock vs Paper): You won")
            elif player == 3:
                if computer[1] == 'X':
                    initial_score += 3
                    print("3 points: (Rock vs Scissors): Opponent chose you to end with lose:(+3)") # You will get some points even if  you lose,
                else:                                                                               # if you meet the opponent's second condition
                    initial_score += 0
                    print("0 points: (Rock vs Scissors): You lose")

        elif computer[0] == 'B':
            if player == 1:
                if computer[1] == 'X':
                    initial_score += 1
                    print("1 points: (Paper Vs Rock): Opponent chose you to end with lose:(+1)")
                else:
                    initial_score += 0
                    print("0 points: (Paper vs Rock): You lose")
            elif player == 2:
                if computer[1] == 'Y':
                    initial_score += 5
                    print("5 points: (Paper vs Paper): Opponent chose to end with Draw:(+2)")
                else:
                    initial_score += 3
                    print("3 points: (Paper vs Paper):")
            elif player == 3:
                if computer[1] == 'X':
                    initial_score += 9
                    print("9 points: (Paper vs Scissors): Opponent chose you to end  win:(+3)")
                else:
                    initial_score += 6
                    print("6 points: (Paper vs Scissors):")
        elif computer[0] == 'C':
            if player == 1:
                if computer[1] == 'Z':
                    initial_score += 7
                    print("7 points: (Scissors vs Rock): Opponent chose you to won:(+1)")
                else:
                    initial_score += 6
                    print("6 points: (Scissors vs Rock): You win")
            elif player == 2:
                if computer[1] == 'X':
                    initial_score += 2
                    print(" 2 points: (scissors vs Rock): opponent chose you to lose:(+2)")
                else:
                    initial_score += 0
                    print("0 points: (Scissors vs Rock): You lose")
            elif player == 3:
                if computer[1] == 'Y':
                    initial_score += 6
                    print("6 points: (Scissors vs Scissors): Opponent chose you to end Draw:(+3)")
                else:
                    initial_score += 3
                    print("3 points: (Scissors vs Scissors):")
        if attempt_left > 1:
            return calculate_score(*read_input(), attempt_left - 1, initial_score)
        else:
                print(f"\n----------FINAL SCORE ---------\n\t       {initial_score}")
    else:
        print("---------Invalid Choice--------------")  #If your choice is not between 1 to 3, than makes to enter 0 for restarting the game 
        restart=(int(input("ENTER 0 TO RESTART: ")))
        if restart == 0:
            calculate_score(*read_input(),attempt_left,initial_score)
        else:
            print("----------------------------------\nSORRY FAIL TO RESTART!")
calculate_score(*read_input(), max_round, score)
