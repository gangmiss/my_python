# -*- coding:utf-8 -*-
import pygame
import time
from pygame.locals import *
import random

hero_plan_default_x = 200
hero_plan_default_y = 700
screen_window_x = 480
screen_window_y = 852

class Base(object):
    def __init__(self,screen,image,x,y):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(image)

class BasePlane(Base):
    def __init__(self, screen, image, x, y):
        super().__init__(screen,image,x,y)
        self.bullets = []

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def display_2_screen(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            bullet.display_2_scrren()
            bullet.move()
            if bullet.can_delete():
                self.bullets.remove(bullet)


class HeroPlane(BasePlane):
    def __init__(self, screen):
        super().__init__(screen, "./feiji/hero1.png", hero_plan_default_x, hero_plan_default_y)

    def move_up(self):
        self.y -= 10

    def move_down(self):
        self.y += 10

    def fire(self):
        self.bullets.append(Bullet(self.screen, self.x, self.y))


class EnemyPlane(BasePlane):
    def __init__(self, screen):
        super().__init__(screen, "./feiji/enemy0.png", 0, 0)
        self.direction = "right"

    def move_up(self):
        self.y -= 10

    def move_down(self):
        self.y += 1
        if self.direction == "right":
            self.move_right()
        elif self.direction == "left":
            self.move_left()

        if self.x >= screen_window_x - 40:
            self.direction = "left"
        elif self.x <= 0:
            self.direction = "right"

    def display_2_screen(self):
        self.move_down()
        self.fire()
        super().display_2_screen()

    def fire(self):
        random_number = random.randint(1, 60)
        if random_number == 8 or random_number == 20:
            self.bullets.append(EnemyBullet(self.screen, self.x, self.y))


class BaseBullet(Base):
    def __init__(self, screen, image, x, y):
        super().__init__(screen, image, x, y)

    def display_2_scrren(self):
        self.screen.blit(self.image, (self.x, self.y))


class Bullet(BaseBullet):
    def __init__(self, screen, x, y):
        super().__init__(screen, "./feiji/bullet.png", x + 40, y - 20)

    def move_up(self):
        self.y -= 8

    def can_delete(self):
        if self.y <= 0:
            return True
        return False

    def move(self):
        self.move_up()

class EnemyBullet(BaseBullet):
    def __init__(self, screen, x, y):
        super().__init__(screen, "./feiji/bullet1.png", x + 20, y + 30)

    def move_down(self):
        self.y += 8

    def can_delete(self):
        if self.y >= screen_window_y - 12:
            return True
        return False

    def move(self):
        self.move_down()


def key_bord_event(hero):
    for event in pygame.event.get():
        if event.type == QUIT:
            print("退出")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print("left")
                hero.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                print("right")
                hero.move_right()
            elif event.key == K_w or event.key == K_UP:
                print("up")
                hero.move_up()
            elif event.key == K_s or event.key == K_DOWN:
                print("down")
                hero.move_down()
            elif event.key == K_SPACE:
                print("fire")
                hero.fire()


def main():
    screen = pygame.display.set_mode((screen_window_x, screen_window_y), 0, 32)
    background = pygame.image.load("./feiji/background.png")
    hero = HeroPlane(screen)
    enemy = EnemyPlane(screen)
    while True:
        print("11")
        screen.blit(background, (0, 0))
        hero.display_2_screen()
        enemy.display_2_screen()
        pygame.display.update()
        key_bord_event(hero)
        time.sleep(0.01)


if __name__ == "__main__":
    main()
