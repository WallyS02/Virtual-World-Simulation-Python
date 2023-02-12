import Rosliny.Grass
import Rosliny.Guarana
import Rosliny.Hogweed
import Rosliny.Dandelion
import Rosliny.WolfBerries
import Zwierzeta.Wolf
import Zwierzeta.Human
import Zwierzeta.Fox
import Zwierzeta.Antelope
import Zwierzeta.Cybersheep
import Zwierzeta.Turtle
import Zwierzeta.Sheep
import Organism


def createOrganism(organismType, world, position):
    if organismType == Organism.Organism.OrganismType.wolf:
        return Zwierzeta.Wolf.Wolf(world, position, world.turnNumber)
    elif organismType == Organism.Organism.OrganismType.sheep:
        return Zwierzeta.Sheep.Sheep(world, position, world.turnNumber)
    elif organismType == Organism.Organism.OrganismType.fox:
        return Zwierzeta.Fox.Fox(world, position, world.turnNumber)
    elif organismType == Organism.Organism.OrganismType.turtle:
        return Zwierzeta.Turtle.Turtle(world, position, world.turnNumber)
    elif organismType == Organism.Organism.OrganismType.antelope:
        return Zwierzeta.Antelope.Antelope(world, position, world.turnNumber)
    elif organismType == Organism.Organism.OrganismType.human:
        return Zwierzeta.Human.Human(world, position, world.turnNumber)
    elif organismType == Organism.Organism.OrganismType.cybersheep:
        return Zwierzeta.Cybersheep.Cybersheep(world, position, world.turnNumber)
    elif organismType == Organism.Organism.OrganismType.grass:
        return Rosliny.Grass.Grass(world, position, world.turnNumber)
    elif organismType == Organism.Organism.OrganismType.dandelion:
        return Rosliny.Dandelion.Dandelion(world, position, world.turnNumber)
    elif organismType == Organism.Organism.OrganismType.guarana:
        return Rosliny.Guarana.Guarana(world, position, world.turnNumber)
    elif organismType == Organism.Organism.OrganismType.wolfBerries:
        return Rosliny.WolfBerries.WolfBerries(world, position, world.turnNumber)
    elif organismType == Organism.Organism.OrganismType.hogweed:
        return Rosliny.Hogweed.Hogweed(world, position, world.turnNumber)
    else:
        return None
