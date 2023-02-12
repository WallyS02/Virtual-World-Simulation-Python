import random
from abc import ABC

from PyQt5 import QtGui
import Organism
import Plant


class WolfBerries(Plant.Plant, ABC):
    def __init__(self, world, position, bornTurn):
        super().__init__(Organism.Organism.OrganismType.wolfBerries, world, position, bornTurn, 99, 0)
        self.icon = QtGui.QPixmap("WilczeJagody.png")
        self.breedChance = 0.05

    def typeOfOrganismToString(self):
        return "WolfBerries"

    def action(self):
        tmpDraw = random.randint(0, 100)
        if tmpDraw < self.breedChance * 100:
            self.spreading()

    def specialActionDuringAttack(self, aggressor, victim):
        self.world.komentator.addComment(aggressor.organismToString() + " eats " + self.organismToString())
        if aggressor.strength >= 99:
            self.world.deleteOrganism(self)
            self.world.komentator.addComment(aggressor.organismToString() + " destroys wolf berries bush")
        if aggressor.isAnimal():
            self.world.deleteOrganism(aggressor)
            self.world.komentator.addComment(aggressor.organismToString() + " dies from poisonous wolf berries")
        return True
