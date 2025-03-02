from animal import Animal
import random


class Fox(Animal):
    def __init__(self, strength=3, initiative=7, x=0, y=0, figure='f', world=None):
        super().__init__(strength, initiative, x, y, figure, world)

    def get_free_neighbors_fox(self, x, y):
        neighbors = [(x + dx, y + dy) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]]

        return [(nx, ny) for nx, ny in neighbors if self._in_bound(nx, ny) and not self.is_occupied(nx, ny)
                and not self.is_occupied_by_stronger(nx, ny)]

    def action(self):
        free_positions = self.get_free_neighbors_fox(self.x, self.y)
        if free_positions:
            new_x, new_y = random.choice(free_positions)
            if self.is_occupied(new_x, new_y):
                self.collision(self.get_organism_at(new_x, new_y))
            else:
                self.x, self.y = new_x, new_y
