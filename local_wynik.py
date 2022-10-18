try:
    from getch import getch
except:
    from msvcrt import getch as getch


def printwynik(path):
    try:
        with open(path + 'Wyniki.pyg', 'r') as wynik:
            pass
    except:
        with open(path + 'Wyniki.pyg', 'w') as wynik:
            pass
    with open(path + 'Wyniki.pyg', 'r') as wynik:
        wynik = wynik.readlines()
        for t in range(len(wynik)):
            wynik[t] = wynik[t][:-1]
            wynik[t] = wynik[t].split("|")
            wynik[t] = wynik[t][:7]
            wynik[t][0] = int(wynik[t][0])
        wynik = sorted(wynik)
        #        ---------------------------błąd
        for t in range(len(wynik)):
            wynik[t][0] = str(wynik[t][0])
            while len(wynik[t][0]) < 7:
                wynik[t][0] += " "
            while len(wynik[t][1]) < 15:
                wynik[t][1] += " "
            while len(wynik[t][3]) < 7:
                wynik[t][3] += " "
            while len(wynik[t][4]) < 3:
                wynik[t][4] += " "
            while len(wynik[t][5]) < 3:
                wynik[t][5] += " "
            #        ---------------------------
        print("? Wynik:  Tury:   Lw: Po: Nazwa gracza:   Typ postaci:")
        wynik = wynik[-23:]
        for t in range(len(wynik)):
            print(wynik[t][6] + " " + wynik[t][0] + " " + wynik[t][3] + " " + wynik[t][4] + " " + wynik[t][5] + " " + wynik[t][1][:15] + " " + wynik[t][2])
    getch()