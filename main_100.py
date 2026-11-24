import pygame
import os
import inventory
import game
import character
import sys

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Text Example")

# --- ASSETS SETUP ---
try:
    image_path2 = os.path.join(os.path.dirname(__file__), "images", "island.png")
    surface2 = pygame.image.load(image_path2).convert()
    surface2 = pygame.transform.scale(surface2, (800, 600))
except:
    surface2 = pygame.Surface((800, 600))
    surface2.fill((30, 30, 50))

current_background = surface2

try:
    image_path3 = os.path.join(os.path.dirname(__file__), "images", "forest.png")
    forest_surface = pygame.image.load(image_path3).convert()
    forest_surface = pygame.transform.scale(forest_surface, (800, 600))
except:
    forest_surface = pygame.Surface((800, 600))
    forest_surface.fill((34, 139, 34))

try:
    image_path = os.path.join(os.path.dirname(__file__), "images", "pirate.png")
    surface = pygame.image.load(image_path).convert_alpha()
except:
    surface = pygame.Surface((100, 150), pygame.SRCALPHA)
    surface.fill((0, 200, 0))

player_rect = surface.get_rect()
player_rect.center = (400, 250)
draw_pirate = True

game_font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()
running = True

<<<<<<< HEAD:main.py
# --- INVENTORY SETUP ---
inventory = []

=======
>>>>>>> 209b4ff51856440caa3bac210030b431159e91cf:main_100.py
# --- DIALOGUE 1 SETUP (PIRATE) ---
dialogue_lines = [
    "WHAT ARE YOU DOING HERE SWASHBUCKLER !?!?!?!",
    "whats that? ...... you're looking for treasure?",
    "well i guess i can let you join......",
    "BUT YOU MUST PROVE YOURSELF WORTHY.....",
    "find me a weapon and i'll let you join our crew"
]

choice_responses = {
    "1": ["THATS THE SPIRIT", "go check anywhere you can", "BE QUICK!!!"],
    "2": ["DONT YOU ARGUE AGAIN!!!!", "IF YOU WANT TO JOIN THEN GO FIND ME A WEAPON!!"],
    "3": ["not my problem.....", "if you want to join...then go get a weapon"]
}

current_line_index = 0
<<<<<<< HEAD:main.py
current_state = "dialogue"
=======
current_state = "dialogue"  # Options: "dialogue", "choice", "response", "gameplay"
>>>>>>> 209b4ff51856440caa3bac210030b431159e91cf:main_100.py
selected_branch = []
branch_index = 0

# --- DIALOGUE 2 SETUP (FOREST) ---
dialogue_lines2 = [
    "you find yourself in front of a forest entrance",
<<<<<<< HEAD:main.py
    "you have no idea whats inside...."
=======
    "you have no idea whats inside...." 
>>>>>>> 209b4ff51856440caa3bac210030b431159e91cf:main_100.py
]

choice_responses2 = {
    "1": ["you decide to go in further....."],
<<<<<<< HEAD:main.py
    "2": [
        "you look around the entrance.....",
        "you find a sword",
        "(sword goes into your equipment)"
    ],
    "3": ["CURRENT OBJECTIVE: find a weapon for the captain"]
}

current_line_index2 = 0
current_state2 = "dialogue2"
=======
    "2": ["you look around the entrance.....", "you find a sword", "(sword goes into your equipment)"],
    "3": ["CURRENT OBJECTIVE: find a weapon for the captain"] 
}  

current_line_index2 = 0
current_state2 = "dialogue2"  # Options: "dialogue2", "choice2", "response2", "gameplay_finished"
>>>>>>> 209b4ff51856440caa3bac210030b431159e91cf:main_100.py
selected_branch2 = []
branch_index2 = 0

# Box dimensions
text_box_rect = pygame.Rect(0, 0, 800, 230)
text_box_rect.center = (400, 500)


def draw_dialogue(surface_to_draw):
    """Handles rendering text for dialogue 1."""
    gold_color = (255, 215, 0)
    white_color = (255, 255, 255)

    if current_state == "dialogue":
<<<<<<< HEAD:main.py
        text_surf = game_font.render(
            dialogue_lines[current_line_index], True, white_color
        )
=======
        text_surf = game_font.render(dialogue_lines[current_line_index], True, white_color)
