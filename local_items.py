from random import randint
from local_zero3 import zero3

ilist = []
def items_init(path, depth, p_data):
    global ilist
    with open(str(path) + str(depth) +"_depth.txt") as I:
        ilist = I.read().split("\n")
    if ilist[-1] == "":
        ilist.pop(-1)
    j = []
    if p_data == "Warrior" and randint(0, 2) == 0: # help for warriors -PR-
        j.append("~000")
    if p_data == "Warrior" and randint(0, 2) == 0:
        j.append("?000")
    for i in range(len(ilist)-1):
        ilist[i] = ilist[i].split(" ")
        for _ in range(int(ilist[i][4])):
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

    return([j, int(k[0]), int(k[1]), int(k[2]), int(k[3]), int(k[4])])


def weapon(i):
    global ilist
    return(ilist[0][i])

def putter(i):
    global ilist
    return(ilist[1][i])

def armor(i):
    global ilist
    return(ilist[2][i])
