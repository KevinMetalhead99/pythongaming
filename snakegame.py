import pygame
import time
import random

pygame.init()
snake =[]
position = (0,0)
snake.append(position)
for i in snake:
    print(len(snake))
    print(i)
    x = round(random.randrange(0,100))
    y = round(random.randrange(0,100))
    if(len(snake) > 5):
        snake.clear()
    position = (x,y)
    snake.append(position)
@staticmethod
def snakeMove(window):
    pass