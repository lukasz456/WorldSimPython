from plant import Plant


class Guarana(Plant):
    def __init__(self, strength=0, initiative=0, x=0, y=0, figure='@', world=None):
        super().__init__(strength, initiative, x, y, figure, world)

