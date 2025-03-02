from plant import Plant
from animal import Animal


class SosnowskysHogweed(Plant):
    def __init__(self, strength=10, initiative=0, x=0, y=0, figure='*', world=None):
        super().__init__(strength, initiative, x, y, figure, world)

    def action(self):
        neighbours = self.get_neighbors()

        for x, y in neighbours:
            victim = self.get_organism_at(x, y)
            if victim:
                if victim.figure == 'c':
                    return

                elif isinstance(victim, Animal):
                    self.world.remove_organism(victim)
                    self.world.kill_mes(self, victim)


