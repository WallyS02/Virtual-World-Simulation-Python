import random
from abc import ABC

from PyQt5 import QtGui
import Organism
import Plant
import Point


class Hogweed(Plant.Plant, ABC):
    def __init__(self, world, position, bornTurn):
        super().__init__(Organism.Organism.OrganismType.hogweed, world, position, bornTurn, 10, 0)
        self.icon = QtGui.QPixmap("BarszczSosnowskiego.png")
        self.breedChance = 0.05

    def typeOfOrganismToString(self):
        return "Hogweed"

    def action(self):
        posX = self.position.x
        posY = self.position.y
        self.drawAnyField(self.position)
        for i in range(4):
            tmpOrganism = None
            if i == 0 and self.direction[Organism.Organism.Direction.down] is True:
                tmpOrganism = self.world.whatIsOnField(Point.Point(posX, posY + 1))
            elif i == 1 and self.direction[Organism.Organism.Direction.up] is True:
                tmpOrganism = self.world.whatIsOnField(Point.Point(posX, posY - 1))
            elif i == 2 and self.direction[Organism.Organism.Direction.left] is True:
                tmpOrganism = self.world.whatIsOnField(Point.Point(posX - 1, posY))
            elif i == 3 and self.direction[Organism.Organism.Direction.right] is True:
                tmpOrganism = self.world.whatIsOnField(Point.Point(posX + 1, posY))

            if tmpOrganism is not None and tmpOrganism.organismType != Organism.Organism.OrganismType.cybersheep and tmpOrganism.isAnimal():
                self.world.deleteOrganism(tmpOrganism)
                self.world.komentator.addComment(self.organismToString() + " kills " + tmpOrganism.organismToString())

        tmpDraw = random.randint(0, 100)
        if tmpDraw < self.breedChance * 100:
            self.spreading()

    def specialActionDuringAttack(self, aggressor, victim):
        if aggressor.strength >= 10:
            self.world.deleteOrganism(self)
            self.world.komentator.addComment(aggressor.organismToString() + " eats " + self.organismToString())
            aggressor.makeMove(victim.position)
        if aggressor.organismType != Organism.Organism.OrganismType.cybersheep and aggressor.isAnimal() or aggressor.strength < 10:
            self.world.deleteOrganism(aggressor)
            self.world.komentator.addComment(self.organismToString() + " kills " + aggressor.organismToString())
        return True
