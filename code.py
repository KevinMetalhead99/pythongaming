import random

position = (0,0)
snake = []
snake.append(position)

for i in snake:
    print(i)
    if(len(snake) > 5):
        break
    x = round(random.randrange(0,100))
    y = round(random.randrange(0,100))
    position = (x,y)
    snake.append(position)
    

