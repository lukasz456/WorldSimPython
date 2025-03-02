from organism import Organism
import random


class Plant(Organism):
    def __init__(self, strength, initiative, x, y, figure, world):
        super().__init__(strength, initiative, x, y, figure, world)

    def action(self):
        random_nr = random.randint(1, 100)
        if_sow = random.randint(1, 10)
        new_x, new_y = 0, 0

        if random_nr <= 25:
            new_x, new_y = self.x - 1, self.y

        elif 26 <= random_nr <= 50:
            new_x, new_y = self.x + 1, self.y

        elif 51 <= random_nr <= 75:
            new_x, new_y = self.x, self.y - 1

        elif random_nr >= 75:
            new_x, new_y = self.x, self.y + 1

        if if_sow <= 3 and not self.is_occupied(new_x, new_y) and self._in_bound(new_x, new_y):
            new_plant = self.__class__(x=new_x, y=new_y, world=self.world)
            self.world.add_new_organism(new_plant)

    def collision(self, other):
        super().collision(other)


