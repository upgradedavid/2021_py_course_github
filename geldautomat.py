# -*- coding: utf-8 -*-

###############################################################################
# Geldautomat
#     V01
#     Minimalversion
###############################################################################

# Kundeneingabe ---------------------------------------------------------------

kund_betr = int(input("Wie viel Geld wollen Sie von mir?\n"))

# Berechnung ------------------------------------------------------------------

# Modulo zeigt Anzahl an
# Rest an nächste Stückelung weitergegeben

anzahl_100er = kund_betr//100
rest_100er   = kund_betr%100

anzahl_50er = rest_100er//50
rest_50er   = rest_100er%50

anzahl_20er = rest_50er//20
rest_20er   = rest_50er%20

anzahl_10er = rest_20er//10
rest_10er   = rest_20er%10

# Printing --------------------------------------------------------------------

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
          " auf ihrem Konto.\n"
    )
    kund_betr = float(input("Wie viel Geld wollen Sie von mir?\n"))
    
#%% Rundung des Betrages falls nötig ------------------------------------------

if kund_betr//10 != kund_betr:
    print("\nWir mussten Ihren Betrag runden!")
    kund_betr = int(kund_betr//10*10)
    print(kund_betr)

#%% Stückelung herausfinden ---------------------------------------------------

# Variable initiieren
scheinmax = 0

# Mögliche Scheingrößen
scheine = sorted([100, 50, 20, 10],
                 reverse = True
)

# User MUSS eine von den Größen eingeben
while(scheinmax not in scheine):
    scheinmax = float(input("Wählen Sie die maximale Grösse von Scheinen " +
                            str(scheine) +
                            "\n"
                      )
    )

# Auszahlung ------------------------------------------------------------------

print("\nBesten Dank, hier ihre Auszahlung:\n")

for _ in scheine[scheine.index(scheinmax):]:
    print(str(_) + "er: " + str(kund_betr//_))
    kund_betr = kund_betr%_