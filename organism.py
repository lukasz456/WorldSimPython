from abc import ABC, abstractmethod
import random


class Organism(ABC):
    def __init__(self, strength, initiative, x, y, figure, world):
        self.strength = strength
        self.initiative = initiative
        self.x = x
        self.y = y
        self.figure = figure
        self.world = world
        self.age = 0

    @abstractmethod
    def action(self):
        pass

    def collision(self, other):
        if_escape = random.randint(1, 10)
        if self.figure == other.figure:
            free_positions = other.get_free_neighbors(other.x, other.y)
            if free_positions:
                new_x, new_y = random.choice(free_positions)
                new_animal = self.__class__(x=new_x, y=new_y, world=self.world)
                self.world.add_new_organism(new_animal)
                self.world.breed_mes(self, new_x, new_y)

        elif other.figure == 't' and self.strength < 5:
            return

        elif other.figure == 'a' and if_escape <= 5:
            free_positions = other.get_free_neighbors(other.x, other.y)
            if free_positions:
                self.x = other.x
                self.y = other.y
                other.x, other.y = random.choice(free_positions)
            else:
                self.kill(other)

        elif other.figure == '@':
            self.strength += 3
            self.kill(other)

        elif other.figure == 'b':
            self.kill_self(other)

        elif other.figure == '*' and self.figure is not 'c':
            self.kill_self(other)

        elif self.strength >= other.strength:
            self.kill(other)

        else:
            self.kill_self(other)

    def draw(self):
        return self.figure

    def _in_bound(self, x, y):
        if x < 0 or x >= self.world.height:
            return False
        elif y < 0 or y >= self.world.width:
            return False
        else:
            return True

    def raise_age(self):
        self.age += 1

    def _get_field(self, x, y):
        return self.world.grid.get((x, y), 0)

    def get_organism_at(self, x, y):
        for organism in self.world.organisms:
            if organism.x == x and organism.y == y and organism is not self:
                return organism
        for organism in self.world.new_organisms:
            if organism.x == x and organism.y == y and organism is not self:
                return organism

    def is_occupied(self, x, y):
        for organism in self.world.organisms:
            if organism.x == x and organism.y == y and organism is not self:
                return True
        for organism in self.world.new_organisms:
            if organism.x == x and organism.y == y and organism is not self:
                return True
        return False

    def get_free_neighbors(self, x, y):
        neighbors = [(x + dx, y + dy) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]]
        return [(nx, ny) for nx, ny in neighbors if self._in_bound(nx, ny) and not self.is_occupied(nx, ny)]

    def get_neighbors(self):
        neighbors = [(self.x + dx, self.y + dy) for dx, dy in
                     [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1),
                      (-1, 1)]]
        return [(nx, ny) for nx, ny in neighbors if self._in_bound(nx, ny)]

    def is_human_alive(self):
        for organism in self.world.organisms:
            if organism.figure == 'h':
                return True
        return False

    def get_free_neighbors_fox(self, x, y):
        neighbors = [(x + dx, y + dy) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]]
        return [(nx, ny) for nx, ny in neighbors if self._in_bound(nx, ny) and not self.is_occupied(nx, ny)]

    def is_occupied_by_stronger(self, x, y):
        if self.is_occupied(x, y):
            if self.get_organism_at(x, y).strength > self.strength:
                return True
        else:
            return False

    def kill(self, other):
        from animal import Animal
        self.world.remove_organism(other)
        self.x = other.x
        self.y = other.y
        if isinstance(other, Animal):
            self.world.kill_mes(self, other)
        else:
            self.world.eat_mes(self, other)

    def kill_self(self, other):
        self.world.remove_organism(self)
        self.world.kill_mes(other, self)

    def is_hogweed(self):
        for organism in self.world.organisms:
            if organism.figure == '*':
                return True
        return False

    def find_goal(self):
        goal = None
        d = 0
        counter = 1
        for organism in self.world.organisms:
            if organism.figure == '*':
                a = organism.x - self.x
                b = organism.y - self.y
                c = (a**2 + b**2)**0.5
                if c <= d or counter == 1:
                    d = c
                    goal = organism
                    counter += 1
        return goal

