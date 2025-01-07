import pygame
from game_state import GameState
from prover9_interface import is_move_safe
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize pygame
pygame.init()
grid_size = (10, 10)
window_size = 500
cell_size = window_size // grid_size[0]
screen = pygame.display.set_mode((window_size, window_size))

# Initial game state
pacman_pos = (5, 5)
food_pos = [(3, 3), (7, 7)]
ghost_pos = [(4, 4), (6, 6)]
game_state = GameState(grid_size, pacman_pos, food_pos, ghost_pos)

def draw_grid(screen, game_state):
    for x in range(game_state.grid_size[0]):
        for y in range(game_state.grid_size[1]):
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (200, 200, 200), rect, 1)
            if (x, y) == game_state.pacman_pos:
                pygame.draw.circle(screen, (255, 255, 0), rect.center, cell_size // 2)
            elif (x, y) in game_state.food_pos:
                pygame.draw.circle(screen, (0, 255, 0), rect.center, cell_size // 4)
            elif (x, y) in game_state.ghost_pos:
                pygame.draw.circle(screen, (255, 0, 0), rect.center, cell_size // 2)

running = True

while running:
    screen.fill((0, 0, 0))
    draw_grid(screen, game_state)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            logging.debug(f"Key pressed: {event.key}")
            new_pos = game_state.pacman_pos
            if event.key == pygame.K_UP:
                new_pos = (game_state.pacman_pos[0], game_state.pacman_pos[1] - 1)
            elif event.key == pygame.K_DOWN:
                new_pos = (game_state.pacman_pos[0], game_state.pacman_pos[1] + 1)
            elif event.key == pygame.K_LEFT:
                new_pos = (game_state.pacman_pos[0] - 1, game_state.pacman_pos[1])
            elif event.key == pygame.K_RIGHT:
                new_pos = (game_state.pacman_pos[0] + 1, game_state.pacman_pos[1])
            
            logging.debug(f"Attempting move to: {new_pos}")
            fol_facts = game_state.to_fol()
            logging.debug(f"Current state in FOL: {fol_facts}")

            if is_move_safe(fol_facts, new_pos): 
                logging.debug(f"Move to new position: {new_pos}") 
                game_state.update_pacman(new_pos)
            else: 
                logging.debug(f"Move to {new_pos} is not safe.")

pygame.quit()
