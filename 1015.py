from mcpi.minecraft import Minecraft
import time

mc = Minecraft .create()

time.sleep(5)

x, y, z = mc.player.getTilePos()
mc.postToChat("you are located on X:" +str(x)+ "Y:"  +str(y)+ "Z:" +str(z))
mc.setBlock(x,y,z,103)
time.sleep(1)
mc.setBlock(x,y+1,z,103)
time.sleep(1)
mc.setBlock(x,y+2,z,103)
time.sleep(1)
mc.setBlock(x,y+3,z,103)
time.sleep(1)
mc.setBlock(x,y+4,z,103)
time.sleep(1)
mc.setBlock(x,y+5,z,103)
time.sleep(1)
mc.setBlock(x,y+6,z,103)
time.sleep(1)
mc.setBlock(x,y+7,z,103)
time.sleep(1)
mc.setBlock(x,y+8,z,103)
time.sleep(1)
mc.setBlock(x,y+9,z,103)
    
    
    