from random import randint
from local_zero3 import zero3

ilist = []
def items_init(path, depth):
    global ilist
    with open(str(path) + str(depth) +"_depth_items.txt") as I:
        ilist = I.read().split("\n")
    print(ilist)
    if ilist[-1] == "":
        ilist.pop(-1)
    print(ilist)
    for i in range(3):
       ilist[i] = ilist[i].split(";")
    print(ilist)
    j = []
    for i in range(3,len(ilist)-1):
        ilist[i] = ilist[i].split(" ")
        if int(ilist[i][3]) > randint(0,99):
            j.append(ilist[i][0]+zero3(str(randint(int(ilist[i][1]),int(ilist[i][2])))))
    i = ilist[-1].split(" ")
    print(j)
    return([j, int(i[0]), int(i[1]), int(i[2]), int(i[3])])


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
