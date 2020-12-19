from mcpi.minecraft import Minecraft
mc = Minecraft.create()
myId = mc.getPlayerEntityId('Ivy776')
x,y,z = mc.entity.getTilePos(myId)
list2d = [[12,8,5],
          [5,8,3],
          [23,0,9],
          [30,70,7],
          [44,70,25]]
startX = x
for list1d in list2d:
    for i in list1d:
        mc.setBlock(x,y,z,i)
        x = x+1
    x = startX
    z = z+1