>>>>>>> 209b4ff51856440caa3bac210030b431159e91cf:main_100.py
        text_rect = text_surf.get_rect(center=(400, 500))
        surface_to_draw.blit(text_surf, text_rect)

    elif current_state == "choice":
        choice_lines = [
            "Select a choice (Press 1, 2, or 3):",
            "1: I can get you a weapon",
            "2: Why?",
            "3: I don't know where to get a weapon for you"
        ]
<<<<<<< HEAD:main.py

=======
>>>>>>> 209b4ff51856440caa3bac210030b431159e91cf:main_100.py
        for i, line in enumerate(choice_lines):
            color = gold_color if i == 0 else white_color
            text_surf = game_font.render(line, True, color)
            text_rect = text_surf.get_rect(topleft=(50, 410 + (i * 35)))
            surface_to_draw.blit(text_surf, text_rect)

    elif current_state == "response":
        if selected_branch and branch_index < len(selected_branch):
<<<<<<< HEAD:main.py
            text_surf = game_font.render(
                selected_branch[branch_index], True, white_color
            )
            text_rect = text_surf.get_rect(center=(400, 500))
            surface_to_draw.blit(text_surf, text_rect)


=======
            text_surf = game_font.render(selected_branch[branch_index], True, white_color)
            text_rect = text_surf.get_rect(center=(400, 500))
            surface_to_draw.blit(text_surf, text_rect)

>>>>>>> 209b4ff51856440caa3bac210030b431159e91cf:main_100.py
def draw_dialogue2(surface_to_draw2):
    """Handles rendering text for dialogue 2 (Forest)."""
    gold_color = (255, 215, 0)
    white_color = (255, 255, 255)
<<<<<<< HEAD:main.py

    if current_state2 == "dialogue2":
        text_surf = game_font.render(
            dialogue_lines2[current_line_index2], True, white_color
        )
=======
    
    if current_state2 == "dialogue2":
        text_surf = game_font.render(dialogue_lines2[current_line_index2], True, white_color)
>>>>>>> 209b4ff51856440caa3bac210030b431159e91cf:main_100.py
        text_rect = text_surf.get_rect(center=(400, 500))
        surface_to_draw2.blit(text_surf, text_rect)

    elif current_state2 == "choice2":
        choice_lines2 = [
            "Select a choice (Press 1, 2, or 3):",
            "1: go in further...",
            "2: have a look around the entrance",
            "3: look at current objective"
        ]
<<<<<<< HEAD:main.py

=======
>>>>>>> 209b4ff51856440caa3bac210030b431159e91cf:main_100.py
        for i, line in enumerate(choice_lines2):
            color = gold_color if i == 0 else white_color
            text_surf = game_font.render(line, True, color)
            text_rect = text_surf.get_rect(topleft=(50, 410 + (i * 35)))
            surface_to_draw2.blit(text_surf, text_rect)
<<<<<<< HEAD:main.py

    elif current_state2 == "response2":
        if selected_branch2 and branch_index2 < len(selected_branch2):
            text_surf = game_font.render(
                selected_branch2[branch_index2], True, white_color
            )
            text_rect = text_surf.get_rect(center=(400, 500))
            surface_to_draw2.blit(text_surf, text_rect)


=======
                
    elif current_state2 == "response2":
        if selected_branch2 and branch_index2 < len(selected_branch2):
            text_surf = game_font.render(selected_branch2[branch_index2], True, white_color)
            text_rect = text_surf.get_rect(center=(400, 500))
            surface_to_draw2.blit(text_surf, text_rect)

>>>>>>> 209b4ff51856440caa3bac210030b431159e91cf:main_100.py
# --- MAIN GAME LOOP ---
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
<<<<<<< HEAD:main.py

=======
            
>>>>>>> 209b4ff51856440caa3bac210030b431159e91cf:main_100.py
            # --- PHASE 1: PIRATE DIALOGUE ---
            if current_state == "dialogue":

                if event.key == pygame.K_RETURN:
                    current_line_index += 1
<<<<<<< HEAD:main.py

=======
>>>>>>> 209b4ff51856440caa3bac210030b431159e91cf:main_100.py
                    if current_line_index >= len(dialogue_lines):
                        current_state = "choice"

            elif current_state == "choice":

                if event.key in [
                    pygame.K_1, pygame.K_2, pygame.K_3,
                    pygame.K_KP1, pygame.K_KP2, pygame.K_KP3
                ]:

                    choice_made = (
                        event.unicode
                        if event.unicode in ["1", "2", "3"]
                        else pygame.key.name(event.key)[-1]
                    )

                    if choice_made in choice_responses:
                        selected_branch = choice_responses[choice_made]
                        branch_index = 0
                        current_state = "response"

            elif current_state == "response":

                if event.key == pygame.K_RETURN:
                    branch_index += 1

                    if branch_index >= len(selected_branch):
                        print("thanks for playing")
                        print("Moving to forest...")
