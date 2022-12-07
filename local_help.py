help_echo = ""
def help_init(path,depth):
    global help_echo
    depth = "s" + str((depth+4)//5)
    with open(str(path) + str(depth) +"_depth_help.txt") as I:
        help_echo = I.read()

def pomoc():
    global help_echo
    input("""Tiles: 							Version = H_version.0.1
    @ - you
    # - wall
    + - closed door
    , - open door
    . - light tile
    = - closed tile (You have to kill a Boss "B")
    > - stairs down
    < - stairs up
    ] - weapon
    } - ranged weapon
    ) - armor
    ! - orantium
    - - arrows
    ~ - torch
    ? - mixture
Movement:
    7 8 9
    4 5 6   5 - wait or take item from the flor
    1 2 3
    - - throw orantium
    0 - ranged attack
        Don't forget about NumLock!
Press enter to continue""" + "\n")
    input(help_echo[:-1]+"\n")