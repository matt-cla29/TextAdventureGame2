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

def draw_dialogue(surface_to_draw):
    """Handles rendering text depending on the current game state."""
    gold_color = (255, 215, 0)
    white_color = (255, 255, 255)
    
    if current_state == "dialogue":
        # Render standard dialogue line
        text_surf = game_font.render(dialogue_lines[current_line_index], True, white_color)
        text_rect = text_surf.get_rect(center=(400, 500))
        surface_to_draw.blit(text_surf, text_rect)
        
    elif current_state == "choice":
        # Multi-line choice rendering (since \n doesn't work in a single render call)
        choice_lines = [
            "1: start",
            "2: help",
            "3: exit"
        ]

current_line_index = 0
current_state = "dialogue"  # Options: "dialogue", "choice", "response"
selected_branch = []
branch_index = 0
        
        # Render each choice line with vertical offset padding
        for i, line in enumerate(choice_lines):
            color = gold_color if i == 0 else white_color
            text_surf = game_font.render(line, True, color)
            text_rect = text_surf.get_rect(topleft=(50, 410 + (i * 35)))
            surface_to_draw.blit(text_surf, text_rect)