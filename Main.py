import random
from Const import *

population = []


class FirstGeneration:

    def __init__(self):
        self.desireUp = random.uniform(0, 1)
        self.desireDown = random.uniform(0, 1)
        self.desireLeft = random.uniform(0, 1)
        self.desireRight = random.uniform(0, 1)

        self.xPos = SCREEN_WIDTH / 2
        self.yPos = SCREEN_HEIGHT / 2

    def setNewGenome(self, desireUp, desireDown, desireLeft, desireRight):
        self.desireUp = desireUp
        self.desireDown = desireDown
        self.desireLeft = desireLeft
        self.desireRight = desireRight

    def printGenome(self):
        print(
            {
                "Up": self.desireUp,
                "Down": self.desireDown,
                "Left": self.desireLeft,
                "Right": self.desireRight,
                "Fecundity": self.fecundity,
            }
        )

    def updatePos(self):
        if self.xPos >= SCREEN_WIDTH - 5:
            self.xPos = SCREEN_WIDTH - 5
        elif self.xPos < 100:
            self.xPos = 100
        else:
            self.xPos += self.desireRight - self.desireLeft

        if self.yPos >= SCREEN_HEIGHT - 5:
            self.yPos = SCREEN_HEIGHT - 5
        elif self.yPos < 0:
            self.yPos = 0
        else:
            self.yPos += self.desireDown - self.desireUp

    def decideSurvivors(self, previousPopulation):
        Survivors = []
        for i in range(len(previousPopulation)):
            if (
                previousPopulation[i].xPos > survivingCoditionX
                or previousPopulation[i].yPos > survivingCoditionY
            ):
                Survivors.append(previousPopulation[i])
        population.clear()
        population.extend(Survivors)

    def reproduce(self, population):
        for i in range(len(population)):
            population[i].setNewGenome(
                random.choice(population).desireUp
                + (random.choice(population).desireUp) * random.uniform(0, 1),
                random.choice(population).desireDown
                + (random.choice(population).desireDown) * random.uniform(0, 1),
                random.choice(population).desireLeft
                + (random.choice(population).desireLeft) * random.uniform(0, 1),
                random.choice(population).desireRight
                + (random.choice(population).desireRight) * random.uniform(0, 1),
            )
