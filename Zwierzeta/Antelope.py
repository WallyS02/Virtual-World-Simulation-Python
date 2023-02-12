import random
from abc import ABC

from PyQt5 import QtGui
import Animal
import Organism


class Antelope(Animal.Animal, ABC):
    def __init__(self, world, position, bornTurn):
        super().__init__(Organism.Organism.OrganismType.antelope, world, position, bornTurn, 4, 4)
        self.moveLength = 2
        self.moveChance = 1
        self.icon = QtGui.QPixmap("Antylopa.png")

    def typeOfOrganismToString(self):
        return "Antelope"

    def specialActionDuringAttack(self, aggressor, victim):
        tmpDraw = random.randint(0, 100)
        if tmpDraw < 50:
            if self is aggressor:
                self.world.komentator.addComment(self.organismToString() + " runs away from " + victim.organismToString())
                tmpPosition = self.drawAnyFreeField(victim.position)
                if tmpPosition.x != victim.position.x and tmpPosition.y != victim.position.y:
                    self.makeMove(tmpPosition)
            elif self is victim:
                self.world.komentator.addComment(self.organismToString() + " runs away from " + aggressor.organismToString())
                tmpPosition = self.position
                self.makeMove(self.drawAnyFreeField(self.position))
                if tmpPosition.x == self.position.x and tmpPosition.y == self.position.y:
                    self.world.deleteOrganism(self)
                    self.world.komentator.addComment(aggressor.organismToString() + " kills " + self.organismToString())
                aggressor.makeMove(tmpPosition)
            return True
        else:
            return False
