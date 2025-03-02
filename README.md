# WorldSimPython
Overview
The goal of this project is to implement a 2D virtual world simulator, where different organisms (plants and animals) interact within a 2D grid environment. The world grid has a size of NxM, and each organism occupies one cell on this grid. The simulator operates in turns, with each organism performing actions based on its species and initiative.

Key Features:
Organisms: Various life forms (animals and plants) exist with different behaviors. Each organism occupies a single cell in the world.
Turn-Based Simulation: The world progresses in turns, where every organism performs an action according to its behavior.
Collisions and Fights: If two organisms collide in a cell, one may defeat the other depending on factors like strength, initiative, and species-specific abilities.
Human Player: A human player, who is an animal, can move by pressing the arrow keys to determine their movement direction. The human also has a special ability that can be activated for five turns.
