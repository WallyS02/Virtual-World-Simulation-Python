from abc import ABC

from PyQt5 import QtGui
import Animal
import Organism


class Sheep(Animal.Animal, ABC):
    def __init__(self, world, position, bornTurn):
        super().__init__(Organism.Organism.OrganismType.sheep, world, position, bornTurn, 4, 4)
        self.moveLength = 1
        self.moveChance = 1
        self.icon = QtGui.QPixmap("Owca.png")

    def typeOfOrganismToString(self):
        return "Sheep"
