import pygame
import inventory
import main
import character
import os

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Text Example")

# open page

# intro section 
try:
    image_path2 = os.path.join(os.path.dirname(__file__), "images", "island.png")
    surface2 = pygame.image.load(image_path2).convert()
    surface2 = pygame.transform.scale(surface2, (800, 600))
except:
    surface2 = pygame.Surface((800, 600))
    surface2.fill((30, 30, 50))

# Box dimensions
text_box_rect = pygame.Rect(0, 0, 800, 230)
text_box_rect.center = (500, 500)

pygame.draw.rect(screen, (255, 215, 0), text_box_rect)