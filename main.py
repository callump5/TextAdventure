from characters import *
from items import *
import combat
import pygame
import time
from colours import *
from story import story_ground

pygame.init()

columns, rows = 50, 50
cell_size = 10
screen = pygame.display.set_mode([800,600])
screen.fill(white)
pygame.display.set_caption("My program")

basicfont = pygame.font.SysFont(None, 48)

screen.fill((255, 255, 255))

pygame.display.update()

index = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            index += 1
            text = basicfont.render(story_ground[index], True, (255, 0, 0), (255, 255, 255))
            textrect = text.get_rect()
            textrect.centerx = screen.get_rect().centerx
            textrect.centery = screen.get_rect().centery
            screen.blit(text, textrect)
            pygame.display.update()

    pygame.display.update()






'''
me = characters.c
you = characters.e
you.update_stats()
me.update_stats()

answer = raw_input('Y/N')
if answer == 'y':
    weapons[1].equip(me)
elif answer == 'n':
    print 'Do you want the dagger then?'
    answer = raw_input('Y/N')
    if answer == 'y':
        print weapons[0].equip(me)
    elif answer == 'n':
        print 'Then take the gladius!'
        weapons[1].equip(me)
print ''
print 'Are you ready? Its time for your first areana battle!'
answer = raw_input('Y/N')
if answer == 'y':
    combat.battle(me, you)
print ''
'''


