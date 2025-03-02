from plant import Plant


class Belladonna(Plant):
    def __init__(self, strength=99, initiative=0, x=0, y=0, figure='b', world=None):
        super().__init__(strength, initiative, x, y, figure, world)

