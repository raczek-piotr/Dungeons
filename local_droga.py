from galwana import galwana
from random import randint

def makedroga(depth, sizey,sizex,sciana,podloga,jpodloga,drzwi,zdrzwi,items,ile = 25,minilosc = 10):
    ile -= 1
    mmap = [[sciana for _ in range(sizex)] for _ in range(sizey)]
    pokoje = [[0,0,randint(3,5)/2,randint(3,5)/2]]
    pokoje[0][0] = randint(1,sizey-2 - 2 * pokoje[0][2])
    pokoje[0][1] = randint(1,sizex-2 - 2 * pokoje[0][3])
    proby = 0
    while len(pokoje) < minilosc or proby < ile:
        sy,sx = randint(3,5)/2,randint(3,5)/2
        y,x = randint(1,sizey-2 - 2 * sy),randint(1,sizex-2 - 2 * sx)
        can, proby = True, proby + 1
        for i in pokoje:
            if ((abs((i[0]+i[2])-(y+sy))<i[2]+sy+1 and
                 abs((i[1]+i[3])-(x+sx))<i[3]+sx+1) or
                 abs((i[0]+i[2])-(y+sy))==i[2]+sy+2 or
                 abs((i[1]+i[3])-(x+sx))==i[3]+sx+2):
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
    start_points(mmap,sizey,sizex,pokoje,2)
    for i in range(sizey):
        for j in range(sizex):
            if mmap[i][j] == "|":
                mmap[i][j] = "#"
    i = randint(1,len(pokoje)-2)
    for k in items:
        while mmap[pokoje[i][0]+randint(1,pokoje[i][2]-1)][pokoje[i][1]+randint(1,pokoje[i][3]-1)] != "_.":
            i = randint(1,len(pokoje)-2)
        mmap[pokoje[i][0]+randint(1,pokoje[i][2]-1)][pokoje[i][1]+randint(1,pokoje[i][3]-1)] = jpodloga+k+"."
    if depth % 5 == 0:
        mmap[pokoje[-1][0]+pokoje[-1][2]//2][pokoje[-1][1]+pokoje[-1][3]//2] = "_=>."
    else:
        mmap[pokoje[-1][0]+pokoje[-1][2]//2][pokoje[-1][1]+pokoje[-1][3]//2] = "_>."
    return(mmap,pokoje[0][0]+pokoje[0][2]//2,pokoje[0][1]+pokoje[0][3]//2)
        #rmap[i[0]+randint(1-sy,sy-1)][i[1]+randint(1-sx,sx-1)] = item
def start_points(mmap, sizey, sizex, pokoje, l):
    pokojen = []
    for i in pokoje:
        pokojen.append(i)
    pokojeok = [pokojen.pop(1)]
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
        p2 = [p2[0]+p2[2]//2,p2[1]+p2[3]//2]
        p1 = pokojen[n_minodl]
        p1 = [p1[0]+p1[2]//2,p1[1]+p1[3]//2]
        middle2 = [(p1[0]+p2[0])//2,(p1[1]+p2[1])//2]
        middle1 = [(p1[0]+p2[0])//2,(p1[1]+p2[1])//2]
        connect(mmap, sizey, sizex, p2, middle2)
        connect(mmap, sizey, sizex, p1, middle1, True)
        pokojeok.append(pokojen.pop(n_minodl))

def connect(mmap, sizey, sizex, p_end, p_start, clear = False):
    kier = 0
    goal = True
    while goal:
        if kier == 0:
            if p_start[0] < p_end[0]:
                k = (p_start[0]+1)%sizey
            elif p_start[0] > p_end[0]:
                k = (p_start[0]-1)%sizey
            else:
                k = p_start[0]
                kier += 1
            p_start[0], p_start[1] = galwana(p_start[0],sizey), galwana(p_start[1],sizex)
            if mmap[p_start[0]][p_start[1]] == "|" or mmap[p_start[0]][p_start[1]] == " " or mmap[p_start[0]+1][p_start[1]] == " " or mmap[p_start[0]-1][p_start[1]] == " " or mmap[p_start[0]][p_start[1]+1] == " " or mmap[p_start[0]-1][p_start[1]] == " ":
                goal = False
            if mmap[p_start[0]][p_start[1]] == "|":
                mmap[p_start[0]][p_start[1]] = "+"
            elif mmap[p_start[0]][p_start[1]] == "#":
                mmap[p_start[0]][p_start[1]] = "d"
            p_start[0] = k
            kier = kier+2%4
        else:
            if p_start[1] < p_end[1]:
                k = (p_start[1]+1)%sizex
            elif p_start[1] > p_end[1]:
                k = (p_start[1]-1)%sizex
            else:
                k = p_start[1]
                kier -= 1
            p_start[0], p_start[1] = galwana(p_start[0],sizey), galwana(p_start[1],sizex)
            if mmap[p_start[0]][p_start[1]] == "|" or mmap[p_start[0]][p_start[1]] == " " or mmap[p_start[0]+1][p_start[1]] == " " or mmap[p_start[0]-1][p_start[1]] == " " or mmap[p_start[0]][p_start[1]+1] == " " or mmap[p_start[0]-1][p_start[1]] == " ":
                goal = False
            if mmap[p_start[0]][p_start[1]] == "|":
                mmap[p_start[0]][p_start[1]] = "+"
            elif mmap[p_start[0]][p_start[1]] == "#":
                mmap[p_start[0]][p_start[1]] = "d"
            p_start[1] = k
            kier = kier+2%4
        if p_start[0] == p_end[0] and p_start[1] == p_end[1]:
            goal = False
        if randint(0,99) < 20:
            kier = (kier+1)%2
    if clear:
        for i in range(sizey):
            for j in range(sizex):
                if mmap[i][j] == "d":
                    mmap[i][j] = " "

def open_doors(rmap,vmap):
    for y in range(len(rmap)):
        for x in range(len(rmap[0])):
            if rmap[y][x][0] == "=":
                rmap[y][x] = rmap[y][x][1:]
                vmap[y][x] = rmap[y][x]
            else:
                if len(rmap[y][x]) > 1 and rmap[y][x][1] == "=":
                    rmap[y][x] = rmap[y][x][0] + rmap[y][x][2:]
