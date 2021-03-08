# -*- coding: utf-8 -*-

###############################################################################
###############################################################################
# Encoding    
#     V01
#     Minimalversion
###############################################################################
###############################################################################

#%% Userinput -----------------------------------------------------------------

char = input("Choose your character.\n")
encd = int(input("Choose your encoding number.\n"))

#%% Translation of character input --------------------------------------------
print()
for _ in char:
    print(char +
          " wird zu " +
          chr(ord(_)-encd)
    )

###############################################################################
###############################################################################
# Encoding    
#     V02
#     Venere
###############################################################################
###############################################################################

#%% Initialize packages

import sys

#%% Choose range of possible message characters -------------------------------

# Example using characters for normal text
# encrypt_min    = 32
# encrypt_max    = 126

# Example using only upper case characters
encrypt_min    = 65
encrypt_max    = 65+26

encrypt_space  = list(range(encrypt_min,
                            encrypt_max
                      )
)

#%% Userinput -----------------------------------------------------------------

# list assignment important for replacing single characters. The reason is that
# strings are having a single memory reference, as opposed to list. So deep and
# shallow copies are the difference (ask tutors!)

message  = list(input("Choose your message in ASCII space.\n"))

# Use single character for caesar cipher disk
password = list(input("Choose your password in ASCII space.\n"))

#%% Stop program if input does not correspond to encrypt space ----------------

for _ in message + password:
    if ord(_) not in encrypt_space:
        sys.exit("Input not part of allowed characters.")

#%% Store occurrence of spaces and remove them --------------------------------

# spaces = list()
# for pos, x in enumerate(message):
#     if(x == " "):
#         spaces.append(pos)
#         del(message[pos])

###############################################################################
# Encryption using Venere's method (actually by Bellaso 1553)
###############################################################################

#%% Translate characters to ASCII decimals ------------------------------------

# Learned something suuuper important. While automatic copying is found during
# variable assignment, the same is not true for lists. Here, only the reference
# is copied, so that changing the list is now possible through both names - WTF
# ASK TUTOR!

message_deci  = list(message)
for pos, char in enumerate(message_deci):
    message_deci[pos] = ord(char) - encrypt_min
    
password_deci = list(password)
for pos, char in enumerate(password_deci):
    password_deci[pos] = ord(char) - encrypt_min

#%% List of repetitions of the password until it has same length as message

password_deci_rep = list(password_deci)

# Add until the length of password vector is same or longer than message
iteration = int()

while len(password_deci_rep) <= len(message_deci):
    
    password_deci_rep = password_deci_rep + (password_deci)

    # Possibility to make it harder to decipher
    # password_deci_rep = password_deci_rep + list(range(1,1)) + (password_deci)
    # iteration += 1

# Truncate password vector if it is longer
password_deci_rep = password_deci_rep[ : len(message_deci)]

#%% Calculate shift for each message character --------------------------------

message_deci_trans = list()
for pos, cont in enumerate(password_deci_rep):
    message_deci_trans.append(message_deci[pos] + password_deci_rep[pos])
    
#%% Iterate through encryption space ------------------------------------------

# For this approach to work, we need to set the first character to 0 as this
# sets the iteration point using modulus

message_deci_trans_space = list()

for x in message_deci_trans:
    
    # If the number is higher than the allowed encryption space (e.g. 26)
    if x >= len(encrypt_space):
        
        # Modulus shows where it is upon repetition of space
        message_deci_trans_space.append(x%len(encrypt_space))
    
    # If it is a shift within the space, just add it
    else:
        message_deci_trans_space.append(x)

#%% Translate back to ASCII ---------------------------------------------------

message_trans = list()
for nr in message_deci_trans_space:
    message_trans.append(chr(nr + encrypt_min))

#%% Encrypted message output as string

message_output = str()
for x in message_trans:
    message_output += x
    
print(message_output)
