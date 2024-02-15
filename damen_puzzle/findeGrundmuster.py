# Ziel ist zu klaeren, warum das Ergebnis nicht durch 8, 12 oder 16 teilbar ist.
# Die Annahme: es muss mindestens eine symmetrische Loesung geben: Diese gilt es zu finden: 

import copy
# mainV10 ist die Hauptlogik zur Generierung der urspruenglichen 92 Loesungen
import mainV10

# Variable fuer die 92 Loesungen
loesungUngefiltert = copy.deepcopy(mainV10.loesungen)
# Variable fuer die Grundmuster
loesungGefiltert = []

# Initialfunktion
def startfunktion():
    filter()
    erzeugenSichSelbst()

# aus den 92 moeglichen Positionierungen, jene herausfiltern, die die Grundmuster bilden
def filter():    
    for lu in loesungUngefiltert:
        aMP = mainV10.alleMoeglichenPositionen(lu)
        z = 0
        for a in aMP:
            if a not in loesungGefiltert:
                z += 1
            else:
                break
        if z == 16:
            loesungGefiltert.append(aMP[0])
    print('Anzahl der Grundmuster: ' + str(len(loesungGefiltert)))

# alle 16 Varianten jedes der 12 Grundmuster auf Gleichheit pruefen
def erzeugenSichSelbst():
    print('Alle symmetrischen Positionierungen:')
    for lg in loesungGefiltert:
        aMP = mainV10.alleMoeglichenPositionen(lg)
        z = 0
        for a in aMP:
            if a == lg:
                z += 1
        # da sich, aufgrund der diversen Rotationen und Spiegelungen, immer eine Dopplung findet, 
        # braucht es mindestens eine weitere, um eine symmetrische Loesung zu finden => >2
        if z > 2:
            mainV10.zeigeSpielfeld(lg)

# Aufruf Initialfunktion
startfunktion()
        
