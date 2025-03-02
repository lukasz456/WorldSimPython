from animal import Animal
import random


class Turtle(Animal):
    def __init__(self, strength=2, initiative=1, x=0, y=0, figure='t', world=None):
        super().__init__(strength, initiative, x, y, figure, world)

    def action(self):
        new_x, new_y = self.x, self.y
        random_nr = random.randint(1, 100)
        if_stay = random.randint(1, 100)

        if random_nr <= 25 and self._in_bound(self.x - 1, self.y):
            new_x = self.x - 1

        elif 26 <= random_nr <= 50 and self._in_bound(self.x + 1, self.y):
            new_x = self.x + 1

        elif 51 <= random_nr <= 75 and self._in_bound(self.x, self.y - 1):
            new_y = self.y - 1

        elif random_nr >= 75 and self._in_bound(self.x, self.y + 1):
            new_y = self.y + 1

        if if_stay <= 75:
            return
        elif self.is_occupied(new_x, new_y):
            self.collision(self.get_organism_at(new_x, new_y))
        else:
            self.x, self.y = new_x, new_y



