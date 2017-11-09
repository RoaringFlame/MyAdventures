import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

print("x="+str(pos.x)+";y="+str(pos.y)+";z="+str(pos.z))

mc.postToChat("x="+str(pos.x)+";y="+str(pos.y)+";z="+str(pos.z))

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.x == 5 and pos.z == 23:
        mc.postToChat("welcome home!")
