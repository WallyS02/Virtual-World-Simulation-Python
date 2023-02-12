import random
from abc import ABC

from PyQt5 import QtGui
import Animal
import Organism
import Point


class Fox(Animal.Animal, ABC):
    def __init__(self, world, position, bornTurn):
        super().__init__(Organism.Organism.OrganismType.fox, world, position, bornTurn, 3, 7)
        self.moveLength = 1
        self.moveChance = 1
        self.icon = QtGui.QPixmap("Lis.png")

    def typeOfOrganismToString(self):
        return "Fox"

    def drawAnyField(self, position):
        self.unlockAllDirections()
        posX = position.x
        posY = position.y
        sizeX = self.world.sizeX
        sizeY = self.world.sizeY
        possibleDirections = 0
        tmpOrganism = None
        if posX == 0:
            self.lockDirection(self.Direction.left)
        else:
            tmpOrganism = self.world.board[posY][posX - 1]
            if tmpOrganism is not None and tmpOrganism.strength > self.strength:
                self.lockDirection(self.Direction.left)
            else:
                possibleDirections += 1
        if posX == sizeX - 1:
            self.lockDirection(self.Direction.right)
        else:
            tmpOrganism = self.world.board[posY][posX + 1]
            if tmpOrganism is not None and tmpOrganism.strength > self.strength:
                self.lockDirection(self.Direction.right)
            else:
                possibleDirections += 1
        if posY == 0:
            self.lockDirection(self.Direction.up)
        else:
            tmpOrganism = self.world.board[posY - 1][posX]
            if tmpOrganism is not None and tmpOrganism.strength > self.strength:
                self.lockDirection(self.Direction.up)
            else:
                possibleDirections += 1
        if posY == sizeY - 1:
            self.lockDirection(self.Direction.down)
        else:
            tmpOrganism = self.world.board[posY + 1][posX]
            if tmpOrganism is not None and tmpOrganism.strength > self.strength:
                self.lockDirection(self.Direction.down)
            else:
                possibleDirections += 1

        if possibleDirections == 0:
            return Point.Point(posX, posY)

        while True:
            upperBound = 100
            tmpDraw = random.randint(0, upperBound)
            if tmpDraw < 25 and self.direction[self.Direction.left] is True:
                return Point.Point(posX - 1, posY)
            elif 25 <= tmpDraw < 50 and self.direction[self.Direction.right] is True:
                return Point.Point(posX + 1, posY)
            elif 50 <= tmpDraw < 75 and self.direction[self.Direction.up] is True:
                return Point.Point(posX, posY - 1)
            elif tmpDraw >= 75 and self.direction[self.Direction.down] is True:
                return Point.Point(posX, posY + 1)
