from world import World
from human import Human
from sheep import Sheep
from grass import Grass
from wolf import Wolf
from fox import Fox
from turtle import Turtle
from antelope import Antelope
from sow_thistle import SowThistle
from guarana import Guarana
from belladonna import Belladonna
from sosnowskys_hogweed import SosnowskysHogweed
from cyber_sheep import CyberSheep

world = World(15, 15)

# fox1 = Fox(x=1, y=7, world=world)
# world.add_organism(fox1)
# fox2 = Fox(x=8, y=2, world=world)
# world.add_organism(fox2)
# sheep1 = Sheep(x=4, y=6, world=world)
# world.add_organism(sheep1)
# sheep2 = Sheep(x=2, y=2, world=world)
# world.add_organism(sheep2)
# wolf1 = Wolf(x=4, y=2, world=world)
# world.add_organism(wolf1)
# wolf2 = Wolf(x=4, y=13, world=world)
# world.add_organism(wolf2)
# grass = Grass(x=1, y=0, world=world)
# world.add_organism(grass)
# turtle1 = Turtle(x=7, y=7, world=world)
# world.add_organism(turtle1)
# turtle2 = Turtle(x=0, y=7, world=world)
# world.add_organism(turtle2)
# antelope1 = Antelope(x=11, y=7, world=world)
# world.add_organism(antelope1)
# antelope2 = Antelope(x=13, y=0, world=world)
# world.add_organism(antelope2)
# sow_thistle = SowThistle(x=12, y=1, world=world)
# world.add_organism(sow_thistle)
# guarana = Guarana(x=14, y=7, world=world)
# world.add_organism(guarana)
# belladonna = Belladonna(x=14, y=11, world=world)
# world.add_organism(belladonna)
# sosnowsky = SosnowskysHogweed(x=12, y=10, world=world)
# world.add_organism(sosnowsky)
# cyber = CyberSheep(x=10, y=7, world=world)
# world.add_organism(cyber)
# sosnowsky2 = SosnowskysHogweed(x=1, y=10, world=world)
# world.add_organism(sosnowsky2)
human = Human(x=10, y=8, world=world)
world.add_organism(human)

print(human.find_goal())

world.draw_world()
while human.is_human_alive():
    world.make_turn()
    for message in world.messages:
        print("round: " + str(world.round) + message)
    world.messages.clear()
print('Game Over!')







