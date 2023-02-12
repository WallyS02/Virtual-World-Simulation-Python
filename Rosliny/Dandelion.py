import random
from abc import ABC

from PyQt5 import QtGui
import Organism
import Plant


class Dandelion(Plant.Plant, ABC):
    def __init__(self, world, position, bornTurn):
        super().__init__(Organism.Organism.OrganismType.dandelion, world, position, bornTurn, 0, 0)
        self.icon = QtGui.QPixmap("Mlecz.png")

    def typeOfOrganismToString(self):
        return "Dandelion"

    def action(self):
        for i in range(3):
            tmpDraw = random.randint(0, 100)
            if tmpDraw < self.breedChance:
                self.spreading()
