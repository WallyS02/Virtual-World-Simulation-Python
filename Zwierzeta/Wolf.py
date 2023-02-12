from abc import ABC

from PyQt5 import QtGui
import Animal
import Organism


class Wolf(Animal.Animal, ABC):
    def __init__(self, world, position, bornTurn):
        super().__init__(Organism.Organism.OrganismType.wolf, world, position, bornTurn, 9, 5)
        self.moveLength = 1
        self.moveChance = 1
        self.icon = QtGui.QPixmap("Wilk.png")

    def typeOfOrganismToString(self):
        return "Wolf"
