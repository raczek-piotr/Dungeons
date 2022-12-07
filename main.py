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

path = 'data/'

def takein():
    global enable_windows_stuff
    if enable_windows_stuff:
        return str(getch())[2]
    return getch()

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
    return(atak, miotacz, zbroja, "")

def attack_enemies(y, x, atak, chance = 60):
    global rmap, vmap, py, px, npy, npx, echo, pd
    atak += randint(randint((1-atak)//2, 0),
                    randint(0, (atak-1)//2))
    hp = int(rmap[y][x][1:4])
    k = enemies_heads(rmap[y][x][0])
    if k != "-":
        if randint(0, 99) < chance:
            if hp-atak <= 0:
                if rmap[y][x][0] == "B":
                    open_doors(rmap, vmap)
                rmap[y][x] = rmap[y][x][4:]
                vmap[y][x] = rmap[y][x]
                pd += enemies_xp(k)
                echo = translate("YOU KILL") + " " + translate("A MONSTER")
            else:
                rmap[y][x] = rmap[y][x][0] + zero3(hp-atak) + rmap[y][x][4:]
                echo = translate("YOU HIT") + " " + translate("A MONSTER") + " | " + str(atak) + " | " + str(hp-atak) + " |"
                if enemies_specials(k) != "-":
                    if "t" in enemies_specials(k):
                        t_m = rmap[y][x][:4]
                        if "p" in enemies_specials(k):
                            rmap[y][x] = "`001" + rmap[y][x][4:]
                        else:
                            rmap[y][x] = rmap[y][x][4:]
                        y, x = randint(3, sizey-4), randint(3, sizex-4)
                        while rmap[y][x] not in tlist:
                            y, x = randint(3, sizey-4), randint(3, sizex-4)
                        rmap[y][x] = t_m + rmap[y][x]
                        #
                        # bonus = 0
                        # i = 2
                        # if randint(0, 99) < player_atributs[1]:
                        #     bonus = enemies_attack(i)
                        # if bonus != 0:
                        #     bonus += randint(randint((1-bonus)//2, 0),
                        #                      randint(0, (bonus-1)//2))
                        # if bonus > zbroja:
                        #     hp += zbroja - bonus
        else:
            echo = translate("YOU MISS") + " " + translate("A MONSTER")

def wybierzpostac():
    player_atributs = [60, 50, 20, 5, 0, 0, 1]
    Baner = [[0, 0], 0, 8]
    player_data = []
    Backpack = []
    print("""                                DUNGEONS
                               CHOOSE A CHARACTER
    0 - human
    1 - halfling
    2 - hobbit
    """)
    i = takein()
    if i == "1":
        player_data = ["Halfling"]
        print("""
        0 - warrior
        1 - rogue
        2 - mage""")
        i = takein()
        if i == "1":
            player_atributs = [60, 40, 16, 4, 2, 75, 4]
            player_data.append("Rogue")
            Backpack = ["KNIFE [03]", "SLING {02}"]
            Baner[2] = 20
        elif i == "2":
            player_atributs = [60, 40, 12, 3, 5, 50, 6]
            player_data.append("Mage")
            Backpack = ["KNIFE [03]"]
            Baner[2] = 0
        else:
            player_atributs = [70, 40, 16, 4, 0, 0, 8]
            player_data.append("Warrior")
            Backpack = ["DAGGER [04]"]
    elif i == "2":
        player_data = ["Hobbit"]
        print("""
        0 - warrior
        1 - rogue
        2 - mage""")
        i = takein()
        if i == "1":
            player_atributs = [60, 30, 12, 3, 2, 75, 3]
            player_data.append("Rogue")
            Backpack = ["KNIFE [03]", "SLING {02}"]
            Baner[2] = 20
        elif i == "2":
            player_atributs = [60, 30, 8, 2, 5, 50, 4]
            player_data.append("Mage")
            Backpack = ["KNIFE [03]"]
            Baner[2] = 0
        else:
            player_atributs = [70, 30, 12, 3, 0, 0, 5]
            player_data.append("Warrior")
            Backpack = ["DAGGER [04]"]
    else:
        player_data = ["Human"]
        print("""
        0 - warrior
        1 - rogue
        2 - mage""")
        i = takein()
        if i == "1":
            player_atributs = [60, 50, 20, 5, 2, 75, 6]
            player_data.append("Rogue")
            Backpack = ["KNIFE [03]", "SLING {02}"]
            Baner[2] = 20
        elif i == "2":
            player_atributs = [60, 50, 16, 4, 5, 50, 8]
            player_data.append("Mage")
            Backpack = ["KNIFE [03]"]
            Baner[2] = 0
        else:
            player_atributs = [70, 50, 20, 5, 0, 0, 10]
            player_data.append("Warrior")
            Backpack = ["DAGGER [04]"]
    Backpack.append("TORCH")
    pd = 0
    vision = 1
    lw = 1
    depth = 1
    gold = 0
    pochodnia = 0
    pochotime = 0
    licznik = 0
    wasattackby = ""
    name = input("Your name (up to 17 letters): ")
    return(pd, vision, lw, depth, gold, pochodnia, pochotime, licznik, wasattackby, player_data, name, Backpack, Baner, player_atributs)

def makemap():
    global depth, rmap, vmap, omap, depth, sizey, sizex, py, px, echo
    j, sizey, sizex, maxp, minp, type_of_map = items_init(path, depth, player_data[1])
    enemies_init(path, depth)
    help_init(path, depth)
    rmap, py, px = makedroga(depth, sizey, sizex, j, maxp, minp, type_of_map)
    #rmap[py][px] = "<"

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
        print(i + "| " + dpos(y, player_data, hp, mhp, pd, lw, gold, depth, atak, zbroja, wasattackby, Backpack, Baner))


# X i Y
sizey = 0
sizex = 0
py = 0
px = 0
npy = py
npx = px
n_lw = 5

player_time = 0
#Backpack, mhp, hp, pd, vision, zbroja, lw, depth, gold, pochodnia, pochotime, licznik, wasattackby, player_data, name, atak, time, Baner = [], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 0, 0, 0, [[0, 0], 0, 0]
pd, vision, lw, depth, gold, pochodnia, pochotime, licznik, wasattackby, player_data, name, Backpack, Baner, player_atributs = wybierzpostac()
time, manatime = 0, 0
hp, mhp = player_atributs[2], player_atributs[2]
Baner[0][0], Baner[0][1] = player_atributs[4], player_atributs[4]
sort()

#depth = 6
#pd = 51

atak, Baner[1], zbroja, echo = wezbron()

makemap()
printwynik(path)
test_room(rmap, vmap, [py, px])
tlist = [".",","," ","_","]","}",")","~","-","!","?"]
while True:
    out()
    print(echo)
    #     -----move_p-----
    moved = 1
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
                        if player_data[1] == "Rogue":
                            pochotime += 50
                        echo = translate("YOU LIGHT A") + " " + translate(i,1) + ", " + translate("AND IT WILL GIVE YOU LIGHT FOR") + " " + str(pochotime) + " " + translate("TURNS")
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
                        attack_enemies(i[0], i[1], int(i[2][-2]), player_atributs[0])
            except:
                moved = 0
        elif imput == "-":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n    1 - MAGIC MORE LIGHT (1)\n    2 - HEAL SELF (SOME) (2)\n    3 - HEAL SELF + MAGIC MORE LIGHT(4)")
            k = takein()
            if k == "1" and Baner[0][0] >= 1:
                pochotime += 50
                pochodnia = 1
                echo = "YOU HAVE A MAGIC LIGHT"
                Baner[0][0] -= 1
            elif k == "2" and hp != mhp and Baner[0][0] >= 2:
                hp += (mhp-hp)//2
                echo = "YOU HAVE BEEN HEALED (SOME)"
                Baner[0][0] -= 2
            elif k == "3" and hp != mhp and Baner[0][0] >= 4:
                pochotime += 50
                pochodnia = 1
                hp = mhp
                echo = "YOU HAVE BEEN HEALED AND MORE LIGHT"
                Baner[0][0] -= 4
            else:
                moved = 0
                echo = "YOU CAN'T MAKE A SPELL"
        elif imput == "0":
            if Baner[2] > 0:
                out()
                print("Wybierz kierunek gdzie strzelisz")
                try:
                    pm = pmover(str(int(takein())))
                    npy = int(pm[0])-1
                    npx = int(pm[1])-1
                except:
                    moved = 0
                    continue
                i = [(py+npy) % sizey, (px+npx) % sizex]
                if pm != "11":
                    while rmap[i[0]][i[1]][0] in tlist:
                        i = [(i[0]+npy) % sizey, (i[1]+npx) % sizex]
                if rmap[i[0]][i[1]] == "#" or rmap[i[0]][i[1]] == "+":
                    i = [(i[0]-npy) % sizey, (i[1]-npx) % sizex] # cofanie o 1
                if enemies_heads(rmap[i[0]][i[1]][0]) != "-":
                    attack_enemies(i[0], i[1], Baner[1], player_atributs[0])
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
                test_room(rmap, vmap, [py, px])
            else:
                moved = 0
        elif imput == "<":
            if rmap[npy][npx][0] == "<":
                echo = "Wszedłeś do góry przez jednokierunkowe drzwi:"
                py, px = 0, 0
                depth -= 1
                makemap()
                test_room(rmap, vmap, [py, px])
            else:
                moved = 0
        elif imput == "r":
            if hp < mhp:
                if test_enemies(px, py, sizex, sizey, rmap) == 9:
                    pochotime -= 9
                    hp += 1
                    time += 9
                    manatime += 9
                    echo = "Odpocząłeś 10 tur:"
                else:
                    echo = "Nie możesz tu odpocząć:"
            else:
                echo = "Nie musisz odpoczywać:"
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
        test_room(rmap, vmap, [py, px])
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
            attack_enemies(npy, npx, atak, player_atributs[0])
    
    if moved == 1:
        time += 1
        if player_atributs[4] > Baner[0][0]:
            manatime += 1
            if manatime > player_atributs[5]:
                manatime = 0
                Baner[0][0] += 1
        else:
            manatime = 0
        if pochodnia == 1:
            pochotime -= 1
            if pochotime < 0:
                pochodnia = 0
        while pd >= n_lw:
            lw += 1
            n_lw = (lw + 4) * (lw + 5) * (2 * lw + 9) // 30 - 6 #((x+4)**2)//5
            mhp += player_atributs[3]
            hp += player_atributs[3]
        wasattackby = ""
        mmap_init(rmap, [py, px], player_atributs[6])
        mmap = []
        for y in range(-player_atributs[6],1+player_atributs[6]):
            if py+y >= 0 and py+y < sizey:
                for x in range(-player_atributs[6],1+player_atributs[6]):
                    if px+x >= 0 and px+x < sizex:
                        k = enemies_heads(rmap[(py+y) % sizey][(px+x) % sizex][0])
                        if k != "-":
                            mmap.append([y, x, k])
        while mmap != []:
            i = mmap.pop(randint(0,len(mmap)-1))
            k = number_mmap([py+i[0], px+i[1]])
            if k == 1:
                bonus = 0
                i = [py, px, i[2]]
                if randint(0, 99) < player_atributs[1]:
                    wasattackby += enemies_head(i[2])
                    bonus = enemies_attack(i[2])
                if bonus != 0:
                    bonus += randint(randint((1-bonus)//2, 0),
                                     randint(0, (bonus-1)//2))
                if bonus > zbroja:
                    hp += zbroja - bonus
            elif k > 0:
                move_mmap(rmap, vmap, sizey, sizex, [py+i[0], px+i[1]])
        
        for y in range(sizey):
            for x in range(sizex):
                if (enemies_heads(vmap[y][x][0]) != "-" and
                        enemies_heads(rmap[y][x][0]) != enemies_heads(vmap[y][x][0])):
                        vmap[y][x] = rmap[y][x]

            # for y in range(-2, 3):
            #     for x in range(-2, 3):
            #         if y > 1 or y < -1 or x > 1 or x < -1:
            #             i = [(py+y) % sizey, (px+x) % sizex]
            #             if enemies_heads(rmap[i[0]][i[1]][0]) != "-":
            #                 i = [i[0], i[1], (i[0]+randint(-1, 1)) % sizey, (i[1]+randint(-1, 1)) % sizex, rmap[i[0]][i[1]][:4], rmap[i[0]][i[1]][4:]]
            #                 # i = [sy, sx, ny, nx, wrog, s.teren]
            #                 if rmap[i[2]][i[3]][0] in tlist:
            #                     rmap[i[2]][i[3]] = i[4] + rmap[i[2]][i[3]]
            #                     if i[5] != " ":
            #                         vmap[i[2]][i[3]] = rmap[i[2]][i[3]]
            #                     rmap[i[0]][i[1]] = i[5]
            #                     vmap[i[0]][i[1]] = rmap[i[0]][i[1]]
            #                 elif rmap[i[0]][i[1]][1] == " " or rmap[i[0]][i[1]][1] == "_":
            #                     vmap[i[0]][i[1]] = " "


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
    wynik.write(str(i)+"|"+name+"|"+player_data[0]+" "+player_data[1]+"|"+str(time)+"|"+str(lw)+"|"+str(depth)+"|R|"+str(Backpack)+"\n")
out()
input(player_data[0]+" "+player_data[1]+" "+str(i)) + " time:" + str(time) + ":"
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