#import curses
#from curses import wrapper

enable_windows_stuff = False
try:
    from getch import getch
except:
    from msvcrt import getch
    enable_windows_stuff = True
from random import randint

from local_help import *
from local import *
from local_pokoj import *
from local_items import items_init
from local_enemies import *#enemies_init, test_enemies, enemies_heads, enemies_attack
from local_wynik import *
from local_droga import *
from local_translator import translate
from local_zero3 import zero3
from local_terrain import terrain

path = ''
def takein():
    global enable_windows_stuff
    if enable_windows_stuff:
        return str(getch())[2]
    return getch()

Backpack, mhp, hp, pd, vision, zbroja, lw, depth, gold, pochodnia, pochotime, licznik, echo, wasattackby, playerdata, name, atak, time, Baner = [], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 0, 0, 0, [0, 0, 0]

def sort():
    global Backpack
    for i in range(len(Backpack)):
        Backpack[i] = Backpack[i][::-1]
    Backpack = sorted(Backpack)
    for i in range(len(Backpack)):
        Backpack[i] = Backpack[i][::-1]
    Backpack = Backpack[::-1]
    
def wezbron():
    atak = 1
    zbroja = 0
    miotacz = 1
    for i in Backpack:
        if i[-1] == "]":
            try:
                j = int(i[-3]+i[-2])
            except:
                j = int(i[-2])
            if j > atak:
                atak = j
        elif i[-1] == "}":
            try:
                k = int(i[-3]+i[-2])
            except:
                k = int(i[-2])
            if k > miotacz:
                miotacz = k
        elif i[-1] == ")":
            try:
                j = int(i[-3]+i[-2])
            except:
                j = int(i[-2])
            if j > zbroja:
                zbroja = j
    return(atak, miotacz, zbroja, echo)

