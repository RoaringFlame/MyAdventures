import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

mc.setBlock(pos.x + 3, pos.y, pos.z, block.STONE.id)
mc.setBlock(pos.x + 3, pos.y + 2, pos.z, block.STONE.id)
mc.setBlock(pos.x + 3, pos.y + 4, pos.z, block.STONE.id)
mc.setBlock(pos.x + 3, pos.y, pos.z + 4, block.STONE.id)
mc.setBlock(pos.x + 3, pos.y + 2, pos.z + 4, block.STONE.id)
mc.setBlock(pos.x + 3, pos.y + 4, pos.z + 4, block.STONE.id)
