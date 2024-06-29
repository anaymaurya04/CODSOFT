import sys
import pygame
import numpy as np

pygame.init()

# Colors
white = (255, 255, 255)
grey = (180, 180, 180)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# Game settings
width = 300
height = 300
line_width = 5
board_row = 3
board_col = 3
square = width // board_row
circle_rad = square // 3
circle_width = 15
cross_width = 25

# Pygame setup
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("TIC TAC TOE AI")
screen.fill(black)

# Game board
board = np.zeros((board_row, board_col))

def draw_lines(color=white):
    for i in range(1, board_row):
        pygame.draw.line(screen, color, (0, square * i), (width, square * i), line_width)
        pygame.draw.line(screen, color, (square * i, 0), (square * i, width), line_width)

def draw_figures(color=white):
    for row in range(board_row): 
        for col in range(board_col):
            if board[row][col] == 1:
                pygame.draw.circle(screen, color, (int(col * square + square // 2), int(row * square + square // 2)), circle_rad, circle_width)
            elif board[row][col] == 2:
                pygame.draw.line(screen, color, (col * square + square // 4, row * square + square // 4), (col * square + 3 * square // 4, row * square + 3 * square // 4), cross_width)
                pygame.draw.line(screen, color, (col * square + square // 4, row * square + 3 * square // 4), (col * square + 3 * square // 4, row * square + square // 4), cross_width)

def mark_sq(row, col, player):
    board[row][col] = player

def available_sq(row, col):
    return board[row][col] == 0

def is_board_full():
    return not np.any(board == 0)

def check_win(player):
    for col in range(board_col):
        if all(board[:, col] == player):
            return True
    for row in range(board_row):
        if all(board[row, :] == player):
            return True    
    if board[0, 0] == player and board[1, 1] == player and board[2, 2] == player:
        return True
    if board[0, 2] == player and board[1, 1] == player and board[2, 0] == player:
        return True
    return False

def minimax(minimax_board, depth, is_maximizing):
    if check_win(2):
        return float('inf')
    elif check_win(1):
        return float('-inf')
    elif is_board_full():
        return 0
    
    if is_maximizing:
        best_score = -1000
        for row in range(board_row):
            for col in range(board_col):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 2
                    score = minimax(minimax_board, depth + 1, False)
                    minimax_board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for row in range(board_row):
            for col in range(board_col):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 1
                    score = minimax(minimax_board, depth + 1, True)
                    minimax_board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score
    
def best_move():
    best_score = -1000
    move = (-1, -1)
    for row in range(board_row):
        for col in range(board_col):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(board, 0, False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    move = (row, col)

    if move != (-1, -1):
        mark_sq(move[0], move[1], 2)
        return True
    return False

def restart():
    screen.fill(black)
    draw_lines()
    for row in range(board_row):
        for col in range(board_col):
            board[row][col] = 0

draw_lines()

player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            row = mouseY // square
            col = mouseX // square

            if available_sq(row, col):
                mark_sq(row, col, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1

            if not game_over:
                if best_move():
                    if check_win(2):
                        game_over = True
                    player = player % 2 + 1

            if not game_over and is_board_full():
                game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False
                player = 1

    if not game_over:
        draw_figures()
    else:
        if check_win(1):
            draw_figures(green)
            draw_lines(green)
        elif check_win(2):
            draw_figures(red)
            draw_lines(red)
        else:
            draw_figures(grey)
            draw_lines(grey)

    pygame.display.update()
