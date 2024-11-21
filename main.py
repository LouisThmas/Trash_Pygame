import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Platform Game")

WIDTH, HEIGHT = 1000, 800
FPS = 60
window = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load('abstract.png')
guy = pygame.image.load("good_ship.png").convert_alpha()
heart = pygame.image.load("heart2.png").convert_alpha()
villain = pygame.image.load("enemy_ship.png").convert_alpha()

def postion_change(bullet):
    bullet[1] -= 5
    return bullet
    

class Bullets():
    def __init__(self):
        self.bullets = []
        self.weapon_mask = pygame.mask.from_surface(heart)
    
    def update(self, player_pos_x = 0, player_pos_y = 0, is_added = False):
        
        self.bullets = list(map(postion_change, self.bullets))
        
        if is_added:
            self.bullets.append([player_pos_x, player_pos_y])
            
        self.bullets = [bullet for bullet in self.bullets if bullet[1] > 0]
        
    def display(self, bullet):
        for elem in self.bullets:
            bullet.center = (elem[0], elem[1])
            window.blit(heart, bullet)
            
    def is_strike(self, enemy_ship_mask, enemy_ship):
        for elem in self.bullets:
            if self.weapon_mask.overlap(enemy_ship_mask, (elem[0] - enemy_ship.x, elem[1] - enemy_ship.y)):
                self.bullets.remove(elem)
        
def main(window):
    
    clock = pygame.time.Clock()
    run = True

    player2 = guy.get_rect()
    player2.center = (500, 600)
    player2_mask = pygame.mask.from_surface(guy)
    
    weapon = heart.get_rect()
    
    ennemy_ship = villain.get_rect()
    ennemy_ship.center = (500, 200)
    ennemy_ship_mask = pygame.mask.from_surface(villain)
    
    pygame.draw.rect(window, (0,0,0), weapon)
    pygame.draw.rect(window, (0,0,0), player2)
    pygame.draw.rect(window, (0,0,0), ennemy_ship)
    
    bullet_list = Bullets()
    bullet_delay = 0

    
    while (run):
        clock.tick(FPS)
        pygame.display.update()

        window.blit(background, (0, 0))
        
        window.blit(guy, player2)
        
        
        window.blit(villain, ennemy_ship)
        
        
        bullet_list.display(weapon)
        
        is_bullet_added = False
        
        if player2_mask.overlap(ennemy_ship_mask, (player2.x - 500, player2.y - 200)):
            player2.y += 200
            
        bullet_list.is_strike(ennemy_ship_mask, ennemy_ship)
        
        key = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        if key[pygame.K_d] and player2.x < 968:
            player2.move_ip(10, 0)
        if key[pygame.K_a] and player2.x > 0:
            player2.move_ip(-10, 0)
        if key[pygame.K_w] and player2.y > 0:
            player2.move_ip(0, -10)
        if key[pygame.K_s] and player2.y < 768:
            player2.move_ip(0, 10)
        if mouse[0]:
            if bullet_delay == 0:
                is_bullet_added = True
                bullet_delay = 20
            bullet_delay -= 1
        if mouse[0] == False:
            bullet_delay = 0
                

        bullet_list.update(player2.x, player2.y, is_bullet_added)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break 
                
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)