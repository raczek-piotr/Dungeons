from random import randint
from local_zero3 import zero3

ilist = []
def items_init(path, depth):
    global ilist
    with open(str(path) + str(depth) +"_depth.txt") as I:
        ilist = I.read().split("\n")
    if ilist[-1] == "":
        ilist.pop(-1)
    j = []
    for i in range(len(ilist)-1):
        ilist[i] = ilist[i].split(" ")
        if int(ilist[i][3]) > randint(0,99):
            j.append(ilist[i][0]+zero3(str(randint(int(ilist[i][1]),int(ilist[i][2])))))
    k = ilist[-1].split(" ")

    depth = "s" + str((depth+4)//5)
    with open(str(path) + str(depth) +"_depth_items.txt") as I:
        ilist = I.read().split("\n")
    if ilist[-1] == "":
        ilist.pop(-1)
    for i in range(len(ilist)):
        ilist[i] = ilist[i].split(";")

    return([j, int(k[0]), int(k[1]), int(k[2]), int(k[3])])


def weapon(i):
    global ilist
    try:
        return(ilist[0][i])
    except:
        return("meniek [5]")

def putter(i):
    global ilist
    try:
        return(ilist[1][i])
    except:
        return("meniek {3}")

def armor(i):
    global ilist
    try:
        return(ilist[2][i])
    except:
        return("meniek (1)")
