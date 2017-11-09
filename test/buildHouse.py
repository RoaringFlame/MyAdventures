import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

SIZE = 20

pos = mc.player.getTilePos()

x = pos.x + 2
y = pos.y
z = pos.z

midX = x + SIZE / 2
midY = y + SIZE / 2

mc.setBlocks(x, y, z, x + SIZE, y + SIZE, z + SIZE,
             block.COBBLESTONE.id)
mc.setBlocks(x + 1, y, z + 1, x + SIZE - 2, y + SIZE - 1, z + SIZE - 2,
             block.AIR.id)
mc.setBlocks(midX - 1, y, z, midX + 1, y + 3, z,
             block.AIR.id)

mc.setBlocks(x + 3, y + SIZE - 3, z, midX - 3, midY - 3, z,
             block.GLASS.id)
mc.setBlocks(midX + 3, y + SIZE - 3, z, x + SIZE - 3, midY + 3, z,
             block.GLASS.id)

mc.setBlocks(x, y + SIZE - 1, z, x + SIZE, y + SIZE - 1, z + SIZE,
             block.WOOD.id)
mc.setBlocks(x + 1, y - 1, z + 1, x + SIZE - 2, y - 1, z + SIZE - 2,
             block.WOOL.id)
