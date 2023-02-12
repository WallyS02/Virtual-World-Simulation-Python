from abc import ABC

from PyQt5 import QtGui
import Organism
import Plant


class Grass(Plant.Plant, ABC):
    def __init__(self, world, position, bornTurn):
        super().__init__(Organism.Organism.OrganismType.grass, world, position, bornTurn, 0, 0)
        self.icon = QtGui.QPixmap("Trawa.png")

    def typeOfOrganismToString(self):
        return "Grass"
