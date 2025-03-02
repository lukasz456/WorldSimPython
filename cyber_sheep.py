from animal import Animal
import random


class CyberSheep(Animal):
    def __init__(self, strength=11, initiative=4, x=0, y=0, figure='c', world=None):
        super().__init__(strength, initiative, x, y, figure, world)

    def action(self):
        if self.is_hogweed():
            goal = self.find_goal()
            new_x, new_y = self.x, self.y

            if self.x > goal.x:
                new_x -= 1
            elif self.x < goal.x:
                new_x += 1
            elif self.y > goal.y:
                new_y -= 1
            elif self.y < goal.y:
                new_y += 1
            if self.is_occupied(new_x, new_y):
                self.collision(self.get_organism_at(new_x, new_y))
            else:
                self.x, self.y = new_x, new_y
        else:
            super().action()
