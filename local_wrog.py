def testwrog(px,py,sizex,sizey,rmap):
    i = [(py+2)%sizey,(px+2)%sizex,0]
    for y in range(i[0]-3,i[0]):
        for x in range(i[1]-3,i[1]):
            if rmap[y][x][0] != "s" and rmap[y][x][0] != "g" and rmap[y][x][0] != "b" and rmap[y][x][0] != "i":
                i[2] += 1
    return(i[2])