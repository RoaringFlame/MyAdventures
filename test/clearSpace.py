import mcpi.minecraft as minecreaft
import mcpi.block as block

mc = minecreaft.Minecraft.create()

pos = mc.player.getTilePos()

size = int(raw_input("size of area to clear?"))

mc.setBlocks(pos.x, pos.y, pos.z,
             pos.x + size, pos.y + size, pos.z + size,
             block.AIR.id)
