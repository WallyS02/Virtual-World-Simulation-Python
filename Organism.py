from enum import IntEnum
import random
from abc import ABC, abstractmethod

import Point


class Organism(ABC):
    class OrganismType(IntEnum):
        human = 0,
        wolf = 1,
        sheep = 2,
        fox = 3,
        turtle = 4,
        antelope = 5,
        cybersheep = 6
        grass = 7,
        dandelion = 8,
        guarana = 9,
        wolfBerries = 10,
        hogweed = 11

    class Direction(IntEnum):
        left = 0,
        right = 1,
        up = 2,
        down = 3,
        noDirection = 4

    def __init__(self, organismType, world, position, bornTurn, strength, initiative):
        self.breedChance = 0.0
        self.didMultiplied = False
        self.organismType = organismType
        self.world = world
        self.icon = None
        self.position = position
        self.bornTurn = bornTurn
        self.strength = strength
        self.initiative = initiative
        self.isDead = False
        self.direction = [True, True, True, True]

    @abstractmethod
    def typeOfOrganismToString(self):
        pass

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def collision(self, other):
        pass

    @abstractmethod
    def isAnimal(self):
        pass

    def specialActionDuringAttack(self, aggressor, victim):
        return False

    def organismToString(self):
        return str(self.typeOfOrganismToString()) + " x[" + str(self.position.x) + "] y[" + str(self.position.y) + "] strength[" + str(self.strength) + "]"

    def makeMove(self, nextPosition):
        x = nextPosition.x
        y = nextPosition.y
        self.world.board[self.position.y][self.position.x] = None
        self.world.board[y][x] = self
        self.position.x = x
        self.position.y = y

    def drawType(self):
        tmp = random.randint(0, 10)
        if tmp == 0:
            return self.OrganismType.antelope
        if tmp == 1:
            return self.OrganismType.hogweed
        if tmp == 2:
            return self.OrganismType.guarana
        if tmp == 3:
            return self.OrganismType.fox
        if tmp == 4:
            return self.OrganismType.dandelion
        if tmp == 5:
            return self.OrganismType.sheep
        if tmp == 6:
            return self.OrganismType.grass
        if tmp == 7:
            return self.OrganismType.wolfBerries
        if tmp == 8:
            return self.OrganismType.wolf
        if tmp == 9:
            return self.OrganismType.turtle
        else:
            return self.OrganismType.cybersheep

    def unlockDirection(self, direction):
        self.direction[direction] = True

    def lockDirection(self, direction):
        self.direction[direction] = False

    def unlockAllDirections(self):
        self.unlockDirection(self.Direction.left)
        self.unlockDirection(self.Direction.right)
        self.unlockDirection(self.Direction.up)
        self.unlockDirection(self.Direction.down)

    def drawAnyField(self, position):
        self.unlockAllDirections()
        posX = position.x
        posY = position.y
        sizeX = self.world.sizeX
        sizeY = self.world.sizeY
        possibleDirections = 0
        if posX == 0:
            self.lockDirection(self.Direction.left)
        else:
            possibleDirections += 1
        if posX == sizeX - 1:
            self.lockDirection(self.Direction.right)
        else:
            possibleDirections += 1
        if posY == 0:
            self.lockDirection(self.Direction.up)
        else:
            possibleDirections += 1
        if posY == sizeY - 1:
            self.lockDirection(self.Direction.down)
        else:
            possibleDirections += 1

        if possibleDirections == 0:
            return position

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

    def drawAnyFreeField(self, position):
        self.unlockAllDirections()
        posX = position.x
        posY = position.y
        sizeX = self.world.sizeX
        sizeY = self.world.sizeY
        possibleDirections = 0
        if posX == 0:
            self.lockDirection(self.Direction.left)
        else:
            if self.world.isTaken(Point.Point(posX - 1, posY)) is False:
                possibleDirections += 1
            else:
                self.lockDirection(self.Direction.left)
        if posX == sizeX - 1:
            self.lockDirection(self.Direction.right)
        else:
            if self.world.isTaken(Point.Point(posX + 1, posY)) is False:
                possibleDirections += 1
            else:
                self.lockDirection(self.Direction.right)
        if posY == 0:
            self.lockDirection(self.Direction.up)
        else:
            if self.world.isTaken(Point.Point(posX, posY - 1)) is False:
                possibleDirections += 1
            else:
                self.lockDirection(self.Direction.up)
        if posY == sizeY - 1:
            self.lockDirection(self.Direction.down)
        else:
            if self.world.isTaken(Point.Point(posX, posY + 1)) is False:
                possibleDirections += 1
            else:
                self.lockDirection(self.Direction.down)

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
