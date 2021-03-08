# -*- coding: utf-8 -*-

###############################################################################
# Geldautomat
#     V01
#     Minimalversion
###############################################################################

#%% Kundeneingabe -------------------------------------------------------------

kund_betr = int(input("Wie viel Geld wollen Sie von mir?\n"))

# Berechnung ------------------------------------------------------------------

# Modulo zeigt Anzahl an > Divisionsrest > nächste Stückelung

anzahl_100er = kund_betr//100
rest_100er   = kund_betr%100

anzahl_50er = rest_100er//50
rest_50er   = rest_100er%50

anzahl_20er = rest_50er//20
rest_20er   = rest_50er%20

anzahl_10er = rest_20er//10
rest_10er   = rest_20er%10

#%% Printing ------------------------------------------------------------------

print("\nBesten Dank, hier ihre Auszahlung:")

print("100er: ", anzahl_100er)
print("50er: ", anzahl_50er)
print("20er: ", anzahl_20er)
print("10er: ", anzahl_10er)

###############################################################################
# Geldautomat
#     V02
#     Erweiterte Version
###############################################################################

#%% Kundeneingabe -------------------------------------------------------------
kund_betr = float(input("Wie viel Geld wollen Sie von mir?\n"))

#%% Kontobetrag überschritten -------------------------------------------------

kontobetrag = 1000

while kund_betr >= kontobetrag:
    print("\nLeider haben Sie nur " +
          str(kontobetrag) +
          " auf ihrem Konto."
    )
    kund_betr = float(input("Wie viel Geld wollen Sie von mir?\n"))
    
#%% Stückelung herausfinden ---------------------------------------------------

# Usereingabe
scheine = input("Bitte Scheingrößen angeben.\n")

# Trennung zu Einzelnen Einträgen des Strings
scheine = scheine.split(sep = ",")

# Konvertierung zu Integern mit "list-comprehension"
# https://www.w3schools.com/python/python_lists_comprehension.asp
scheine = [int(_) for _ in scheine]

# Sortieren erst möglich nach Konversion zu Integer
scheine = sorted(scheine,
                 reverse = True
)
    
#%% Rundung des Betrages falls nötig ------------------------------------------

# Wenn der Betrag nicht mit den möglichen Scheine ausbezahlt werden kann, wird
# der Kundenbetrag gerundet auf die kleinsten Scheine
 
if kund_betr//min(scheine) != kund_betr:
    print("\nWir mussten Ihren Betrag runden!")
    kund_betr = int(kund_betr//min(scheine)*min(scheine))
    print(kund_betr)

#%% Auszahlung ----------------------------------------------------------------

print("\nBesten Dank, hier ihre Auszahlung:\n")

# Variable Kundenbetrag wird sukzessive durch den Divisionsrest ersetzt
for _ in scheine:
    print(str(_) + "er: " + str(kund_betr // _))
    kund_betr = kund_betr % _