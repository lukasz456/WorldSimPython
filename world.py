class World:

    def __init__(self, width, height, organisms=None):
        if organisms is None:
            organisms = []
        self.width = width
        self.height = height
        self.organisms = organisms
        self.new_organisms = []
        self.grid = {}
        self.messages = []
        self.round = 0

    def add_organism(self, organism):
        self.organisms.append(organism)

    def add_new_organism(self, organism):
        self.new_organisms.append(organism)

    def remove_organism(self, organism):
        self.organisms.remove(organism)

    def remove_plant(self, organism):
        self.new_organisms.remove(organism)

    def make_turn(self):
        self.organisms.sort(key=lambda o: (-o.initiative, -o.age))
        for organism in self.organisms:
            organism.action()
            organism.raise_age()
        self.organisms += self.new_organisms
        self.new_organisms.clear()
        self.round += 1

        print()
        print()
        self.draw_world()

    def draw_world(self):
        for i in range(self.height):
            for j in range(self.width):
                if_dot = True
                for organism in self.organisms:
                    if i == organism.x and j == organism.y:
                        print(organism.draw() + ' ', end='')
                        self.grid[(i, j)] = organism.figure
                        if_dot = False
                if if_dot:
                    print('.', end=' ')
                    self.grid[(i, j)] = '.'
            print()

    def get_name(self, figure):
        names = {'h': 'human', 's': 'sheep', 'g': 'grass', 'w': 'wolf', 'f': 'fox', 't': 'turtle', 'a': 'antelope',
                 '$': 'sow thistle', '@': 'guarana', 'b': 'belladonna', '*': 'sosnowskys hogweed',
                 'c': 'cyber'}
        return names[figure]

    def breed_mes(self, organism, new_x, new_y):
        self.messages.append(
            " new " + self.get_name(organism.figure) + " created at x: " + str(new_x) + ", y: " + str(new_y))

    def kill_mes(self, organism, other):
        self.messages.append(
            " " + self.get_name(organism.figure) + " killed " + self.get_name(other.figure) + " at x: " +
            str(organism.x) + ", y: " + str(organism.y))

    def eat_mes(self, organism, other):
        self.messages.append(
            " " + self.get_name(organism.figure) + " ate " + self.get_name(other.figure) + " at x: " +
            str(organism.x) + ", y: " + str(organism.y))

    def eat_mes_sh(self, organism, other):
        self.messages.append(
            " " + self.get_name(organism.figure) + " ate " + self.get_name(other.figure) + " at x: " +
            str(other.x) + ", y: " + str(other.y))

