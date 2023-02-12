from abc import ABC

from PyQt5 import QtGui
import Animal
import Organism


class Turtle(Animal.Animal, ABC):
    def __init__(self, world, position, bornTurn):
        super().__init__(Organism.Organism.OrganismType.turtle, world, position, bornTurn, 2, 1)
        self.moveLength = 1
        self.moveChance = 0.25
        self.icon = QtGui.QPixmap("Zolw.png")

    def typeOfOrganismToString(self):
        return "Turtle"

    def specialActionDuringAttack(self, aggressor, victim):
        if self is victim:
            if aggressor.strength < 5 and aggressor.isAnimal() is True:
                self.world.komentator.addComment(self.organismToString() + " defends from " + aggressor.organismToString())
                return True
            else:
                return False
        else:
            if aggressor.strength >= 5 and aggressor.isAnimal() is True:
                return False
            else:
                if victim.strength < 5 and victim.isAnimal() is True:
                    self.world.komentator.addComment(self.organismToString() + " defends from " + victim.organismToString())
                    return True
                else:
                    return False
