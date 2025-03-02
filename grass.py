from plant import Plant


class Grass(Plant):
    def __init__(self, strength=0, initiative=0, x=0, y=0, figure='g', world=None):
        super().__init__(strength, initiative, x, y, figure, world)

