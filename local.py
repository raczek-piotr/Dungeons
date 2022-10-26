from local_translator import translate

# local mmap
from random import randint
ex_tlist = [".",","," ","_","]","}",")","~","-","!","?","<",">", "r", "b", "B", "S", "t", "`"]
tlist = [".",","," ","_","]","}",")","~","-","!","?","<",">"]
mmap = []
def mmap_init(rmap, p1, h = 5):
    print(h)
    global ex_tlist, mmap
    sizey, sizex = len(rmap), len(rmap[0])
    mmap = [[-1 for _ in range(sizey)] for _ in range(sizex)]
    w, k = p1[0], p1[1]
    q = [[w, k, 0]]
    while q != []:
        p1 = q.pop(0)
        if p1[2] <= h:
            w, k = p1[0], p1[1]
            if (rmap[w][k][0] in ex_tlist) and mmap[w][k] == -1:
                q.append([w, k, p1[2] + 1])
                mmap[w][k] = p1[2] + 1
            if (rmap[w-1][k][0] in ex_tlist) and mmap[w-1][k] == -1:
                q.append([w-1, k, p1[2] + 1])
                mmap[w-1][k] = p1[2] + 1
            if (rmap[w+1][k][0] in ex_tlist) and mmap[w+1][k] == -1:
                q.append([w+1, k, p1[2] + 1])
                mmap[w+1][k] = p1[2] + 1
            if (rmap[w][k-1][0] in ex_tlist) and mmap[w][k-1] == -1:
                q.append([w, k-1, p1[2] + 1])
                mmap[w][k-1] = p1[2] + 1
            if (rmap[w][k+1][0] in ex_tlist) and mmap[w][k+1] == -1:
                q.append([w, k+1, p1[2] + 1])
                mmap[w][k+1] = p1[2] + 1

            if (rmap[w-1][k-1][0] in ex_tlist) and mmap[w-1][k-1] == -1:
                q.append([w-1, k-1, p1[2] + 1])
                mmap[w-1][k-1] = p1[2] + 1
            if (rmap[w+1][k-1][0] in ex_tlist) and mmap[w+1][k-1] == -1:
                q.append([w+1, k-1, p1[2] + 1])
                mmap[w+1][k-1] = p1[2] + 1
            if (rmap[w-1][k+1][0] in ex_tlist) and mmap[w-1][k+1] == -1:
                q.append([w-1, k+1, p1[2] + 1])
                mmap[w-1][k+1] = p1[2] + 1
            if (rmap[w+1][k+1][0] in ex_tlist) and mmap[w+1][k+1] == -1:
                q.append([w+1, k+1, p1[2] + 1])
                mmap[w+1][k+1] = p1[2] + 1
def direction_mmap(p1):
    global mmap
    t_mmap = [[mmap[p1[0]-1][p1[1]-1], p1[0]-1, p1[1]-1],
              [mmap[p1[0]-1][p1[1]], p1[0]-1, p1[1]],
              [mmap[p1[0]-1][p1[1]+1], p1[0]-1, p1[1]+1],
              [mmap[p1[0]][p1[1]-1], p1[0], p1[1]-1],
              [mmap[p1[0]][p1[1]], p1[0], p1[1]],
              [mmap[p1[0]][p1[1]+1], p1[0], p1[1]+1],
              [mmap[p1[0]+1][p1[1]-1], p1[0]+1, p1[1]-1],
              [mmap[p1[0]+1][p1[1]], p1[0]+1, p1[1]],
              [mmap[p1[0]+1][p1[1]+1], p1[0]+1, p1[1]+1],
              ]
    # t_mmap = [[mmap[p1[0]-1][p1[1]-1], p1[0]+1, p1[1]+1],
    #           [mmap[p1[0]-1][p1[1]], p1[0]+1, p1[1]],
    #           [mmap[p1[0]-1][p1[1]+1], p1[0]+1, p1[1]-1],
    #           [mmap[p1[0]][p1[1]-1], p1[0], p1[1]+1],
    #           [mmap[p1[0]][p1[1]], p1[0], p1[1]],
    #           [mmap[p1[0]][p1[1]+1], p1[0], p1[1]-1],
    #           [mmap[p1[0]+1][p1[1]-1], p1[0]-1, p1[1]+1],
    #           [mmap[p1[0]+1][p1[1]], p1[0]-1, p1[1]],
    #           [mmap[p1[0]+1][p1[1]+1], p1[0]-1, p1[1]-1],
    #           ]
    p_min = mmap[p1[0]][p1[1]]
    direction = t_mmap[4]

    while t_mmap != []:
        i = t_mmap.pop(randint(0, len(t_mmap)-1))
        if i[0] > 0 and i[0] <= p_min:
            p_min = i[0]
            direction = [i[1], i[2]]
    return direction
