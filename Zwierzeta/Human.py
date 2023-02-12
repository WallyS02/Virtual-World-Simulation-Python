from abc import ABC

from PyQt5 import QtGui
import Animal
import Organism
import Point


class Human(Animal.Animal, ABC):
    def __init__(self, world, position, bornTurn):
        super().__init__(Organism.Organism.OrganismType.human, world, position, bornTurn, 5, 4)
        self.moveLength = 1
        self.moveChance = 1
        self.moveDirection = Organism.Organism.Direction.noDirection
        self.icon = QtGui.QPixmap("Czlowiek.png")
        self.cooldown = 0

    def typeOfOrganismToString(self):
        return "Human"

    def planMove(self):
        x = self.position.x
        y = self.position.y
        self.drawAnyField(self.position)
        if self.moveDirection == Organism.Organism.Direction.noDirection or self.direction[self.moveDirection] is False:
            return self.position
        else:
            if self.moveDirection == Organism.Organism.Direction.down:
                return Point.Point(x, y + 1)
            elif self.moveDirection == Organism.Organism.Direction.up:
                return Point.Point(x, y - 1)
            elif self.moveDirection == Organism.Organism.Direction.left:
                return Point.Point(x - 1, y)
            elif self.moveDirection == Organism.Organism.Direction.right:
                return Point.Point(x + 1, y)
            else:
                return Point.Point(x, y)

    def action(self):
        for i in range(1, self.moveLength + 1):
            futurePosition = self.planMove()
            if self.world.isTaken(futurePosition) and self.world.whatIsOnField(futurePosition) is not self:
                self.collision(self.world.whatIsOnField(futurePosition))
                break
            elif self.world.whatIsOnField(futurePosition) is not self:
                self.makeMove(futurePosition)
        self.moveDirection = Organism.Organism.Direction.noDirection
