from time import sleep
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    mc.executeCommand("time add 100")
    sleep(0.05)