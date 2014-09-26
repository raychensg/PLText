import classes as cl
import constants as cn

with cn.characters[0] as cl.screen:
    while cn.characters[0].dat.alive:
        cn.characters[0].prompt()
        cn.characters[0].parse(cl.screen.getstr())
        cl.screen.refresh()
    exit()
