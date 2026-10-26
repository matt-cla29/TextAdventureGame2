import pygame
import os
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Text Example")

# Load the island background
image_path2 = os.path.join(os.path.dirname(__file__), "images", "island.png")
surface2 = pygame.image.load(image_path2).convert()
surface2 = pygame.transform.scale(surface2, (800, 600))

# Load the pirate player
image_path = os.path.join(os.path.dirname(__file__), "images", "pirate.png")
surface = pygame.image.load(image_path).convert_alpha()

# Set the pirate's position
player_rect = surface.get_rect()
player_rect.center = (400, 250)



clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background first
    screen.blit(surface2, (0, 0))

    # Draw the pirate on top of the background
    screen.blit(surface, player_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
 

