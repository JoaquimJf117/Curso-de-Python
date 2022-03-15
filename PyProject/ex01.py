import pygame
from time import sleep
pygame.init()
pygame.mixer.music.load('slowdown.mp3')
pygame.mixer.music.play()
sleep(120)
pygame.event.wait()
