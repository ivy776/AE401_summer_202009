import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x, y, z = mc.player.getTilePos()

for i in range(20):
    
    d = random.randrange(1,5)
    
    if d == 1:
        mc.setBlocks(x,y,z,x+10,y+2,z,57)
        x = x+10
        y = y+2
    elif d == 2:
        mc.setBlocks(x,y,z,x-10,y-2,z,57)
        x = x-10
        y = y-2
    elif d == 3:
        mc.setBlocks(x,y,z,x,y,z+10,57)
        z = z+10
    elif d == 4:
        mc.setBlocks(x,y,z,x,y,z-10,57)
        z = z-10