<<<<<<< HEAD:main.py

=======
                        
>>>>>>> 209b4ff51856440caa3bac210030b431159e91cf:main_100.py
                        # Transition to forest scene
                        current_background = forest_surface
                        draw_pirate = False
                        current_state = "gameplay"
<<<<<<< HEAD:main.py

                        current_state2 = "dialogue2"
                        current_line_index2 = 0

=======
                        current_state2 = "dialogue2"
                        current_line_index2 = 0

>>>>>>> 209b4ff51856440caa3bac210030b431159e91cf:main_100.py
            # --- PHASE 2: FOREST DIALOGUE ---
            elif current_state == "gameplay":
                if current_state2 == "dialogue2":

                    if event.key == pygame.K_RETURN:
                        current_line_index2 += 1
                        if current_line_index2 >= len(dialogue_lines2):
                            current_state2 = "choice2"

                elif current_state2 == "choice2":
<<<<<<< HEAD:main.py

                    if event.key in [
                        pygame.K_1, pygame.K_2, pygame.K_3,
                        pygame.K_KP1, pygame.K_KP2, pygame.K_KP3
                    ]:

                        choice_made = (
                            event.unicode
                            if event.unicode in ["1", "2", "3"]
                            else pygame.key.name(event.key)[-1]
                        )

=======
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3]:
                        choice_made = event.unicode if event.unicode in ["1", "2", "3"] else pygame.key.name(event.key)[-1]
                        
>>>>>>> 209b4ff51856440caa3bac210030b431159e91cf:main_100.py
                        if choice_made in choice_responses2:

                            selected_branch2 = choice_responses2[choice_made]
                            branch_index2 = 0
                            current_state2 = "response2"

                            # --- CHOICE 2: FIND SWORD ---
                            chosen_once = False
                            if choice_made == "2":

                                if "Sword" not in inventory:
                                    inventory.append("Sword")

                                    print("Sword added to inventory!")
                                    print("Current inventory:", inventory)
                                    chosen_once = True

                                if chosen_once == True:
                                    print("You already have a sword!")

                            # --- CHOICE 3: CHECK OBJECTIVE ---
                            elif choice_made == "3":
                                print("Current objective: Find a weapon for the captain")
                                print("Inventory:", inventory)

                elif current_state2 == "response2":

                    if event.key == pygame.K_RETURN:
                        branch_index2 += 1
                        if branch_index2 >= len(selected_branch2):

                            print("Forest dialogue finished")

<<<<<<< HEAD:main.py
                            # Choice 1 goes further into the forest
                            if selected_branch2 == choice_responses2["1"]:
                                current_state2 = "gameplay_finished"

                                print("You are going further into the forest...")

                            # Choices 2 and 3 return to the choices
                            else:
                                current_state2 = "choice2"

                                print("Returning to forest choices...")

    # --- RENDERING SECTION ---
    screen.blit(current_background, (0, 0))

    if draw_pirate:
        screen.blit(surface, player_rect)

    if current_state in ["dialogue", "choice", "response"]:
        pygame.draw.rect(screen, (255, 0, 0), text_box_rect)
        draw_dialogue(screen)

    elif current_state == "gameplay":

        if current_state2 in [
            "dialogue2", "choice2", "response2"
        ]:
            pygame.draw.rect(screen, (255, 0, 0), text_box_rect)
            draw_dialogue2(screen)

=======
    # --- RENDERING SECTION ---
    screen.blit(current_background, (0, 0))
    
    if draw_pirate:
        screen.blit(surface, player_rect)
    
    if current_state in ["dialogue", "choice", "response"]:
        pygame.draw.rect(screen, (255, 0, 0), text_box_rect)
        draw_dialogue(screen)
        
    elif current_state == "gameplay":
        if current_state2 in ["dialogue2", "choice2", "response2"]:
            pygame.draw.rect(screen, (255, 0, 0), text_box_rect)
            draw_dialogue2(screen)
   
>>>>>>> 209b4ff51856440caa3bac210030b431159e91cf:main_100.py
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()