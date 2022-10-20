heads, attacks, xp = [], [], []
def enemies_init(path,depth):
    global heads, attacks, xp
    with open(str(path) + str(depth) +"_depth_enemies.txt") as I:
        elist = I.read().split("\n")
    if elist[-1] == "":
        elist.pop(-1)
    for i in range(len(elist)):
        elist[i] = elist[i].split(" ")
    heads = []
    for i in elist:
        heads.append(i[0])
    attacks = []
    for i in elist:
        attacks.append(i[1])
    xp = []
    for i in elist:
        xp.append(i[2])
    return([])
def enemies_heads(head):
    global heads
    for id in range(len(heads)):
        if heads[id] == head:
            return id
    return "-"
def enemies_attack(id):
    global attacks
    return int(attacks[id])
def enemies_xp(id):
    global xp
    return int(xp[id])
def enemies_head(id):
    global heads
    return heads[id]
def test_enemies(px,py,sizex,sizey,rmap):
    global heads
    i = [(py+2)%sizey,(px+2)%sizex,0]
    for y in range(i[0]-3,i[0]):
        for x in range(i[1]-3,i[1]):
            if rmap[y][x][0] in heads:
                pass
            else:
                i[2] += 1
    return(i[2])
