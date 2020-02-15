import pygame
from plane_sprites import *
pygame.init()

#创建游戏窗口
screen = pygame.display.set_mode((480,700))
#绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
#英雄飞机
hero =pygame.image.load("./images/me1.png")
screen.blit(hero,(200,500))
pygame.display.update()

clock = pygame.time.Clock()
hero_rect = pygame.Rect(150,300,102,124)

#敌机精灵
enemy = GameSprites("./images/enemy1.png",1)
enemy1 = GameSprites("./images/enemy1.png",2)

#敌机精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)


while True:
    clock.tick(60)
    hero_rect.y -=10
    if hero_rect.y <= -126:
        hero_rect.y = 700
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏")
            pygame.quit()
            exit()
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)

    enemy_group.update()
    enemy_group.draw(screen)

    pygame.display.update()

pygame.quit()