from local_translator import translate
from local_items import *

def f_gold(rmap, vmap, p, np, gold, baner, backpack, direction):
    npy, npx = np
    i = int(rmap[npy][npx][1:4])
    if direction == "11":
        rmap[npy][npx] = rmap[npy][npx][4:]
        vmap[npy][npx] = rmap[npy][npx]
        gold += i
        echo = translate("YOU TAKE")+" "+str(i)+" "+translate("GOLD", i)
    else:
        echo = translate("HERE IS")+" "+str(i)+" "+translate("GOLD", i)
    return [np, gold, echo, 1]

def f_arrows(rmap, vmap, p, np, gold, baner, backpack, direction):
    npy, npx = np
    i = int(rmap[npy][npx][1:4])
    if direction == "11":
        i = int(rmap[npy][npx][1:4])
        baner[2] += i
        echo = translate("YOU TAKE")+" "+str(i)+" "+translate("ARROWS", i)
        rmap[npy][npx] = rmap[npy][npx][4:]
        vmap[npy][npx] = rmap[npy][npx]
    else:
        i = int(rmap[npy][npx][1:4])
        echo = translate("HERE ARE")+" "+str(i)+" "+translate("ARROWS", i)
    return [np, gold, echo, 1]

def f_door(rmap, vmap, p, np, gold, baner, backpack, direction):
    npy, npx = np[0], np[1]
    rmap[npy][npx] = ","
    vmap[npy][npx] = ","
    echo = "YOU OPEN A DOOR"
    return [p, gold, echo, 1]

def f_weapon(rmap, vmap, p, np, gold, baner, backpack, direction):
    npy, npx = np
    i = weapon(int(rmap[npy][npx][1:4]))
    if direction == "11":
        if len(backpack) <= 5:
            rmap[npy][npx] = rmap[npy][npx][4:]
            vmap[npy][npx] = rmap[npy][npx]
            backpack.append(i)
            echo = translate("YOU TAKE") + " " + translate(str(i[:-5])) + str(i[-5:])
        else:
            echo = "NO SPACE IN BACKPACK!"
    else:
        echo = translate("HERE IS") + " " + translate(str(i[:-5])) + str(i[-5:])
    return [np, gold, echo, 1]

def f_putter(rmap, vmap, p, np, gold, baner, backpack, direction):
    npy, npx = np
    i = putter(int(rmap[npy][npx][1:4]))
    if direction == "11":
        if len(backpack) <= 5:
            rmap[npy][npx] = rmap[npy][npx][4:]
            vmap[npy][npx] = rmap[npy][npx]
            backpack.append(i)
            echo = translate("YOU TAKE") + " " + translate(str(i[:-5])) + str(i[-5:])
        else:
            echo = "NO SPACE IN BACKPACK!"
    else:
        echo = translate("HERE IS") + " " + translate(str(i[:-5])) + str(i[-5:])
    return [np, gold, echo, 1]

def f_armor(rmap, vmap, p, np, gold, baner, backpack, direction):
    npy, npx = np
    i = armor(int(rmap[npy][npx][1:4]))
    if direction == "11":
        if len(backpack) <= 5:
            rmap[npy][npx] = rmap[npy][npx][4:]
            vmap[npy][npx] = rmap[npy][npx]
            backpack.append(i)
            echo = translate("YOU TAKE") + " " + translate(str(i[:-5])) + str(i[-5:])
        else:
            echo = "NO SPACE IN BACKPACK!"
    else:
        echo = translate("HERE IS") + " " + translate(str(i[:-5])) + str(i[-5:])
    return [np, gold, echo, 1]

def f_torch(rmap, vmap, p, np, gold, baner, backpack, direction):
    npy, npx = np
    i = weapon(int(rmap[npy][npx][1:4]))
    if direction == "11":
        if len(backpack) <= 5:
            rmap[npy][npx] = rmap[npy][npx][4:]
            vmap[npy][npx] = rmap[npy][npx]
            i = "TORCH"
            backpack.append(i)
            echo = translate("YOU TAKE") + " " + translate("TORCH",1)
        else:
            echo = "NO SPACE IN BACKPACK!"
    else:
        echo = translate("HERE IS") + " " + translate("TORCH")
    return [np, gold, echo, 1]

def f_mixture(rmap, vmap, p, np, gold, baner, backpack, direction):
    npy, npx = np
    i = weapon(int(rmap[npy][npx][1:4]))
    if direction == "11":
        if len(backpack) <= 5:
            rmap[npy][npx] = rmap[npy][npx][4:]
            vmap[npy][npx] = rmap[npy][npx]
            i = "MIXTURE"
            backpack.append(i)
            echo = translate("YOU TAKE") + " " + translate("MIXTURE",1)
        else:
            echo = "NO SPACE IN BACKPACK!"
    else:
        echo = translate("HERE IS") + " " + translate("MIXTURE")
    return [np, gold, echo, 1]

def terrain(rmap, vmap, p, np, gold, baner, backpack, direction):
    # ramp, vmap, p, gold, baner, backpack, echo, moved
    match rmap[np[0]][np[1]][0]:
        case "$":
            return f_gold(rmap, vmap, p, np, gold, baner, backpack, direction)
        case "-":
            return f_arrows(rmap, vmap, p, np, gold, baner, backpack, direction)
        case "!":
            return f_orantium(rmap, vmap, p, np, gold, baner, backpack, direction)
        case "+":
            return f_door(rmap, vmap, p, np, gold, baner, backpack, direction)
        case "]":
            return f_weapon(rmap, vmap, p, np, gold, baner, backpack, direction)
        case "}":
            return f_putter(rmap, vmap, p, np, gold, baner, backpack, direction)
        case ")":
            return f_armor(rmap, vmap, p, np, gold, baner, backpack, direction)
        case "~":
            return f_torch(rmap, vmap, p, np, gold, baner, backpack, direction)
        case "?":
            return f_mixture(rmap, vmap, p, np, gold, baner, backpack, direction)
        case "=":
            return [p, gold, translate("THIS TILE IS CLOSE"), 0]
        case ".":
            return [np, gold, "", 1]
        case ",":
            return [np, gold, "", 1]
        case " ":
            return [np, gold, "", 1]
        case "#":
            return [p, gold, translate("HERE IS A WALL"), 0]
        case ">":
            return [np, gold, "HERE ARE STAIRS DOWN", 1]
        case "<":
            return [np, gold, "HERE ARE STAIRS UP", 1]
        case _:
            return [p, gold, "? - for help", 1]