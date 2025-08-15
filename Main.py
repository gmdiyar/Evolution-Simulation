import random


class Subject:

    def __init__(self):
        self.sight = random.randint(1, 100)
        self.hearing = random.randint(1, 100)
        self.agility = random.randint(1, 100)
        self.strength = random.randint(1, 100)
        self.fecundity = random.randint(1, 100)

        self.startingX = random.randint(1, 50)
        self.startingY = random.randint(1, 50)

    def returnStartingX(self):
        return self.startingX

    def returnStartingY(self):
        return self.startingY

    def printScores(self):
        print(
            {
                "Sight": self.sight,
                "Hearing": self.hearing,
                "Agility": self.agility,
                "Strength": self.strength,
                "Fecundity": self.fecundity,
            }
        )


def setSurvivalCondition():
    pass


population = []

if __name__ == "__main__":
    for i in range(15):
        population.append(Subject())
        # population[i].printScores()
