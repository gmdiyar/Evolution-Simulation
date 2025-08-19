import random

population = []


class FirstGeneration:

    def __init__(self):
        self.desireUp = random.uniform(0, 1)
        self.desireDown = random.uniform(0, 1)
        self.desireLeft = random.uniform(0, 1)
        self.desireRight = random.uniform(0, 1)

        self.fecundity = random.uniform(0, 1)

        self.xPos = 400
        self.yPos = 300

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
        if self.xPos >= 750:
            self.xPos = 750
        elif self.xPos < 50:
            self.xPos = 50
        else:
            self.xPos += self.desireLeft - self.desireRight

        if self.yPos >= 550:
            self.yPos = 550
        elif self.yPos < 50:
            self.yPos = 50
        else:
            self.yPos += self.desireDown - self.desireUp


class NextGeneration(FirstGeneration):

    def __init__(self):
        super().__init__()
        self.desireUp = (self.desireUp + random.randint(-100, 100)) % 100
        self.desireDown = (self.desireDown + random.randint(-100, 100)) % 100
        self.desireLeft = (self.desireLeft + random.randint(-100, 100)) % 100
        self.desireRight = (self.desireRight + random.randint(-100, 100)) % 100

        self.fecundity = random.randint(-100, 100)
