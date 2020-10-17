from mcpi.minecraft import Minecraft
mc = Minecraft .create()

while True:
    x, y, z = mc.player.getTilePos()
    mc.postToChat("you are located on X:" +str(x)+ "Y:"  +str(y)+ "Z:" +str(z))