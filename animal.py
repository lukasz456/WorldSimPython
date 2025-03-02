from organism import Organism
import random


class Animal(Organism):
    def __init__(self, strength, initiative, x, y, figure, world):
        super().__init__(strength, initiative, x, y, figure, world)

    def action(self):
        new_x, new_y = self.x, self.y
        random_nr = random.randint(1, 100)

        if random_nr <= 25 and self._in_bound(self.x-1, self.y):
            new_x = self.x-1

        elif 26 <= random_nr <= 50 and self._in_bound(self.x+1, self.y):
            new_x = self.x+1

        elif 51 <= random_nr <= 75 and self._in_bound(self.x, self.y-1):
            new_y = self.y-1

        elif random_nr >= 75 and self._in_bound(self.x, self.y+1):
            new_y = self.y+1

        if self.is_occupied(new_x, new_y):
            self.collision(self.get_organism_at(new_x, new_y))
        else:
            self.x, self.y = new_x, new_y

    def collision(self, other):
        super().collision(other)
