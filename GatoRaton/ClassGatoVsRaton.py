from tablero import tablero

class GatoVsRaton:
    def __init__(self):
        self.board = tablero
        self.raton_pos = (0, 0)  # posición inicial del ratón
        self.gato_pos = (3, 9)   # posición inicial del gato
        
        # Colocar al gato y al ratón
        tablero[0][0] = 'G'
        tablero[7][9] = 'R'
        self.update_board()

    def update_board(self):
        """Actualiza el tablero con las posiciones actuales"""
        self.board = [[" " for _ in range(self.size)] for _ in range(self.size)]
        x_r, y_r = self.raton_pos
        x_g, y_g = self.gato_pos
        if (x_r, y_r) == (x_g, y_g):
            self.board[x_r][y_r] = "X"  # atrapado  
        else:
            self.board[x_r][y_r] = "R"
            self.board[x_g][y_g] = "G"

    def print_board(self):
        """Imprime el tablero en consola"""
        for row in self.board:
            print(" | ".join(row))
            print("-" * (self.size * 4 - 1))

    def valid_moves(self, pos):
        """Devuelve los movimientos válidos desde una posición (x, y)"""
        x, y = pos
        moves = []
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                moves.append((nx, ny))
        return moves

    def move_raton(self, new_pos):
        """Mueve al ratón"""
        if new_pos in self.valid_moves(self.raton_pos):
            self.raton_pos = new_pos
            self.update_board()

    def move_gato(self, new_pos):
        """Mueve al gato"""
        if new_pos in self.valid_moves(self.gato_pos):
            self.gato_pos = new_pos
            self.update_board()

    def is_game_over(self):
        return self.raton_pos == self.gato_pos

    def get_state(self):
        return {
            "gato": self.gato_pos,
            "raton": self.raton_pos
        }