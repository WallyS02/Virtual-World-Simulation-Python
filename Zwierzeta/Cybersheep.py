from abc import ABC

from PyQt5 import QtGui
import Animal
import Organism
import Point


class Cybersheep(Animal.Animal, ABC):
    def __init__(self, world, position, bornTurn):
        super().__init__(Organism.Organism.OrganismType.cybersheep, world, position, bornTurn, 11, 4)
        self.moveLength = 1
        self.moveChance = 1
        self.breedChance = 0.1
        self.icon = QtGui.QPixmap("Cyberowca.png")

    def typeOfOrganismToString(self):
        return "Cybersheep"

    def findDistance(self, otherPosition):
        dx = abs(self.position.x - otherPosition.x)
        dy = abs(self.position.y - otherPosition.y)
        return dx + dy

    def findClosestHogweed(self):
        tmpHogweed = None
        closestDistance = self.world.sizeX + self.world.sizeY + 1
        for i in range(self.world.sizeY):
            for j in range(self.world.sizeX):
                tmpOrganism = self.world.board[i][j]
                if tmpOrganism is not None and tmpOrganism.organismType == Organism.Organism.OrganismType.hogweed:
                    tmpDistance = self.findDistance(tmpOrganism.position)
                    if closestDistance > tmpDistance:
                        closestDistance = tmpDistance
                        tmpHogweed = tmpOrganism
        return tmpHogweed

    def drawAnyField(self, position):
        if self.world.isHogweedOnMap():
            target = self.findClosestHogweed().position
            dx = abs(position.x - target.x)
            dy = abs(position.y - target.y)
            if dx >= dy:
                if position.x > target.x:
                    return Point.Point(position.x - 1, position.y)
                else:
                    return Point.Point(position.x + 1, position.y)
            else:
                if position.y > target.y:
                    return Point.Point(position.x, position.y - 1)
                else:
                    return Point.Point(position.x, position.y + 1)
        else:
            return Animal.Animal.drawAnyFreeField(self, position)
