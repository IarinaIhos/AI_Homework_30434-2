class GameState:
    def __init__(self, grid_size, pacman_pos, food_pos, ghost_pos):
        self.grid_size = grid_size
        self.pacman_pos = pacman_pos
        self.food_pos = food_pos
        self.ghost_pos = ghost_pos

    def to_fol(self):
        facts = [f"Pacman({self.pacman_pos[0]},{self.pacman_pos[1]})."]
        for food in self.food_pos:
            facts.append(f"Food({food[0]},{food[1]}).")
        for ghost in self.ghost_pos:
            facts.append(f"Ghost({ghost[0]},{ghost[1]}).")
        return facts

    def update_pacman(self, new_pos):
        self.pacman_pos = new_pos
