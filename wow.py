from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

time.sleep(5)

x, y, z = mc.player.getTilePos()

mc.setBlocks(x+55,y-1,z+55,x-55,y-1,z-55,56)

    
    