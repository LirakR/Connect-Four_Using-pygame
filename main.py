import pygame, os, sys
import board as b
import ctypes
import numpy as np

pygame.init()


WIDTH = 1000  
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
disc_radius = int(HEIGHT/20)
board_rect_width = int(HEIGHT/8)
board_x = (WIDTH - board_rect_width*b.get_columns())/2
board_y = (HEIGHT - board_rect_width*b.get_rows())*0.8


# Colors
bg_color = (0,0,0)
player1_color =(0,0,255)
player2_color = (255,0,0)
board_color = (51,255,153)
hover_color = (255,255,0)

# Variables
FPS = 60


pygame.display.set_caption('Connect Four Game')
def update_screen(array, mouse, turn):
    screen.fill(bg_color)
    draw_board(array)
    show_disc(array)
    font = pygame.font.SysFont('Arial',int(HEIGHT/20) )
    text1 = font.render('PLAYER 1', False, player1_color)
    text2 = font.render('PLAYER 2', False, player2_color)
    screen.blit(text1, (board_x,HEIGHT/12))
    screen.blit(text2, (board_x+board_rect_width*b.get_columns()-int(HEIGHT/5),HEIGHT/12))
    if(turn)%2==0:
        column_hover(mouse[0],mouse[1],player1_color)
    else:
        column_hover(mouse[0],mouse[1],player2_color)
    pygame.display.update()

def main():
    board = b.get_board()
    turn=1
    clock = pygame.time.Clock()
    running = True
    while running:
        if b.check_winner(board):
            print("The winner is player: "+ str(turn%2+1))
            board = np.zeros((6, 7))
            answer= ctypes.windll.user32.MessageBoxW(0, "The winner is PLAYER: "+ str(turn%2+1)+ ". Do u want to play again?", "Well Done", 1)
            turn = 1
            if answer == 2:
                pygame.quit()
                sys.exit(0)
        clock.tick(FPS)
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if not b.check_zeros_in_column(board,column_clicked(pos[0],pos[1])) and column_clicked(pos[0],pos[1])!=-1:
                        turn=turn+1
                if column_clicked(pos[0],pos[1])!=-1:
                    if turn%2 == 0:
                        b.play_here(board, 1, column_clicked(pos[0],pos[1]))
                        
                    else:
                        b.play_here(board, 2, column_clicked(pos[0],pos[1]))
                    
                print(turn%2+1)
                print(board)
            
        update_screen(board,pos, turn+1)
    pygame.quit()

def show_disc(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == 1:
                pygame.draw.circle(screen, player1_color, (board_x+(j*board_rect_width)+board_rect_width/2,board_y+(i*board_rect_width)+board_rect_width/2),disc_radius,0)
            elif array[i][j] == 2:
                pygame.draw.circle(screen, player2_color,(board_x+(j*board_rect_width)+board_rect_width/2,board_y+(i*board_rect_width)+board_rect_width/2),disc_radius,0)

def draw_board(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            pygame.draw.rect(screen, board_color,(board_x+(j*board_rect_width), board_y+(i*board_rect_width), board_rect_width , board_rect_width), 0)
            pygame.draw.circle(screen, bg_color,(board_x+(j*board_rect_width)+board_rect_width/2,board_y+(i*board_rect_width)+board_rect_width/2),disc_radius,0)


def column_clicked(posx, posy):
    for i in range(7):
        if posx>board_x+i*board_rect_width and posx<board_x + (i+1)*board_rect_width and posy>board_y and posy<board_y+board_rect_width*6:
            return i+1
    return -1

def column_hover(posx, posy, hover_color):
    for i in range(7):
        if posx>board_x+i*board_rect_width and posx<board_x + (i+1)*board_rect_width and posy>board_y and posy<board_y+board_rect_width*6:
            pygame.draw.rect(screen, hover_color, (board_x+i*board_rect_width-5, board_y-5, board_rect_width+10,board_rect_width*b.get_rows()+10), 2)


def all_zeros():
    board = np.zeros((6, 7))

main()
