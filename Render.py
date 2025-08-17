import pygame
from Const import *
from Main import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

if __name__ == "__main__":
    for i in range(15):
        first = FirstGeneration()
        population.append(first)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    for i in range(len(population)):
        pygame.draw.rect(screen, black, (population[i].xPos, population[i].yPos, 5, 5))
        population[i].updatePos()

    print(population[i].xPos, population[i].yPos)
    pygame.display.flip()

    clock.tick(10)

pygame.quit()
