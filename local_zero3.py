def zero3(i):
    i = str(i)
    while len(i) < 3:
        i = "0" + i
    return i
#print(zero3(99))
#print([0,1,2][3:])