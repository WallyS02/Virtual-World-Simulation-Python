import random
import Factory
import Komentator
import Organism
import Point


class World:
    def __init__(self, sizeX, sizeY, gui):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.gui = gui
        self.turnNumber = 0
        self.isHumanAlive = True
        self.isEndOfGame = False
        self.pause = True
        self.komentator = Komentator.Komentator()
        self.board = [[0 for row in range(sizeX)] for col in range(sizeY)]
        for i in range(sizeX):
            for j in range(sizeY):
                self.board[j][i] = None
        self.organisms = list()
        self.human = None

    def saveWorld(self, nameOfFile):
        nameOfFile += ".txt"
        file = open(nameOfFile, "x")
        file.write(str(self.sizeX) + " ")
        file.write(str(self.sizeY) + " ")
        file.write(str(self.turnNumber) + " ")
        tmpIsHumanAlive = int(self.isHumanAlive)
        file.write(str(tmpIsHumanAlive) + " ")
        tmpIsEndOfGame = int(self.isEndOfGame)
        file.write(str(tmpIsEndOfGame) + "\n")
        for i in range(len(self.organisms)):
            orgType = int(self.organisms[i].organismType)
            file.write(str(orgType) + " ")
            file.write(str(self.organisms[i].position.x) + " ")
            file.write(str(self.organisms[i].position.y) + " ")
            file.write(str(self.organisms[i].strength) + " ")
            file.write(str(self.organisms[i].bornTurn) + " ")
            tmpIsDead = int(self.organisms[i].isDead)
            file.write(str(tmpIsDead) + " ")
            if orgType == Organism.Organism.OrganismType.human:
                file.write(str(self.human.cooldown) + " ")
            file.write('\n')
        file.close()

    def loadWorld(self, nameOfFile):
        nameOfFile = nameOfFile + ".txt"
        file = open(nameOfFile, "r")
        firstLine = file.readline()
        properties = firstLine.split(" ")
        sizeX = int(properties[0])
        sizeY = int(properties[1])
        tmpWorld = World(sizeX, sizeY, None)
        tmpWorld.turnNumber = int(properties[2])
        tmpIsHumanAlive = int(properties[3])
        tmpWorld.isHumanAlive = bool(tmpIsHumanAlive)
        tmpIsEndOfGame = int(properties[4])
        tmpWorld.isEndOfGame = bool(tmpIsEndOfGame)
        tmpWorld.human = None
        for x in file:
            properties = x.split(" ")
            organismType = int(properties[0])
            x = int(properties[1])
            y = int(properties[2])
            tmpOrganism = Factory.createOrganism(organismType, tmpWorld, Point.Point(x, y))
            strength = int(properties[3])
            tmpOrganism.strength = strength
            bornTurn = int(properties[4])
            tmpOrganism.bornTurn = bornTurn
            tmpIsDead = int(properties[5])
            isDead = bool(tmpIsDead)
            tmpOrganism.isDead = isDead
            if organismType == Organism.Organism.OrganismType.human:
                tmpWorld.human = tmpOrganism
                cooldown = int(properties[6])
                tmpWorld.human.cooldown = cooldown
            tmpWorld.addOrganism(tmpOrganism)
        file.close()
        return tmpWorld

    def drawFreeField(self):
        for i in range(self.sizeX):
            for j in range(self.sizeY):
                if self.board[j][i] is None:
                    while True:
                        x = random.randint(0, self.sizeX - 1)
                        y = random.randint(0, self.sizeY - 1)
                        if self.board[j][i] is None:
                            return Point.Point(x, y)
        return Point.Point(-1, -1)

    def createWorld(self):
        numberOfOrganisms = int(self.sizeX * self.sizeY / 3)
        position = self.drawFreeField()
        tmpOrganism = Factory.createOrganism(Organism.Organism.OrganismType.human, self, position)
        self.human = tmpOrganism
        self.addOrganism(self.human)
        for i in range(numberOfOrganisms):
            position = self.drawFreeField()
            if position.x != -1 and position.y != -1:
                self.addOrganism(Factory.createOrganism(Organism.Organism.drawType(tmpOrganism), self, position))
            else:
                return

    def makeTurn(self):
        if self.isEndOfGame is True:
            return
        self.turnNumber += 1
        self.komentator.addComment("\nTURN " + str(self.turnNumber))
        self.organisms.sort(key=lambda x: x.initiative, reverse=True)
        if self.human is not None:
            if self.human.cooldown > 5:
                self.human.strength = self.human.strength - 1
            if self.human.cooldown > 0:
                self.human.cooldown = self.human.cooldown - 1
        for i in range(len(self.organisms)):
            if self.organisms[i].bornTurn != self.turnNumber and self.organisms[i].isDead is False:
                self.organisms[i].action()

        for organism in self.organisms:
            if organism.isDead is True:
                self.organisms.remove(organism)

        for i in range(len(self.organisms)):
            self.organisms[i].didMultiplied = False

    def isTaken(self, field):
        if self.board[field.y][field.x] is not None:
            return True
        return False

    def whatIsOnField(self, field):
        return self.board[field.y][field.x]

    def addOrganism(self, organism):
        self.organisms.append(organism)
        self.board[organism.position.y][organism.position.x] = organism

    def deleteOrganism(self, organism):
        self.board[organism.position.y][organism.position.x] = None
        organism.isDead = True
        if organism.organismType == Organism.Organism.OrganismType.human:
            self.isHumanAlive = False
            self.human = None

    def isHogweedOnMap(self):
        for i in range(self.sizeX):
            for j in range(self.sizeY):
                if self.board[j][i] is not None and self.board[j][i].organismType == Organism.Organism.OrganismType.hogweed:
                    return True
        return False
