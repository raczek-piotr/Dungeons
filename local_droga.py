from galwana import galwana
from random import randint

from local_enemies import enemies_heads

def makedroga(sizey,sizex,sciana,podloga,jpodloga,drzwi,zdrzwi,items,ile = 25,minilosc = 10):
    ile -= 1
    mmap = [[sciana for _ in range(sizex)] for _ in range(sizey)]
    pokoje = [[0,0,randint(3,5)/2,randint(3,5)/2]]
    pokoje[0][0] = randint(1,sizey-2 - 2 * pokoje[0][2])
    pokoje[0][1] = randint(1,sizex-2 - 2 * pokoje[0][3])
    proby = 0
    print(sizey,sizex)
    while len(pokoje) < minilosc or proby < ile:
        sy,sx = randint(3,5)/2,randint(3,5)/2
        y,x = randint(1,sizey-2 - 2 * sy),randint(1,sizex-2 - 2 * sx)
        can, proby = True, proby + 1
        for i in pokoje:
            if abs((i[0]+i[2])-(y+sy))<i[2]+sy+1 and abs((i[1]+i[3])-(x+sx))<i[3]+sx+1:
                can = False
        if can:
            pokoje.append([y,x,sy,sx,0])
            continue
    for i in range(len(pokoje)):
        pokoje[i][2] = int(2*pokoje[i][2])
        pokoje[i][3] = int(2*pokoje[i][3])
    for i in range(len(pokoje)):
        j = [galwana(pokoje[i][0],sizey),galwana(pokoje[i][1],sizex),pokoje[i][2],pokoje[i][3]]
        for y in range(j[0]-1,j[0]+j[2]+1):
            for x in range(j[1]-1,j[1]+j[3]+1):
                mmap[y][x] = "|"
        for y in range(j[0],j[0]+j[2]):
            for x in range(j[1],j[1]+j[3]):
                mmap[y][x] = jpodloga+"."
    pokoje[0].append(-1)
    mmap = polacz(mmap,sizey,sizex,pokoje,2)
    for i in range(sizey):
        for j in range(sizex):
            if mmap[i][j] == "|":
                mmap[i][j] = "#"
    i = randint(1,len(pokoje)-2)
    for k in items:
        while mmap[pokoje[i][0]+randint(1,pokoje[i][2]-1)][pokoje[i][1]+randint(1,pokoje[i][3]-1)] != "_.":
            i = randint(1,len(pokoje)-2)
        mmap[pokoje[i][0]+randint(1,pokoje[i][2]-1)][pokoje[i][1]+randint(1,pokoje[i][3]-1)] = jpodloga+k+"."
        print(jpodloga+k+".",end = "| ")
    if enemies_heads("B") != "-":
        mmap[pokoje[-1][0]+pokoje[-1][2]//2][pokoje[-1][1]+pokoje[-1][3]//2] = "_=>."
    else:
        mmap[pokoje[-1][0]+pokoje[-1][2]//2][pokoje[-1][1]+pokoje[-1][3]//2] = "_>."
    print(len(pokoje),pokoje[0][0]+pokoje[0][2]//2,pokoje[0][1]+pokoje[0][3]//2)
    return(mmap,pokoje[0][0]+pokoje[0][2]//2,pokoje[0][1]+pokoje[0][3]//2)
        #rmap[i[0]+randint(1-sy,sy-1)][i[1]+randint(1-sx,sx-1)] = item
def polacz(mmap,sizey,sizex,pokoje,l):
    pokojen = []
    for i in pokoje:
        pokojen.append(i)
    pokojeok = [pokojen.pop(1)]
    kier = 0
    while pokojen != []:
        n_minodl = 0
        o_minodl = 0
        minodl = sizey**2 + sizex**2
        for id_n in range(len(pokojen)):
            n = pokojen[id_n]
            modl = sizey**2 + sizex**2
            o_modl = -1
            for id_o in range(len(pokojeok)):
                o = pokojeok[id_o]
                odl = (n[0]-n[2]/2-o[0]+o[2]/2)**2 + (n[1]-n[3]/2-o[1]+o[3]/2)**2
                if odl < modl:
                    modl = odl
                    o_modl = id_o
            if modl < minodl:
                minodl = modl
                n_minodl = id_n
                o_minodl = o_modl
        p2 = pokojeok[o_minodl]
        cel = [p2[0]+p2[2]//2,p2[1]+p2[3]//2]
        p1 = pokojen[n_minodl]
        pokojeok.append(pokojen.pop(n_minodl))
        y,x, = p1[0]+p1[2]//2,p1[1]+p1[3]//2
        j = [galwana(p1[0],sizey),galwana(p1[1],sizex),p1[2],p1[3]]
        goal = True
        while goal:
            if kier == 0:
                if y < cel[0]:
                    k = (y+1)%sizey
                    if mmap[y][x] == " " or mmap[y+1][x] == " " or mmap[y-1][x] == " " or mmap[y][x+1] == " " or mmap[y-1][x] == " ":
                        goal = False
                    if mmap[y][x] == "|":
                        mmap[y][x] = "+"
                    elif mmap[y][x] == "#":
                        mmap[y][x] = "d"
                    y = k
                kier = kier+2%4
            elif kier == 1:
                if y > cel[0]:
                    k = (y-1)%sizey
                    if mmap[y][x] == " " or mmap[y+1][x] == " " or mmap[y-1][x] == " " or mmap[y][x+1] == " " or mmap[y-1][x] == " ":
                        goal = False
                    if mmap[y][x] == "|":
                        mmap[y][x] = "+"
                    elif mmap[y][x] == "#":
                        mmap[y][x] = "d"
                    y = k
                kier = kier+2%4
            elif kier == 2:
                if x < cel[1]:
                    k = (x+1)%sizex
                    if mmap[y][x] == " " or mmap[y+1][x] == " " or mmap[y-1][x] == " " or mmap[y][x+1] == " " or mmap[y-1][x] == " ":
                        goal = False
                    if mmap[y][x] == "|":
                        mmap[y][x] = "+"
                    elif mmap[y][x] == "#":
                        mmap[y][x] = "d"
                    x = k
                kier = kier+2%4
            else:
                if x > cel[1]:
                    k = (x-1)%sizex
                    if mmap[y][x] == " " or mmap[y+1][x] == " " or mmap[y-1][x] == " " or mmap[y][x+1] == " " or mmap[y-1][x] == " ":
                        goal = False
                    if mmap[y][x] == "|":
                        mmap[y][x] = "+"
                    elif mmap[y][x] == "#":
                        mmap[y][x] = "d"
                    x = k
                kier = kier+2%4
            if y == cel[0] and x == cel[1]:
                goal = False
            if randint(0,9) == 0:
                kier = randint(0,4)
        for i in range(sizey):
            for j in range(sizex):
                if mmap[i][j] == "d":
                    mmap[i][j] = " "
    return(mmap)

def open_doors(rmap,vmap):
    for y in range(len(rmap)):
        for x in range(len(rmap[0])):
            if rmap[y][x][0] == "=":
                rmap[y][x] = rmap[y][x][1:]
                vmap[y][x] = rmap[y][x]
            else:
                if len(rmap[y][x]) > 1 and rmap[y][x][1] == "=":
                    rmap[y][x] = rmap[y][x][0] + rmap[y][x][2:]
