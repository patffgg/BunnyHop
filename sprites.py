# Sprite classes for platform game
import pygame as pg
#from random import choice, randrange
from settings import *
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (40, HEIGHT - 100)
        self.pos = vec(40, HEIGHT - 100)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
      self.rect.y += 1
      hits = pg.sprite.spritecollide(self, self.game.platforms, False)
      self.rect.y -= 1
      if hits:
        self.vel.y = -PLAYER_JUMP

    
    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
          self.pos.x = 0
        if self.pos.x < 0:
          self.pos.x = WIDTH  

        self.rect.midbottom = self.pos

    



class Platform(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))     
        self.image.set_colorkey(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
       