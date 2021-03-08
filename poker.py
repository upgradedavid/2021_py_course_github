# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 14:29:12 2021

@author: daviv
"""

print("*********")
print("P O K E R")
print("*********")
print("EINGABE IHRER KARTEN")
print("Geben Sie die Karten sortiert nach der Wertigkeit ein (hohe Wertigkeit vor tiefer Wertigkeit):")
print()


wert1 = int(input("1. Wert: "))
farbe1 = int(input("1. Farbe: "))
wert2 = int(input("2. Wert: "))
farbe2 = int(input("2. Farbe: "))
wert3 = int(input("3. Wert: "))
farbe3 = int(input("3. Farbe: "))
wert4 = int(input("4. Wert: "))
farbe4 = int(input("4. Farbe: "))
wert5 = int(input("5. Wert: "))
farbe5 = int(input("5. Farbe: "))
print()
print("Sie haben eingegeben:")
print("Karte 1 (Wert|Farbe):", wert1, farbe1)
print("Karte 2 (Wert|Farbe):", wert2, farbe2)
print("Karte 3 (Wert|Farbe):", wert3, farbe3)
print("Karte 4 (Wert|Farbe):", wert4, farbe4)
print("Karte 5 (Wert|Farbe):", wert5, farbe5)

#%% let's make two lists of our input

werte = sorted([wert1,
                wert2,
                wert3,
                wert4,
                wert5
               ]
)

farbe = [farbe1,
         farbe2,
         farbe3,
         farbe4,
         farbe5
]

#%% Adjust to lowest number to check sequence

werte_adj = list()
for x in werte:
    werte_adj.append(x - min(werte))    

sequence_bool = False
if max(werte_adj) == 4:
    sequence_bool = True
    
#%% Does the sequence have only one colour?

allcolour_bool = False
if len(set(farbe)) == 1:
    allcolour_bool = True
    
#%% How many different cards are there?

handscheck = list()
handscheck.append(1)

for x in range(0,4):
    if werte[x] == werte[x+1]:
        handscheck[len(handscheck)-1] += 1
    else:
        handscheck.append(1)

handscheck = sorted(handscheck)

differentcards = len(handscheck)
maxnrofsamecard = max(handscheck)

#%% Let's put that all together...

# Royal flush definition
if allcolour_bool == True and \
   sequence_bool == True and \
   max(werte) == 14:
       print("Royal Flush")
    
# Straight flush definition
if allcolour_bool == True and \
   sequence_bool == True and \
   max(werte) != 14:
       print("Straight Flush")
        
# Four of a kind definition
if maxnrofsamecard == 4:
        print("Four of a kind")

# Full house defintion
if differentcards == 2 and \
   maxnrofsamecard == 3:
       print("Full house")

# Flush definition
if sequence_bool == False and \
   allcolour_bool == True and \
   differentcards == 5:
       print("Flush")
       
# Straight definition
if sequence_bool == True and \
   allcolour_bool == False:
       print("Straight")
       
# Drilling definition
if differentcards == 3 and \
   maxnrofsamecard == 3:
       print("Three of a kind")

# Two pairsd efinition
if differentcards == 3 and \
   maxnrofsamecard == 2:
       print("Two pairs")

# One pair definition      
if differentcards == 4:
       print("One pair")