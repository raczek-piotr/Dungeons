from local_translator import translate

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
    
def dpos(y,hp,mhp,pd,lw,gold,poziom,atak,zbroja,wasattackby,Backpack,Baner):
    dposout = {
        1: "  hp: " + str(hp) + "/" + str(mhp),
        2: "  xp: " + str(pd),
        3: "  lw: " + str(lw),
        5: "  depth: " + str(poziom),
        4: "  gold: " + str(gold),
        6: "  attack: " + str(atak),
        7: "  armor: " + str(zbroja),
        9: "      orantium:" + str(Baner[0]),
        10: " range attack: " + str(Baner[1]),
        11: "       arrows: " + str(Baner[2]),
        13: "------Backpack:------",
        14: printBackpack(Backpack,0),
        15: printBackpack(Backpack,1),
        16: printBackpack(Backpack,2),
        17: printBackpack(Backpack,3),
        18: printBackpack(Backpack,4),
        19: printBackpack(Backpack,5),
        21: "attack by: " + wasattackby,
        }
    print("|" + dposout.get(y, "---------------------"))
