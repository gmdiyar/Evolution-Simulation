from matplotlib import pyplot as plt
from Main import Subject, population

print(len(population))

if __name__ == "__main__":
    for i in range(15):
        population.append(Subject())
        # population[i].printScores()

    for i in range(len(population)):
        x = population[i].returnStartingX()
        y = population[i].returnStartingY()
        plt.scatter(x, y)


plt.show()
