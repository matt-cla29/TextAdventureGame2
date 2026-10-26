import pygame
import os
import sys
import inventory
import character

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Text Example")

# Load assets
image_path2 = os.path.join(os.path.dirname(__file__), "images", "island.png")
surface2 = pygame.image.load(image_path2).convert()
surface2 = pygame.transform.scale(surface2, (800, 600))

image_path = os.path.join(os.path.dirname(__file__), "images", "pirate.png")
surface = pygame.image.load(image_path).convert_alpha()

player_rect = surface.get_rect()
player_rect.center = (400, 250)

# --- NEW DIALOGUE SYSTEM SETUP ---
game_font = pygame.font.Font(None, 36)

# 1. Store your conversation lines in a list
dialogue_lines = [
    "WHAT ARE YOU DOING HERE SWASHBUCKLER !?!?!?!",
    "whats that? ...... you're looking for treasure?",
    "well i guess i can let you join......",
    "BUT YOU MUST PROVE YOURSELF WORTHY.....",#
    "find me a weapon and i'll let you join our crew"  
]

# 2. Track which line the player is currently reading
current_line_index = 0

# 3. Create a helper function to render the current text line
def get_current_text_surface(index):
    # Safe check: if we go past the last line, show a default message or stop
    if index < len(dialogue_lines):
        return game_font.render(dialogue_lines[index], True, (255, 255, 255))
    else:
        return game_font.render("find me a weapon and i'll let you join our crew", True, (255, 255, 255))

user_choice1 = input("select a choice: \n 1: i can get you a weapon \n 2: why? \n 3: i dont know where to get a weapon for you")

if user_choice1 == "1":
    dialogue_lines2 = [
    "well what are you waiting for?, FIND ME A WEAPON!!!"   
]
    # 3. Create a helper function to render the current text line
def get_current_text_surface(index):
    # Safe check: if we go past the last line, show a default message or stop
    if index < len(dialogue_lines2):
        return game_font.render(dialogue_lines2[index], True, (255, 255, 255))
    else:
        return game_font.render("[end conversation]", True, (255, 255, 255))

# Generate the initial first line of text
text_surface = get_current_text_surface(current_line_index)
text_rect = text_surface.get_rect()
text_rect.center = (400, 550)

# Box dimensions
text_box_rect = pygame.Rect(0, 0, 550, 70)
text_box_rect.center = (400, 550)
# ---------------------------------

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 4. Listen for the Enter key press event
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # K_RETURN is the Enter key
                # Move to the next line
                current_line_index += 1
                
                # Update the text surface with the new text line
                text_surface = get_current_text_surface(current_line_index)
                
                # Re-center the bounding box because text lengths change
                text_rect = text_surface.get_rect()
                text_rect.center = (400, 550)

    # 1. Draw background
    screen.blit(surface2, (0, 0))

    # 2. Draw player
    screen.blit(surface, player_rect)
    
    # 3. Draw the solid red text box container
    pygame.draw.rect(screen, (255, 0, 0), text_box_rect)
    
    # 4. Draw the dynamic text over it
    screen.blit(text_surface, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()




