from mcpi.minecraft import Minecraft
mc = Minecraft.create()

myId = mc.getPlayerEntityId('Ivy776')
mc.postToTitle(myId,'你好')

mc.entity.setTilePos(myId,0,0,0)