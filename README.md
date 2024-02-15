# chessWithQueens

- Erwartung: ist (bedingt durch gefundenes Muster + 3 Rotationen zzgl jeweils 3 Spiegelungen (h, v, h+v)) durch 16 (eher 8) teilbar 
- Ergebnis:  92
- Erklaerungsversuch: Rotationen oder Spiegelungen, die ihr urspruengliches Dasein beschreiben, existieren
  - in 'damen_puzzle/findeGrundmuster.py' wird diese Annahme bestaetigt: EINE 2fach-Rotation erzeugt das Grundmuster erneut
    - 11 Grundmuster in 8 verschiedenen Rotationen/Spiegelungen UND
    - 1 Grundmuster in 4 verschiedenen Rotationen/Spiegelungen
- durch das Ergruenden der Grundmuster zeigt sich, dass sich, in den in 'alleMoeglichenPositionen()' aufgerufenen Funktionen, jede Positionierungs-Variante zu doppeln scheint
  - aus Performance-Gruenden koennte dort eine Optimierung, via Reduktion der Rotations- und Spiegelungsfunktionen, vorgenommen werden
    - dies bedarf einer Analyse der konkreten Musterbildung
