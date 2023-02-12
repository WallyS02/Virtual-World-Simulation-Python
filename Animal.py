import random
from abc import ABC
import Factory
import Organism


class Animal(Organism.Organism, ABC):
    def __init__(self, organismType, world, position, bornTurn, strength, initiative):
        super().__init__(organismType, world, position, bornTurn, strength, initiative)
        self.moveLength = 1
        self.didMultiplied = False
        self.breedChance = 0.5
        self.moveChance = 1

    def breeding(self, other):
        if self.didMultiplied is True or other.didMultiplied is True:
            return
        tmpPoint = self.drawAnyFreeField(self.position)
        if tmpPoint.x == self.position.x and tmpPoint.y == self.position.y:
            tmpPoint2 = other.drawAnyFreeField(other.position)
            if tmpPoint2.x == other.position.x and tmpPoint2.y == other.position.y:
                return
            else:
                tmpOrganism = Factory.createOrganism(self.organismType, self.world, tmpPoint2)
                self.world.komentator.addComment("New organism born " + tmpOrganism.organismToString())
                self.world.addOrganism(tmpOrganism)
                self.didMultiplied = True
                other.didMultiplied = True
        else:
            tmpOrganism = Factory.createOrganism(self.organismType, self.world, tmpPoint)
            self.world.komentator.addComment("New organism born " + tmpOrganism.organismToString())
            self.world.addOrganism(tmpOrganism)
            self.didMultiplied = True
            other.didMultiplied = True

    def collision(self, other):
        if self.organismType == other.organismType:
            tmpDraw = random.randint(0, 100)
            if tmpDraw < self.breedChance * 100:
                self.breeding(other)
        else:
            if other.specialActionDuringAttack(self, other):
                return
            if self.specialActionDuringAttack(self, other):
                return
            if self.strength >= other.strength:
                self.world.deleteOrganism(other)
                self.makeMove(other.position)
                self.world.komentator.addComment(self.organismToString() + " kills " + other.organismToString())
            else:
                self.world.deleteOrganism(self)
                self.world.komentator.addComment(other.organismToString() + " kills " + self.organismToString())

    def isAnimal(self):
        return True

    def planMove(self):
        tmpDraw = random.randint(0, 100)
        if tmpDraw >= int(self.moveChance * 100):
            return self.position
        else:
            return self.drawAnyField(self.position)

    def action(self):
        for i in range(1, self.moveLength + 1):
            futurePosition = self.planMove()
            if self.world.isTaken(futurePosition) is True and self.world.whatIsOnField(futurePosition) != self:
                self.collision(self.world.whatIsOnField(futurePosition))
                break
            elif self.world.whatIsOnField(futurePosition) != self:
                self.makeMove(futurePosition)
