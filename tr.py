from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

def Pyramid(x,y,z,base):
    height = (base//2)+1
    
    for i in range(height):
        x1 = x+i
        y1 = y+i
        z1 = z+i
        
        x2 = x+base-i
        #y與y2相同
        z2 = z +base-i
        mc.setBlocks(x1,y1,z1,x2,y1,z2,53)
        
x,y,z = mc.player.getTilePos()
Pyramid(x,y,z,50)        
   
    
    
    
    