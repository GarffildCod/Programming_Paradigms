# - Контекст
# Вероятнее всего, вы с детства знакомы с этой игрой. Пришло
# время реализовать её. Два игрока по очереди ставят крестики
# и нолики на игровое поле. Игра завершается когда кто-то
# победил, либо наступила ничья, либо игроки отказались
# играть.
# - Задача
    
#     Написать игру в “Крестики-нолики”. Можете использовать
#     любые парадигмы, которые посчитаете наиболее
#     подходящими. Можете реализовать доску как угодно - как
#     одномерный массив или двумерный массив (массив массивов).
#     Можете использовать как правила, так и хардкод, на своё
#     усмотрение. Главное, чтобы в игру можно было поиграть через
#     терминал с вашего компьютера.


# игра крестики нолики на Pygame

import pygame
import sys

def check_win(mas, sign):
    zerouse = 0
    for row in mas:
        zerouse+= row.count(0)
        if row.count(sign)==3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
    if mas[0][0] == sign and mas[0][1] == sign and mas[0][2] == sign:
        return sign
    if mas[0][2] == sign and mas[0][1] == sign and mas[0][1] == sign:
        return sign
    if zerouse == 0:
        return 'Piece'
    return False

pygame.init()
size_block = 100
margin = 15
width = heigth = size_block*3 + margin*4

size_window = (width, heigth)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Крестики-Нолики")

black = (0, 0, 0)
red = (250, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0]*3 for i in range(3)]
query = 0  # 1 2 3 4 5 6 7
game_over = False
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif i.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = "x"
                else:
                    mas[row][col] = "o"
                query+=1
        elif i.type == pygame.KEYDOWN and not i.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query = 0
            screen.fill(black)
    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == "x":
                    color = red
                elif mas[row][col] == "o":
                        color = green
                else:
                    color = white
                x = col*size_block + (col+1) * margin
                y = row*size_block + (row+1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == red:
                    pygame.draw.line(screen, white, (x+5, y+5), (x+size_block-5, y+size_block-5),3)
                    pygame.draw.line(screen, white, (x + size_block - 5, y + 5), (x+5, y + size_block - 5), 3)
                elif color == green:
                    pygame.draw.circle(screen, white, (x+size_block//2, y+size_block//2), size_block//2 - 3 , 3)

    if (query -1 ) % 2== 0 : # это x
        game_over = check_win(mas, 'x')
    else:
        game_over = check_win(mas, 'o')

    if game_over:
        screen.fill(black)
        font = pygame.font.SysFont("stxinqkai", 80)
        text1 = font.render(game_over,True,white)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width /2
        text_y = screen.get_height() /2 - text_rect.height / 2
        screen.blit(text1 , [text_x, text_y])
    pygame.display.update()