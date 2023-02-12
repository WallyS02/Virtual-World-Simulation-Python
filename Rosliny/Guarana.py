from abc import ABC

from PyQt5 import QtGui
import Organism
import Plant


class Guarana(Plant.Plant, ABC):
    def __init__(self, world, position, bornTurn):
        super().__init__(Organism.Organism.OrganismType.guarana, world, position, bornTurn, 0, 0)
        self.icon = QtGui.QPixmap("Guarana.png")

    def typeOfOrganismToString(self):
        return "Guarana"

    def specialActionDuringAttack(self, aggressor, victim):
        tmpPosition = self.position
        self.world.deleteOrganism(self)
        aggressor.makeMove(tmpPosition)
        self.world.komentator.addComment(aggressor.organismToString() + " eats " + self.organismToString())
        aggressor.strength += 3
        return True