def move_mmap(rmap, vmap, sizey, sizex, j):
    global mmap
    i = [j[0], j[1]]
    i = [i[0], i[1], i[0], i[1], rmap[i[0]][i[1]][:4], rmap[i[0]][i[1]][4:]]
    # i = [sy, sx, ny, nx, wrog, s.teren]
    i[2], i[3] = direction_mmap(j)
    if rmap[i[2]][i[3]][0] in tlist:
        rmap[i[2]][i[3]] = i[4] + rmap[i[2]][i[3]]
        if rmap[i[2]][i[3]][-1] != " ":
            vmap[i[2]][i[3]] = rmap[i[2]][i[3]]
        if i[5] == "":
            i[5] = " "
        rmap[i[0]][i[1]] = i[5]
        if rmap[i[0]][i[1]][-1] != " ":
            vmap[i[0]][i[1]] = rmap[i[0]][i[1]]
    elif len(rmap[i[0]][i[1]]) > 1 and (rmap[i[0]][i[1]][1] == " " or rmap[i[0]][i[1]][1] == "_"):
        vmap[i[0]][i[1]] = " "
    return mmap
def number_mmap(p1):
    global mmap
    try:
        return mmap[p1[0]][p1[1]]
    except:
        return 0
def return_mmap():
    global mmap
    return mmap
# end of local_mmap

def printBackpack(Backpack,arg):
    try:
        if Backpack[arg][-1] in ["]","}",")"]:
            return(translate(str(Backpack[arg][:-5])))+str(Backpack[arg][-5:])
        return(translate(str(Backpack[arg])))
    except:
        pass
    return("")

def pmover(pv):
    switcher = {
        "1": "20",
        "2": "21",
        "3": "22",
        "4": "10",
        "5": "11",
        "6": "12",
        "7": "00",
        "8": "01",
        "9": "02",
        }
    return switcher.get(pv, "q")
    
def dpos(y, player_data, hp, mhp, xp, lw, gold, poziom, atak, zbroja, wasattackby, Backpack, Baner):
    match y:
        case 1:
            return " " + player_data[0] + " " + player_data[1]
        case 3:
            return " hp: " + str(hp) + "/" + str(mhp)
        case 4:
            return " xp: " + str(xp)
        case 5:
            return " lw: " + str(lw)
        case 6:
            return " depth: " + str(poziom)
        case 7:
            return " attack: " + str(atak)
        case 8:
            return " armor: " + str(zbroja)
        case 9:
            return " gold: " + str(gold)
        case 11:
            return "         mana: " + str(Baner[0][0]) + "/" + str(Baner[0][1])
        case 12:
            return " range attack: " + str(Baner[1])
        case 13:
            return "   amuniction: " + str(Baner[2])
        case 15:
            return " " + printBackpack(Backpack, 0)
        case 16:
            return " " + printBackpack(Backpack, 1)
        case 17:
            return " " + printBackpack(Backpack, 2)
        case 18:
            return " " + printBackpack(Backpack, 3)
        case 19:
            return " " + printBackpack(Backpack, 4)
        case 20:
            return " " + printBackpack(Backpack, 5)
        case 22:
            return " attack by: " + wasattackby
        case _:
            return "=----------------------="

