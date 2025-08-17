import random


class FirstGeneration:

    def __init__(self):
        self.desireUp = random.randint(1, 10)
        self.desireDown = random.randint(1, 10)
        self.desireLeft = random.randint(1, 10)
        self.desireRight = random.randint(1, 100)

        self.fecundity = random.randint(1, 100)

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
            self.xPos += self.desireLeft - self.desireRight + random.randint(1, 10)

        if self.yPos >= 550:
            self.yPos = 550
        elif self.yPos < 50:
            self.yPos = 50
        else:
            self.yPos += self.desireDown - self.desireUp + random.randint(1, 10)


class NextGeneration(FirstGeneration):

    def __init__(self):
        super().__init__()
        self.desireUp = (self.desireUp + random.randint(-100, 100)) % 100
        self.desireDown = (self.desireDown + random.randint(-100, 100)) % 100
        self.desireLeft = (self.desireLeft + random.randint(-100, 100)) % 100
        self.desireRight = (self.desireRight + random.randint(-100, 100)) % 100

        self.fecundity = random.randint(-100, 100)
