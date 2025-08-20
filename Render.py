import pygame
from Const import *
from Main import *

pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GUI = pygame.surface.Surface((100, 600))
clock = pygame.time.Clock()
running = True

if __name__ == "__main__":
    for i in range(30000):
        first = FirstGeneration()
        population.append(first)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(first.decideSurvivors(population))
            first.reproduce(population)

    SCREEN.fill(white)
    GUI.fill(grey)

    pygame.draw.rect(GUI, white, (15, 15, 70, 20), 0, 3, 3, 3, 3)

    for i in range(len(population)):
        pygame.draw.rect(SCREEN, black, (population[i].xPos, population[i].yPos, 5, 5))
        population[i].updatePos()

    # print(population[i].xPos, population[i].yPos)

    pygame.Surface.blit(SCREEN, GUI, (0, 0))
    pygame.display.flip()
    clock.tick(120)

pygame.quit()