def walka(y, x, atak):
    global rmap, vmap, py, px, npy, npx, echo, pd
    atak += randint(randint((1-atak)//2, 0), 
                    randint(0, (atak-1)//2))
    hp = int(rmap[y][x][1:4])
    k = enemies_heads(rmap[y][x][0])
    if k != "-":
        if randint(0, 99) < 60:
            if hp-atak<=0:
                if rmap[y][x][0] == "B":
                    open_doors(rmap,vmap)
                rmap[y][x] = rmap[y][x][4:]
                vmap[y][x] = rmap[y][x]
                pd += enemies_xp(k)
                echo = translate("YOU KILL") + " " + translate("A MONSTER")
            else:
                rmap[y][x] = rmap[y][x][0] + zero3(hp-atak) + rmap[y][x][4:]
                echo = translate("YOU HIT") + " " + translate("A MONSTER") + " | " + str(atak) + " | " + str(hp-atak) + " |"
        else:
            echo = translate("YOU MISS") + " " + translate("A MONSTER")

def wybierzpostac(Backpack, mhp, hp, pd, vision, zbroja, lw, depth, gold, pochodnia, pochotime, licznik, echo, wasattackby, playerdata, name, atak, time, Baner):
    pd = 0
    vision = 1
    lw = 1
    depth = 1
    gold = 0
    pochodnia = 0
    pochotime = 0
    time = 0
    Baner = [0, 0, 8]
    print("""                                DUNGEONS
                               CHOOSE A CHARACTER
    h - human
    """)
    i = takein()
    if i == "j":
        mhp = 15
        vision = 2
        playerdata = ["Jaguar", "Łowca"]
        Backpack = ["DAGGER [11]"]
    else:
        mhp = 20
        playerdata = ["Human"]
        print("""
        w - warrior
        a - archer
        ? - alchemist
        f - footpad""")
        i = takein()
        if i == "f":
            playerdata.append("Footpad")
            Backpack = ["KNIFE [03]", "SLING {02}"]
            Baner = [Baner[0], 2, 20]
        elif i == "?":
            playerdata.append("Alchemist")
            Backpack = ["KNIFE [03]"]
            Baner[0] = 1
        elif i == "a":
            playerdata.append("Archer")
            Backpack = ["DAGGER [04]", "BOW {03}"]
            Baner = [Baner[0], 3, 35]
        else:
            playerdata.append("Warrior")
            Backpack = ["SMALL SWORD [05]"]
    Backpack.append("TORCH")
    atak = 1

    hp = mhp

    licznik = 0
    echo = ":"
    wasattackby = ""
    sort()
    name = input("Your name (up to 17 letters): ")
    return(Backpack, mhp, hp, pd, vision, zbroja, lw, depth, gold, pochodnia, pochotime, licznik, echo, wasattackby, playerdata, name, atak, time, Baner)

def makemap():
    global depth, rmap, vmap, omap, depth, sizey, sizex, py, px, echo
    j, sizey, sizex, maxp, minp = items_init(path, depth)
    enemies_init(path, depth)
    help_init(path, depth)
    rmap, py, px = makedroga(depth, sizey, sizex, "#", " ", "_", "+", "=", j, maxp, minp)
    rmap[py][px] = "."
        

    vmap = [[" " for _ in range(sizex)] for _ in range(sizey)]
    omap = [[" " for _ in range(sizex)] for _ in range(sizey)]
            #RealMAP VisionMAP OutputMAP
        
def out():
    global rmap, vmap, omap, px, py, Baner
    if pochodnia == 1:
        for y in range(-vision, 1+vision):
            for x in range(-vision, 1+vision):
                i = [(py+y) % sizey, (px+x) % sizex]
                vmap[i[0]][i[1]] = rmap[i[0]][i[1]]
                if rmap[i[0]][i[1]] == "_":
                    vmap[i[0]][i[1]] = "."
    for y in range(len(vmap)):
        for x in range(len(vmap[y])):
            omap[y][x] = vmap[y][x]
    omap[py][px] = "@"
    if pochodnia == 1:
        for y in range(-vision, 1+vision):
            for x in range(-vision, 1+vision):
                i = [(py+y) % sizey, (px+x) % sizex]
                if omap[i[0]][i[1]] == " ":
                    omap[i[0]][i[1]] = "."
    for y in range(23):
        ty = py+y-11
        if ty >= 0 and ty < sizey:
            i = ""
            for x in range(53):
                tx = px+x-26
                if tx >= 0 and tx < sizex:
                    i += omap[ty][tx][0]
                else:
                    i += " "
        else:
            i = "                                                     "
        print(i, end = "|")
        dpos(y, hp, mhp, pd, lw, gold, depth, atak, zbroja, wasattackby, Backpack, Baner)


# X i Y
sizey = 0
sizex = 0
py = 0
px = 0

depth = 1
Backpack, mhp, hp, pd, vision, zbroja, lw, depth, gold, pochodnia, pochotime, licznik, echo, wasattackby, playerdata, name, atak, time, Baner = wybierzpostac(Backpack, mhp, hp, pd, vision, zbroja, lw, depth, gold, pochodnia, pochotime, licznik, echo, wasattackby, playerdata, name, atak, time, Baner)
sort()
atak, Baner[1], zbroja, echo = wezbron()
makemap()
npy = py
npx = px
printwynik(path)
rmap, vmap = testpokoj(rmap, vmap, [py, px])
tlist = [".",","," ","_","]","}",")","~","-","!","?"]
while True:
    out()
    #     -----move_p-----
    moved = 1
    print(echo)
    imput = takein()
    pm = pmover(imput)
    if pm == "q":
        if imput == "i":
            atak, Baner[1], zbroja, echo = wezbron()
            echo = "Wziąłeś najlepszą broń i zbroję jaką masz!:"
        elif imput == "u":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            for i in range(len(Backpack)):
                print(str(i+1)+":", printBackpack(Backpack, i))
            print("Rzecz którą chcesz wypić/urzyć/zapalić/przeczytać (przestanie istnieć!):")
            try:
                i = int(takein())-1
                if i >= 0 and i < len(Backpack):
                    i = Backpack.pop(i)
                
                    if i == "MIXTURE":
                        hp = mhp
                        echo = "Wypiłeś "+ translate(i,1) + " i twoje rany się zagoiły:"
                    elif i == "TORCH":
                        pochodnia = 1
                        pochotime = 200
                        if playerdata[1] == "Footpad":
                            pochotime = 300
                        echo = translate("YOU LIGHT") + " " + translate(i,1) + ", " + translate("AND IT WILL BY IN FIRE") + " " + str(pochotime) + " " + translate("TURNS")
                    else:
                        Backpack.append(i)
                        echo = "Tego nie umiesz wypić/urzyć/zapalić/przeczytać:"
                else:
                    moved = 0
            except:
                moved = 0
        elif imput == "d":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            for i in range(len(Backpack)):
                print(str(i+1)+":", printBackpack(Backpack, i))
            print("Rzecz którą chcesz zostawić (przestanie istnieć!):")
            try:
                i = Backpack.pop(int(takein())-1)
                atak, Baner[1], zbroja, echo = wezbron()
                echo = "Zostawiłeś '"+ i + "':"
            except:
                moved = 0
        elif imput == "t":
            out()
            print("Wybierz kierunek, rzecz którą rzucisz (ta rzecz przestanie istnieć!):")
            try:
                pm = pmover(str(int(takein())))
            except:
                moved = 0
                continue
            npy = int(pm[0])-1
            npx = int(pm[1])-1 
            i = [(py+npy)%sizey, (px+npx)%sizex]
            if pm != "11":
                while rmap[i[0]][i[1]] == " " or rmap[i[0]][i[1]] == "." or rmap[i[0]][i[1]] == ", " or rmap[i[0]][i[1]] == "_" or rmap[i[0]][i[1]] == "]" or rmap[i[0]][i[1]] == ")" or rmap[i[0]][i[1]] == "~" or rmap[i[0]][i[1]] == "$" or rmap[i[0]][i[1]] == ">" or rmap[i[0]][i[1]] == "<":
                    i = [(i[0]+npy)%sizey, (i[1]+npx)%sizex]
            if rmap[i[0]][i[1]] == "#" or rmap[i[0]][i[1]] == "+":
                i = [(i[0]-npy)%sizey, (i[1]-npx)%sizex] # cofanie o 1
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            for j in range(len(Backpack)):
                print(str(j+1)+":", printBackpack(Backpack, j))
            try:
                i.append(Backpack.pop(int(takein())-1))
                atak, Baner[1], zbroja, echo = wezbron()
                echo = "Rzuciłeś '"+ i[2] + "':"
                if i[2][-1] == "]":
                    if rmap[i[0]][i[1]][0] == "s" or rmap[i[0]][i[1]][0] == "g" or rmap[i[0]][i[1]][0] == "b" or rmap[i[0]][i[1]][0] == "i":
                        walka(i[0], i[1], int(i[2][-2]))
            except:
                moved = 0
        elif imput == "-":
            if Baner[0] > 0:
                out()
                print("Wybierz kierunek gdzie rzucisz orantium:")
                try:
                    pm = pmover(str(int(takein())))
                    npy = int(pm[0])-1
                    npx = int(pm[1])-1 
                except:
                    moved = 0
                    continue
                i = [(py+npy)%sizey, (px+npx)%sizex]
                if pm != "11":
                    while rmap[i[0]][i[1]][0] in tlist:
                        i = [(i[0]+npy)%sizey, (i[1]+npx)%sizex]
                if rmap[i[0]][i[1]] == "#" or rmap[i[0]][i[1]] == "+":
                    i = [(i[0]-npy)%sizey, (i[1]-npx)%sizex] # cofanie o 1
                i = [(i[0]+2)%sizey, (i[1]+2)%sizex]
                for y in range(i[0]-3, i[0]):
                    for x in range(i[1]-3, i[1]):
                        if rmap[y][x] == "#":
                            rmap[y][x] = "_:"
                        elif rmap[y][x][0] == "B":
                            rmap[y][x] = rmap[y][x][0] + zero3(int(rmap[y][x][1:4])//2) + rmap[y][x][4:]
                        elif ">" in rmap[y][x] or "<" in rmap[y][x]:
                            if ">" in rmap[y][x]:
                                rmap[y][x] = "_>"
                            else:
                                rmap[y][x] = "_<"
                        else:
                            k = enemies_heads(rmap[y][x][0])
                            if k != "-":
                                pd += enemies_xp(k)
                            rmap[y][x] = "_."
                            if omap[y][x] == "@":
                                hp = 0
                        vmap[y][x] = rmap[y][x]
                rmap, vmap = testpokoj(rmap, vmap, [i[0]-2, i[1]-2])
                Baner[0] -= 1
            else:
                moved = 0
        elif imput == "0":
            if Baner[2] > 0:
                out()
                print("Wybierz kierunek gdzie strzelisz (tylko we wrogów):")
                try:
                    pm = pmover(str(int(takein())))
                    npy = int(pm[0])-1
                    npx = int(pm[1])-1 
                except:
                    moved = 0
                    continue
                i = [(py+npy)%sizey, (px+npx)%sizex]
                if pm != "11":
                    while rmap[i[0]][i[1]][0] in tlist:
                        i = [(i[0]+npy)%sizey, (i[1]+npx)%sizex]
                if rmap[i[0]][i[1]] == "#" or rmap[i[0]][i[1]] == "+":
                    i = [(i[0]-npy)%sizey, (i[1]-npx)%sizex] # cofanie o 1
                if enemies_heads(rmap[i[0]][i[1]][0]) != "-":
                    walka(i[0], i[1], Baner[1])
                    Baner[2] -= 1
            else:
                moved = 0
        elif imput == "?":
            moved = 0
            pomoc()
        elif imput == ">":
            if rmap[npy][npx][0] == ">":
                echo = "Zszedłeś w dół przez jednokierunkowe drzwi:"
                py, px = 0, 0
                depth += 1
                makemap()
                rmap, vmap = testpokoj(rmap, vmap, [py, px])
            else:
                moved = 0
        elif imput == "<":
            if rmap[npy][npx][0] == "<":
                echo = "Wszedłeś do góry przez jednokierunkowe drzwi:"
                py, px = 0, 0
                depth -= 1
                makemap()
                rmap, vmap = testpokoj(rmap, vmap, [py, px])
            else:
                moved = 0
        elif imput == "r":
            moved = 0
            if hp < mhp:
                if test_enemies(px, py, sizex, sizey, rmap) == 9:
                    pochotime -= 10
                    hp += 1
                    time += 10
                    echo = "Odpocząłeś 10 tur:"
                else:
                    echo = "Nie możesz tu odpocząć:"
            else:
                echo = "Nie musisz odpoczywać:"
        elif imput == "q":
            moved = 0
            if test_enemies(px, py, sizex, sizey, rmap) == 9:
                if (pochotime < 25 or  pochodnia == 0) and rmap[py][px] != ".":
                    echo = "Posiadasz za mało światła:"
                else:
                    out()
                    print("Wybierz kierunek kopania (zajmuje to 10 tur):")
                    try:
                        pm = pmover(str(int(takein())))
                    except:
                        pm = "11"
                    npy = int(pm[0])-1
                    npx = int(pm[1])-1 
                    npy, npx = (py+npy)%sizey, (px+npx)%sizex
                    if rmap[npy][npx] == "#":
                        rmap[npy][npx] = "."
                        vmap[npy][npx] = "."
                        echo = "Wykopałes tunel:"
                        pochotime -= 10
                        time += 10
                    else:
                        echo = "Nie możesz tu kopać:"
            else:
                echo = "Wróg w pobliżu:"
        elif imput == "s":
            sort()
            moved = 0
        else:
               moved = 0
               echo = "?:"
    else:
        # -------------------------------- number input
        npy = (py + int(pm[0]) -1) % sizey
        npx = (px + int(pm[1]) -1) % sizex
        p, np = [py, px], [npy, npx]
        np, gold, echo, moved = terrain(rmap, vmap, p, np, gold, Baner, Backpack, pm)
        py, px = np
        rmap, vmap = testpokoj(rmap, vmap, [py, px])
        # new----------------------------------------------
        if rmap[npy][npx] == ":":
            if randint(0, 4) == 0:
                rmap[npy][npx] = "."
                vmap[npy][npx] = "."
                echo = "Rozwaliłeś przeszkodę i wpadasz do środka:"
                py = npy
                px = npx
            else:
                echo = "Uderzyłeś w przeszkodę:"
        if echo == "?":
            walka(npy, npx, atak)
    
    if moved == 1:
        time += 1
        if pochodnia == 1:
            pochotime -= 1
            if pochotime < 0:
                pochodnia = 0
        while pd >= lw * (lw + 4):
            lw += 1
            mhp += 5
            hp += 5
        wasattackby = ""
        for y in range(-1, 2):
            for x in range(-1, 2):
                bonus = 0
                i = [(py+y) % sizey, (px+x) % sizex]
                k = enemies_heads(rmap[i[0]][i[1]][0])
                if k != "-":
                    if randint(0, 1) == 0:
                        wasattackby += rmap[i[0]][i[1]][0]
                        bonus = enemies_attack(k)
                if bonus != 0:
                    bonus += randint(randint((1-bonus)//2, 0), 
                                     randint(0, (bonus-1)//2))
                if bonus > zbroja:
                    hp += zbroja - bonus
        for y in range(-2, 3):
            for x in range(-2, 3):
                if y > 1 or y < -1 or x > 1 or x < -1:
                    i = [(py+y) % sizey, (px+x) % sizex]
                    if enemies_heads(rmap[i[0]][i[1]][0]) != "-":
                        i = [i[0], i[1], (i[0]+randint(-1, 1)) % sizey, (i[1]+randint(-1, 1)) % sizex, rmap[i[0]][i[1]][:4], rmap[i[0]][i[1]][4:]]
                        # i = [sy, sx, ny, nx, wrog, s.teren]
                        if rmap[i[2]][i[3]][0] == " " or rmap[i[2]][i[3]][0] == "." or rmap[i[2]][i[3]][0] == ", ":
                            rmap[i[2]][i[3]] = i[4] + rmap[i[2]][i[3]]
                            if i[5] != " ":
                                vmap[i[2]][i[3]] = rmap[i[2]][i[3]]
                            rmap[i[0]][i[1]] = i[5]
                            vmap[i[0]][i[1]] = rmap[i[0]][i[1]]
                        elif rmap[i[0]][i[1]][1] == " " or rmap[i[0]][i[1]][1] == "_":
                            vmap[i[0]][i[1]] = " "
        
        
        if hp == mhp:
            licznik = 0
        else:
            licznik += 1
            if licznik > 10:
                licznik -= 10
                hp += 1
        if hp > mhp:
            hp = mhp
        if hp <= 0:
            break
i = pd + atak + zbroja + Baner[1] + 5 * len(Backpack) + mhp + 10 * (lw + depth)
with open(path+'Wyniki.pyg', 'a') as wynik:
    wynik.write(str(i)+"|"+name+"|"+playerdata[0]+" "+playerdata[1]+"|"+str(time)+"|"+str(lw)+"|"+str(depth)+"|R|"+str(Backpack)+"\n")
out()
input(playerdata[0]+" "+playerdata[1]+" "+str(i)) + " time:" + str(time) + ":"
input("""




               _______________________
              /                       \         ___
             /                         \ ___   /   \      ___
            /            RIP            \   \  :   :     /   \ 
           /                             \  : _;, , , ;_    :   :
          /                               \, ;_          _;, , , ;_
         |               the               |   ___
         |               YOU               |  /   \ 
         |                                 |  :   :
         |                                 | _;, , , ;_   ____
         |            Level : n            |          /    \ 
         |                                 |          :    :
         |                                 |          :    :
         |        Died on Level : k        |         _;, , , , ;_
         |            killed by            |
         |              Pycha              |
         |                                 |
        *|   *     *     *    *   *     *  | *
________)/\\_)_/___(\/___(//_\)/_\//__\\(/_|_)_______""")
printwynik(path)
