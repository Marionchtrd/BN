import pygame
import random
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres du jeu
board_size = 10
cell_size = 50
num_ships = 5
width = board_size * cell_size
height = board_size * cell_size
font = pygame.font.Font(None, 36)

# Couleurs
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Création de la fenêtre
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bataille Navale")

# Fonction pour créer une grille vide
def create_board(size):
    return [['O' for _ in range(size)] for _ in range(size)]

# Fonction pour placer les navires de manière aléatoire
def place_ships(board, num_ships):
    for _ in range(num_ships):
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - 1)
        while board[row][col] == 'S':
            row = random.randint(0, len(board) - 1)
            col = random.randint(0, len(board[0]) - 1)
        board[row][col] = 'S'

# Fonction pour afficher la grille
def display_board(board):
    for row in range(board_size):
        for col in range(board_size):
            pygame.draw.rect(screen, white, (col * cell_size, row * cell_size, cell_size, cell_size), 2)
            if board[row][col] == 'X':
                pygame.draw.line(screen, red, (col * cell_size, row * cell_size), ((col + 1) * cell_size, (row + 1) * cell_size), 2)
                pygame.draw.line(screen, red, (col * cell_size, (row + 1) * cell_size), ((col + 1) * cell_size, row * cell_size), 2)
            elif board[row][col] == 'S':
                pygame.draw.circle(screen, red, (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2), cell_size // 2, 2)

# Fonction principale du jeu
def battleship_game():
    board = create_board(board_size)
    place_ships(board, num_ships)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row = pos[1] // cell_size
                col = pos[0] // cell_size
                if board[row][col] == 'S':
                    print("Félicitations ! Vous avez touché un navire !")
                    board[row][col] = 'X'
                    if all('S' not in row for row in board):
                        print("Félicitations ! Vous avez coulé tous les navires !")
                        pygame.quit()
                        sys.exit()
                else:
                    print("Dommage, vous avez manqué.")

        screen.fill(black)
        display_board(board)
        pygame.display.flip()

if __name__ == "__main__":
    battleship_game()
    