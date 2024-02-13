# Programm zur Ermittlung aller Positionen, die Acht Damen auf einem Schachbrett 
# einnehmen koennen, ohne sich gegenseitig schlagen zu koennen.

# Aufgrund der Funktionen sollten alle Rotationen und Spiegelungen abgedeckt sein.
# Hierfuer gibt es dennoch Prueffunktionen.



# Liste zum Eintragen der Loesungen
loesungen = []

# Initialfunktion
def startfunction():

    spielfeld = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]

    
    recursionSpielfeld(0, spielfeld)    
    pruefung()
    pruefungDopplung()
    rotationenUndSpiegelungPruefen()



# Rekursion der Reihen und abgehen aller Positionen der Damen innerhalb der Reihen
def recursionSpielfeld(reihe, spielfeld):    
    freiFelder = pruefungDerReihe(spielfeld[reihe])
    if len(freiFelder) == 0:
        return 
    for dame in freiFelder:

        # Anfertigung einer Kopie von Spielfeld
        temp = []
        for i in spielfeld:
            tempReihe = []
            for j in i:
                tempReihe.append(j)
            temp.append(tempReihe)

        temp[reihe][dame] = 'D'
        temp = schlagWegeEintragen(dame, reihe, temp)
        
        if reihe < 7:
            recursionSpielfeld(reihe + 1, temp) 
        else:
            zeigeSpielfeld(temp)
            loesungen.append(temp)

# Rueckgabe von Positionen, die nicht von moeglichen Zuegen weiter oben gesetzter Damen blockiert werden
def pruefungDerReihe(reihe):
    return [x for x in range(8) if reihe[x] == 0]

# Aufrufen der verschiedenen BlockadePfade
def schlagWegeEintragen(dameInReihe, dameInSpalte, spielfeld):
    spielfeld = vertikal(dameInReihe, dameInSpalte, spielfeld)
    spielfeld = diagonal(dameInReihe, dameInSpalte, spielfeld)
    spielfeld = horizontal(dameInReihe, dameInSpalte, spielfeld)
    return spielfeld

# Blockieren der Pfade in der Horizontalen, zur Absicherung gegen Dopplungen in einer Reihe
def horizontal(damenPositionInReihe, damenPositionInSpalte, spielfeld):
    if damenPositionInReihe > 0:
        for i in range(0, damenPositionInReihe):
            spielfeld[damenPositionInSpalte][i] = 1
    if damenPositionInReihe < 7:
        for i in range(damenPositionInReihe + 1, 8):
            spielfeld[damenPositionInSpalte][i] = 1
    return spielfeld

# Blockieren der Pfade nach Unten, da reihenbasierte Positionierung
def vertikal(damenPositionInReihe, damenPositionInSpalte, spielfeld):
    for i in range(damenPositionInSpalte + 1, 8):
        spielfeld[i][damenPositionInReihe] = 1
    return spielfeld

# Blockieren der Pfade nach Diagonal-Unten, da reihenbasierte Positionierung
def diagonal(damenPositionInReihe, damenPositionInSpalte, spielfeld):
    linksrechts = 1
    for i in range(damenPositionInSpalte + 1, 8):
        if (damenPositionInReihe - linksrechts >= 0):
            spielfeld[i][damenPositionInReihe - linksrechts] = 1
        if (damenPositionInReihe + linksrechts <= 7):
            spielfeld[i][damenPositionInReihe + linksrechts] = 1
        linksrechts += 1
    return spielfeld

# Ausgabe der Moeglichkeiten in der Konsole
def zeigeSpielfeld(spielfeld):
    # Ausgabe: einem Quadrat so nah wie moeglich kommen => Lesbarkeit
    for reihe in spielfeld:
        temp = [x if x == 'D' else '_' for x in reihe]
        s = ''
        for t in temp:
            s += str(t)+' '
        print(s)
        # print(reihe)
    print()


##################
# Pruefungsblock #
##################
    
# Einstieg in Pruefungsblock
def pruefung():
    for n, l in enumerate(loesungen):
        print('Musterloesung Nr.' + str(n))
        pruefungVerteiler(l)
    print()
    print('Gesamt: ' + str(len(loesungen)))

# Verteiler auf Unterfunktionen
def pruefungVerteiler(loesungSpielfeld):
    print('Reihen:')
    pruefungReihen(loesungSpielfeld)
    pruefungSpalten(loesungSpielfeld)

 # In einer Reihe muss eine Dame ('D') einmal vorkommen 
def pruefungReihen(loesungSpielfeld):
    for i in range(8):
        if len([x for x in loesungSpielfeld[i] if x == 'D']) == 1:
            print('eine Dame ' + str(i))
        else:
            print('Fehler in ' + str(i))
    print()

# Umbau via Rotation um 90 Grad => pruefungReihen() kann erneut verwendet werden
def pruefungSpalten(loesungSpielfeld):
    temp = []
    for i in range(8):
        tempReihe = []
        for j in range(8):
            tempReihe.append(loesungSpielfeld[j][i])
        temp.append(tempReihe)
    print('Spalten:')
    pruefungReihen(temp)


##################################    
# Pruefung auf identische Muster #
##################################

# einfache Pruefung
def pruefungDopplung():   
    z = 0 
    for n, i in enumerate(loesungen):
        for m, j in enumerate(loesungen):
            if i == j and n != m:
                z += 1
                print(i)
    print ('Anzahl der Dopplung (Nach Abschluss der RecursionSpielfeld()): ' + str(z))


############################################    
# Pruefung auf gespiegelte/rotierte Muster #
############################################

# Pruefen, ob alle 8 Muster, die durch Rotation und Spiegelung entstehen, bereits gefunden sind
def rotationenUndSpiegelungPruefen():
    z = 0
    for l in loesungen:
        alleMoeglPos = alleMoeglichenPositionen(l)
        for a in alleMoeglPos:
            if a not in loesungen:
                z += 1
    print('Anzahl der Dopplung (Entdeckt durch Rotation und Spiegelung): ' + str(z))

# Verteiler fuer Rotation und Spiegelung
def alleMoeglichenPositionen(spielfeld):
    temp = []
    temp.append(spielfeld)
    for i in range(3):
        temp.append(rotation(temp[-1]))
    for i in range(4):
        temp.append(spiegelnHorizontaleAchse(temp[i]))
        temp.append(spiegelnVertikaleAchse(temp[i]))
    return temp

# rotiert um 90 Grad
def rotation(spielfeld):
    temp = []
    for i in range(8):
        tempReihe = []
        for j in range(8):
            tempReihe.append(spielfeld[j][i])
        temp.append(tempReihe)
    return temp

# spiegelt an der Vertikalen Achse (von links nach rechts)
def spiegelnVertikaleAchse(spielfeld):
    temp = []
    for i in range(8):
        tempReihe = []
        for j in range(8):
            tempReihe.append(spielfeld[i][7 - j])
        temp.append(tempReihe)
    return temp

# spiegelt an der horizontalen Achse (von oben nach unten)
def spiegelnHorizontaleAchse(spielfeld):
    temp = []
    for i in range(8):
        tempReihe = []
        for j in range(8):
            tempReihe.append(spielfeld[7 - i][j])
        temp.append(tempReihe)
    return temp

# Aufruf der Initalfunktion
startfunction()
