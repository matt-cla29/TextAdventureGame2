import pygame
import os
import sys

pygame.init()
pygame.font.init()

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


# Load assets (Mocked paths or handled gracefully)
try:
    image_path2 = os.path.join(os.path.dirname(__file__), "images", "island.png")
    surface2 = pygame.image.load(image_path2).convert()
    surface2 = pygame.transform.scale(surface2, (800, 600))
except:
    surface2 = pygame.Surface((800, 600))
    surface2.fill((30, 30, 50))

try:
    image_path3 = os.path.join(os.path.dirname(__file__), "images", "forest.png")
    forest_surface = pygame.image.load(image_path3).convert()
    forest_surface = pygame.transform.scale(forest_surface, (800, 600))
except:
    # Fallback to green color background if the image isn't found
    forest_surface = pygame.Surface((800, 600))
    forest_surface.fill((34, 139, 34))

    dialogue_lines = [
    "you find yourself in front of a forest entrance",
    "you have no idea whats inside...." ]

    choice_responses = {
    "1": ["you decide to go in further....."],
    "2": ["you decide to have a look around the entrance.......", "there is nothing"],
    "3": ["CURRENT OBJECTIVE: find a weapon for the captain"]
}

    current_line_index2 = 0
    current_state2 = "dialogue"  # Options: "dialogue", "choice", "response"
    selected_branch2 = []
    branch_index2 = 0

def draw_dialogue(surface_to_draw2):
    """Handles rendering text depending on the current game state."""
    gold_color = (255, 215, 0)
    white_color = (255, 255, 255)
    
    if current_state2 == "dialogue":
            # Render standard dialogue line
            text_surf = game_font.render(dialogue_lines[current_line_index2], True, white_color)
            text_rect = text_surf.get_rect(center=(400, 500))
            surface_to_draw2.blit(text_surf, text_rect)

    elif current_state2 == "choice":
            # Multi-line choice rendering (since \n doesn't work in a single render call)
            choice_lines = [
                "Select a choice (Press 1, 2, or 3):",
                "1: go in further...",
                "2: have a look around the entrance",
                "3: look at current objective"
            ]

     # Render each choice line with vertical offset padding
            for i, line in enumerate(choice_lines):
                color = gold_color if i == 0 else white_color
                text_surf = game_font.render(line, True, color)
                text_rect = text_surf.get_rect(topleft=(50, 410 + (i * 35)))
                surface_to_draw2.blit(text_surf, text_rect)
                
    elif current_state2 == "response":
            # Adding if selected_branch and branch_index < len(selected_branch): guarantees that your text drawing code will never look for an item in an empty list or look for an element beyond the list's actual size, preventing IndexError entirely.
            if selected_branch and branch_index < len(selected_branch):
                # Render the follow-up text branch after making a choice
                text_surf = game_font.render(selected_branch[branch_index], True, white_color)
                text_rect = text_surf.get_rect(center=(400, 500))
                surface_to_draw2.blit(text_surf, text_rect)
            

# Create a variable tracking which background surface is actively being drawn
current_background = surface2

try:
    image_path = os.path.join(os.path.dirname(__file__), "images", "pirate.png")
    surface = pygame.image.load(image_path).convert_alpha()
except:
    surface = pygame.Surface((100, 150), pygame.SRCALPHA)
    surface.fill((0, 200, 0))

player_rect = surface.get_rect()
player_rect.center = (400, 250)

# Track whether the pirate should be drawn on the screen
draw_pirate = True

# --- DIALOGUE SYSTEM SETUP ---
game_font = pygame.font.Font(None, 32)

dialogue_lines = [
    "WHAT ARE YOU DOING HERE SWASHBUCKLER !?!?!?!",
    "whats that? ...... you're looking for treasure?",
    "well i guess i can let you join......",
    "BUT YOU MUST PROVE YOURSELF WORTHY.....",
    "find me a weapon and i'll let you join our crew" 
]

# Separate branch responses based on the choice picked
choice_responses = {
    "1": ["THATS THE SPIRIT", "go check anywhere you can", "BE QUICK!!!"],
    "2": ["DONT YOU ARGUE AGAINST ME!!!!", "IF YOU WANT TO JOIN THEN GO FIND ME A WEAPON!!"],
    "3": ["not my problem.....", "if you want to join...then go get a weapon"]
}

current_line_index = 0
current_state = "dialogue"  # Options: "dialogue", "choice", "response"
selected_branch = []
branch_index = 0

# Box dimensions
text_box_rect = pygame.Rect(0, 0, 800, 230)
text_box_rect.center = (400, 500)

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
            "Select a choice (Press 1, 2, or 3):",
            "1: I can get you a weapon",
            "2: Why?",
            "3: I don't know where to get a weapon for you"
        ]
        
        # Render each choice line with vertical offset padding
        for i, line in enumerate(choice_lines):
            color = gold_color if i == 0 else white_color
            text_surf = game_font.render(line, True, color)
            text_rect = text_surf.get_rect(topleft=(50, 410 + (i * 35)))
            surface_to_draw.blit(text_surf, text_rect)
            
    elif current_state == "response":
        # Adding if selected_branch and branch_index < len(selected_branch): guarantees that your text drawing code will never look for an item in an empty list or look for an element beyond the list's actual size, preventing IndexError entirely.
        if selected_branch and branch_index < len(selected_branch):
            # Render the follow-up text branch after making a choice
            text_surf = game_font.render(selected_branch[branch_index], True, white_color)
            text_rect = text_surf.get_rect(center=(400, 500))
            surface_to_draw.blit(text_surf, text_rect)
   
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            # STATE 1: Reading regular dialogue lines
            if current_state == "dialogue":
                if event.key == pygame.K_RETURN:
                    current_line_index += 1
                    # If we finish the list, trigger the choice prompt
                    if current_line_index >= len(dialogue_lines):
                        current_state = "choice"

            # STATE 2: Waiting for the player to press 1, 2, or 3
            elif current_state == "choice":
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3]:
                    choice_made = event.unicode if event.unicode in ["1", "2", "3"] else pygame.key.name(event.key)[-1]
                    
                    if choice_made in choice_responses:
                        selected_branch = choice_responses[choice_made]
                        branch_index = 0
                        current_state = "response"

            # STATE 3: Reading the resulting response text path
            elif current_state == "response":
                if event.key == pygame.K_RETURN:
                    branch_index += 1
                    if branch_index >= len(selected_branch):
                        # End conversation or loop back as needed
                        print("thanks for playing")
                        running = False
                 
                 # --- TRANSITION LOGIC HAPPENS HERE ---
                    current_background = forest_surface  # Switch background layout
                    draw_pirate = False                  # Hide the pirate speaker sprite
                    current_state = "gameplay"           # Enter a generic gameplay phase

# 1. Clear display and blit the active background asset variable
    screen.blit(current_background, (0, 0))
    
    # 2. Draw the character sprite only if the active scene flag allows it
    if draw_pirate:
        screen.blit(surface, player_rect)
    
    # 3. Only keep text boxes visible during an active talking state
    if current_state in ["dialogue", "choice", "response"]:
        pygame.draw.rect(screen, (255, 0, 0), text_box_rect)
        draw_dialogue(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()





