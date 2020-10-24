from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getTilePos()

lenght=40
width=50
high=60

block=57
air=0

mc.setBlocks(x,y,z,x+lenght,y+width,z+high,block)

mc.setBlocks(x+1,y+1,z+1,x+lenght-1,y+width-1,z+high-1,air)



    
    