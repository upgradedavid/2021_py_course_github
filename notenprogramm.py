# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 14:09:59 2021

@author: daviv
"""

eingeben_bool = True
noten = list()
while eingeben_bool == True:
    eingabe = input("Bitte Noten als integer eingeben, oder quit um\n" +
                           "den Mittelwert zu berechnen.\n"
    )
    
    if eingabe == "quit":
        eingeben_bool = False
    else:
        noten.append(int(eingabe))
        
    
summenoten = 0
for x in noten:
    summenoten += x
    
durschnitt = round(summenoten/len(noten), 2)

print("Durchschnitt:\n" +
      str(durschnitt)
)