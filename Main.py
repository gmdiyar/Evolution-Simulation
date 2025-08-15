import random


class FirstGeneration:

    def __init__(self):
        self.desireUp = random.randint(1, 100)
        self.desireDown = random.randint(1, 100)
        self.desireLeft = random.randint(1, 100)
        self.desireRight = random.randint(1, 100)

        self.fecundity = random.randint(1, 100)

        self.startingX = random.randint(1, 50)
        self.startingY = random.randint(1, 50)

    def returnStartingX(self):
        return self.startingX

    def returnStartingY(self):
        return self.startingY

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

    def setSurvivalCondition():
        pass


class NextGeneration(FirstGeneration):

    def __init__(self):
        super().__init__()
        self.desireUp = (self.desireUp + random.randint(-100,100)) % 100
        self.desireDown = (self.desireDown + random.randint(-100,100)) % 100
        self.desireLeft = (self.desireLeft + random.randint(-100,100)) % 100
        self.desireRight = (self.desireRight + random.randint(-100,100)) % 100

        self.fecundity = random.randint(-100,100) 



population = []

if __name__ == "__main__":
    #for i in range(15):
       #population.append(FirstGeneration())
        #population[i].printGenome()
        first = FirstGeneration()
        first.printGenome()
        second = NextGeneration()
        second.printGenome()