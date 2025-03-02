from animal import Animal
import keyboard


class Human(Animal):
    def __init__(self, strength=5, initiative=4, x=0, y=0, figure='h', world=None):
        super().__init__(strength, initiative, x, y, figure, world)
        self.cooldown = 0
        self.counter = 0

    def action(self):
        new_x, new_y = self.x, self.y

        if self.counter != 0:
            self.strength -= 1
            self.counter -= 1
        elif self.counter == 0 and self.cooldown != 0:
            self.cooldown -= 1

        while True:
            event = keyboard.read_event()  # Waits until a key is pressed
            if event.event_type == keyboard.KEY_DOWN:  # Only register key presses, not releases
                if event.name == "up" and self._in_bound(self.x-1, self.y):
                    new_x = self.x-1

                elif event.name == "down" and self._in_bound(self.x+1, self.y):
                    new_x = self.x+1

                elif event.name == "left" and self._in_bound(self.x, self.y-1):
                    new_y = self.y-1

                elif event.name == "right" and self._in_bound(self.x, self.y+1):
                    new_y = self.y+1

                elif event.name == "p" and self._in_bound(self.x, self.y+1):
                    if self.cooldown == 0:
                        self.strength += 5
                        self.cooldown = 5
                        self.counter = 5
                    else:
                        print("ability on cooldown!")

                if self.is_occupied(new_x, new_y):
                    self.collision(self.get_organism_at(new_x, new_y))
                else:
                    self.x, self.y = new_x, new_y

                return  # Exit after moving

    def collision(self, other):
        super().collision(other)

