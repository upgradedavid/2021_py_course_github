# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 09:53:18 2021

@author: daviv
"""

###############################################################################
# Zahlen raten v2: MINIMAL
###############################################################################

# Did not get: "Fuehren Sie fuer die Eingabe der Zahl eine Ausnahmebedingung
# ein.

###############################################################################

#%% packages needed -----------------------------------------------------------

import sys

#%% Functions needed ----------------------------------------------------------

# Convert winning number to ASCII

def ascii_convert(string):
    conv = list()  
    for x in string:
        conv.append(ord(x))
    return(conv)

# BOOLEAN: Check if a string is a number, and if yes, check the range

def checkif_nr(tocheck):
    if str.isdigit(tocheck) == True:
        tocheck = int(tocheck)
        if tocheck >= 0 and tocheck <= 100:
            return(True)
        else:
            return(False)
    else:
        return(False)

    
# BOOLEAN: Check if characters are allowed in general

def checkif_ascii_space(tocheck):
    
    allowednrs = list()
    
    # Capital letters added
    allowednrs = allowednrs + list(range(65, 65 + 26))

    # Numbers added
    allowednrs = allowednrs + list(range(48, 57))

    for x in tocheck:
        if x not in allowednrs:
            return(False)
    
    return(True)
        

#%% User input ----------------------------------------------------------------

win_nr = input("#########################################################" +
               "\n" +
               "Start the guessing game by typing the winning number or " +
               "\n" +
               "character sequence." +
               "\n" +
               "\n" +
               "Using a number between 0 and 100 initiates the numbers game" +
               "\n" +
               "while other sequences initiate the sequence game." +
               "\n" +
               "#########################################################\n"
)

#%% Complain if the space is wrong for winning string
if checkif_ascii_space(ascii_convert(win_nr)) == False:
    sys.exit("Possible characters not used, terminating program.")
    
#%% Obtain attempt number
attemptnr = input("How many attempts used (Number 0 to 100 possible)?\n")

#%% Terminate if it is not a number between 0 and 100
if checkif_nr(attemptnr) == False:
    sys.exit("Impossible attempt nr. or input type.")

#%% Check whether the program is about numbers or not -------------------------

if checkif_nr(win_nr) == True:

#%% Game with number ----------------------------------------------------------
    
    input("#########################################################" +
          "\n" +
          "Welcome to the numbers game. Press Enter to start." +
          "\n" +
          "#########################################################"
    )
    
    usertry = 0
    run_bool = True
    
    while run_bool == True:
        usertry += 1
        if usertry <= int(attemptnr):
            guess_nr = input("What number is right?" +
                             "\n" +
                             "Attempts left: " +
                             str(int(attemptnr) - usertry + 1) +
                             "\n"
            )
        
            if str.isdigit(guess_nr) == True:
                if guess_nr == win_nr:
                    run_bool = False                
                    print("\n\nYou win the game!")            
                else: 
                    if int(guess_nr) < int(win_nr):
                        print("\n\nNumber too small!")
                    elif int(guess_nr) > int(win_nr):
                        print("\n\nNumber too large!")
            else:
                print("\n\nNot a number!")
        else:
            run_bool = False
            print("\n\nToo many attempts. Game over.")
            
else:
    
    usertry = 0
    run_bool = True
    
    while run_bool == True:
        usertry += 1
        if usertry <= int(attemptnr):
            guess_text = input("What character is right?" +
                               "\n" +
                               "Attempts left: " +
                               str(int(attemptnr) - usertry + 1) +
                               "\n"
            )
        
            if ascii_convert(guess_text) == ascii_convert(win_nr):
                run_bool = False                
                print("\nYou win the game!")  
            
            else:
                print("Incorrect!" +
                      "\n" +
                      "\n" +
                      "Here's the beginning of the riddle:"
                      "\n" +
                      "\n"
                )
                
                riddlepart = win_nr[:usertry]
                riddlestring = str()
                for x in riddlepart:
                    riddlestring + str(x)
                
                print(riddlepart +
                      "..."
                )
        else:
            run_bool = False
            print("\nToo many attempts. Game over.")