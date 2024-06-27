import sys
import pygame
import numpy as np

pygame.init()

white=(255,255,255)
grey=(180,180,180)
red=(255,0,0)
green=(0,255,0)
black=(0,0,0)

width=300
height=300
line_width=5
board_row=3
board_col=3
square=width//board_row
circle_rad= square//3
circle_width=15
cross_width=25

screen=pygame.display.set_mode(width,height)
pygame.display.set_caption("TIC TAC TOE AI")
screen.fill(black)

board= np.zeros((board_row,board_col))

def draw_lines(color=white):
    for i in range(1,board_row):
        pygame.draw.line(screen,color,(0,square*i),(width,square*i))
        pygame.draw.line(screen,color,(square*i,0),(square*i,width))

def draw_figures(color=white):
    for row in range(board_row): 
        for col in range(board_col):
            if board[row][col]== 1:
                pygame.draw.circle(screen, color, (int(col*square+square//2), int(row*square+square//2)), circle_rad,circle_width)
            elif board[row][col]==2:
                pygame.draw.line(screen, color,(col * square + square // 4, row* square + square // 4), (col * square + 3 * square // 4,row * square + 3 * square // 4))
                pygame.draw.line(screen, color,(col * square + square // 4, row* square + 3*square // 4), (col * square + 3 * square // 4,row * square + square // 4))

def mark_sq(row,col,player):
    board[row][col]= player

def available_sq(row,col):
    return board[row][col] == 0

def isboardfull(check_board=board):
    for row in range(board_row):
        for col in range (board_col):
            if check_board[row][col] == 0:
                return True
    return False

def check_win(player, check_board):
    for col in range(board_col):
        if check_board[0][col]==player and check_board[1][col]==player and check_board[2][col]== player:
            return True
    for row in range(board_row):
        if check_board[row][0]==player and check_board[row][1]==player and check_board[row][2]== player:
            return True    
    if check_board[0][0]== player and check_board[1][1]== player and check_board[2][2]== player:
        return True
    if check_board[0][2]== player and check_board[1][1]== player and check_board[2][0]== player:
        return True
    return False