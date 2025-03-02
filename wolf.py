from animal import Animal


class Wolf(Animal):
    def __init__(self, strength=9, initiative=5, x=0, y=0, figure='w', world=None):
        super().__init__(strength, initiative, x, y, figure, world)
