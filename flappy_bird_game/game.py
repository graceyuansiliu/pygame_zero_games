import random
import pgzrun
# import pygame
# from pgzero import keyboard

from pgzhelper import *

WIDTH = 690
HEIGHT = 477
TITLE = "Flappy Bird :)"

ground = Actor("ground.png")
ground.x = 370
ground.y = 462

bird = Actor("flappy_bird_up.png")
bird.x = 75
bird.y = 100
bird.scale = 0.15
bird.images = ["flappy_bird_middle.png", "flappy_bird_down.png", "flappy_bird_middle.png", "flappy_bird_up.png"]
bird.fps = 7

gameover = Actor("text_game_over.png")
gameover.x = 345
gameover.y = 231

top_tree = Actor("upside_down_tree.png")
bottom_tree = Actor("tree.png")
top_tree.x = WIDTH
top_tree.y = 0
gap = 140
bottom_tree.x = WIDTH
bottom_tree.y = top_tree.height + gap


gravity = 0.1
bird.speed = 0.1
bird.alive = True
scroll_speed = -5
score = 0


def on_mouse_down():
    global score

    if bird.alive:
        bird.speed = -2.5
    else:
        bird.alive = True
        score = 0


def update():
    global score

    bird.scale = 0.15
    bird.animate()
    bird.y += bird.speed
    bird.speed += gravity

    if bird.y > HEIGHT - 35 or bird.y < 0:
        bird.alive = False

    top_tree.x += scroll_speed
    bottom_tree.x += scroll_speed

    if top_tree.x < -50:
        offset = random.uniform(-100, 200)
        top_tree.midleft = (690, offset)
        bottom_tree.midleft = (690, offset + top_tree.height + gap)
        score += 1

    if bird.colliderect(top_tree) or bird.colliderect(bottom_tree):
        bird.alive = False


def draw():
    screen.blit("background.png", (0, 0))

    if bird.alive:
        top_tree.draw()
        bottom_tree.draw()
        bird.draw()
        ground.draw()
    else:
        screen.draw.text("Click your mouse to play again :)", color=(200, 62, 62), center=(345, 300), shadow=(0.5, 0.5), scolor=(228, 91, 91), fontsize=35)
        ground.draw()
        gameover.draw()
        bird.x = 75
        bird.y = 100
        gravity = 0
        bird.speed = 0
        top_tree.x = 690
        bottom_tree.x = 690

    screen.draw.text("Score: " + str(score), color="black", midtop=(60, 15), shadow=(0.5, 0.5), scolor="white", fontsize=40)


pgzrun.go()
