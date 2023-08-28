import pygame
from pygame.locals import *

# 初始化游戏引擎
pygame.init()

# 设置窗口尺寸
screen = pygame.display.set_mode((800, 600))

# 加载游戏背景
background = pygame.image.load("background.png").convert()

# 加载球和挡板
ball = pygame.image.load("ball.png").convert()
ball.set_colorkey((255, 255, 255))  # 设置透明色

paddle = pygame.image.load("paddle.png").convert()
paddle.set_colorkey((255, 255, 255))  # 设置透明色

# 设置球和挡板的初始位置
ball_x = 400
ball_y = 300
paddle_x = 350
paddle_y = 550

# 设置球的初始速度
ball_dx = 5
ball_dy = 5

# 主游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # 移动挡板
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        paddle_x -= 5
    if keys[K_RIGHT]:
        paddle_x += 5

    # 移动球
    ball_x += ball_dx
    ball_y += ball_dy

    # 球与窗口边界的碰撞检测
    if ball_x < 0 or ball_x > 780:
        ball_dx = -ball_dx
    if ball_y < 0 or ball_y > 580:
        ball_dy = -ball_dy

    # 球与挡板的碰撞检测
    if ball.colliderect(paddle):
        ball_dy = -ball_dy

    # 渲染背景
    screen.blit(background, (0, 0))

    # 渲染球和挡板
    screen.blit(ball, (ball_x, ball_y))
    screen.blit(paddle, (paddle_x, paddle_y))

    pygame.display.update()

# 退出游戏
pygame.quit()
