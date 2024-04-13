################################
# Dinesh Gurung
# BE.Instrumentation and Control Engineering (1ICE)
# 02220232
################################
# REFERENCES
#1.https://www.geeksforgeeks.org/file-handling-python/
#2.https://docs.python.org/3/tutorial/modules.html
#3.https://docs.python.org/3/tutorial/datastructures.html#more-on-conditions
#4.https://docs.python.org/3/tutorial/controlflow.html#if-statements
#5.https://docs.python.org/3/tutorial/inputoutput.html#the-string-format-method
################################
# SOLUTION
# Your Solution Score: 45282
# Put your number here: 02220232
################################
def read_input():
    file = open("input_2_cap1.txt", "r") # Opening the txt file as read mode
    number_of_lines = file.readlines() # reading each lines
    file.close() #closing the file
    return [line.strip().split() for line in number_of_lines] #Removing the whitespace and symbols and splitting and returning the lines
                                                                                # A & 1 == Rock          X == need to end with lose
def calculate_score(computer_input, initial_score):                             # B & 2 == Paper         Y == need to end with draw
    computer = computer_input     #Assigning to variable computer                                               # C & 3 == Scissors      Z == need to end with win
    if computer[0] == 'A':     
        if computer[1] == "X":  #need to end with Lose
            initial_score += 3  #Line 25 to 31 ####It calculate the score of Rock and its three conditions                                                                      
        elif computer[1] == "Y":# Need to end with Draw
            initial_score += 4
        else:                   # Need to end with win
            initial_score += 8
    elif computer[0] == 'B':
        if computer[1] == "X":   #need to end with Lose
            initial_score += 1   # From line 32 to 38 ### It calculate the score of Paper and irs three conditions
        elif computer[1] == "Y": # Need to end with Draw
            initial_score += 2
        else:                     # Need to end with win
            initial_score += 8                                                              
    elif computer[0] == "C":
        if computer[1] == "X":  #need to end with Lose
            initial_score += 2  # From line 39 to 45 # It calculate the score of Scissors and its three conditions
        elif computer[1] == 'Y':# Need to end with Draw
            initial_score += 6
        else:                   # Need to end with win
            initial_score += 7
    return initial_score

#score before game
initial_score = 0  # Set initial score to 0

computer_inputs = read_input()
for computer_input in computer_inputs:   #Looping into the lines 
    initial_score = calculate_score(computer_input, initial_score) #calculating the score for each line present in the input file

print(f"\n----------TOTAL SCORE_---------\n\t    {initial_score}") #Display final score after each line's score had been calculated

