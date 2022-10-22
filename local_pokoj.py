from galwana import galwana

def test_room(rmap,vmap,p1):
    sizey = len(rmap)
    sizex = len(rmap[0])
    w,k = galwana(p1[0],sizey),galwana(p1[1],sizex)
    q = []
    if rmap[w-1][k][0] == "_":
        q.append([w-1,k])
        rmap[w-1][k] = rmap[w-1][k][1:]
    if rmap[w+1][k][0] == "_":
        q.append([w+1,k])
        rmap[w+1][k] = rmap[w+1][k][1:]
    if rmap[w][k-1][0] == "_":
        q.append([w,k-1])
        rmap[w][k-1] = rmap[w][k-1][1:]
    if rmap[w][k+1][0] == "_":
        q.append([w,k+1])
        rmap[w][k+1] = rmap[w][k+1][1:]

    if rmap[w-1][k-1][0] == "_":
        q.append([w-1,k-1])
        rmap[w-1][k-1] = rmap[w-1][k-1][1:]
    if rmap[w+1][k-1][0] == "_":
        q.append([w+1,k-1])
        rmap[w+1][k-1] = rmap[w+1][k-1][1:]
    if rmap[w-1][k+1][0] == "_":
        q.append([w-1,k+1])
        rmap[w-1][k+1] = rmap[w-1][k+1][1:]
    if rmap[w+1][k+1][0] == "_":
        q.append([w+1,k+1])
        rmap[w+1][k+1] = rmap[w+1][k+1][1:]
    while q != []:
        p1 = q.pop(0)
        w,k = galwana(p1[0],sizey),galwana(p1[1],sizex)
        if rmap[w-1][k][0] == "_":
            q.append([w-1,k])
            rmap[w-1][k] = rmap[w-1][k][1:]
        if rmap[w+1][k][0] == "_":
            q.append([w+1,k])
            rmap[w+1][k] = rmap[w+1][k][1:]
        if rmap[w][k-1][0] == "_":
            q.append([w,k-1])
            rmap[w][k-1] = rmap[w][k-1][1:]
        if rmap[w][k+1][0] == "_":
            q.append([w,k+1])
            rmap[w][k+1] = rmap[w][k+1][1:]
        for i in range(w-1,w+2):
            for j in range(k-1,k+2):
                vmap[i][j] = rmap[i][j]
