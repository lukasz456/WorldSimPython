from animal import Animal


class Sheep(Animal):
    def __init__(self, strength=4, initiative=4, x=0, y=0, figure='s', world=None):
        super().__init__(strength, initiative, x, y, figure, world)
