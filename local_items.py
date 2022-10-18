ilist = []
def items_init(path, poziom):
    global ilist
    ilist = [["kastet [2]"], ["sling {2}"], ["futro (1)"]]
    for _ in range(9):
        ilist[0].append("nóż [3]")
    for _ in range(7):
        ilist[0].append("sztylet [4]")
    for _ in range(6):
        ilist[0].append("mały miecz [5]")
    i = poziom
    for _ in range(i-4):
        ilist[0].append("mace [7]")
        ilist[1].append("bow {3}")
    for _ in range(i-9):
        ilist[0].append("spear [10]")
        ilist[1].append("crosbow {5}")
        ilist[2].append("cloack (2)")
    for _ in range(i-14):
        ilist[0].append("sword [14]")
        ilist[2].append("cloack (3)")
    for _ in range(i-19):
        ilist[0].append("glaive [17]")
        ilist[1].append("manshimex {8}")
        ilist[2].append("cloack (4)")
    return(len(ilist[0]), len(ilist[1]), len(ilist[2]))


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
