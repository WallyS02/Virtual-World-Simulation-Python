import random
from abc import ABC
import Factory
import Organism


class Plant(Organism.Organism, ABC):
    def __init__(self, organismType, world, position, bornTurn, strength, initiative):
        super().__init__(organismType, world, position, bornTurn, strength, initiative)
        self.breedChance = 0.3

    def spreading(self):
        tmpPoint = self.drawAnyFreeField(self.position)
        if tmpPoint.x == self.position.x and tmpPoint.y == self.position.y:
            return
        else:
            tmpOrganism = Factory.createOrganism(self.organismType, self.world, tmpPoint)
            self.world.komentator.addComment("New plant spreads " + tmpOrganism.organismToString())
            self.world.addOrganism(tmpOrganism)

    def action(self):
        upperbound = 100
        tmpDraw = random.randint(0, upperbound)
        if tmpDraw < self.breedChance * 100:
            self.spreading()

    def isAnimal(self):
        return False

    def collision(self, other):
        pass
