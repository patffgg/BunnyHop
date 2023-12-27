import pygame as pg
import random
from settings import *
from sprites import *
from pygame.locals import QUIT


class Game:

  def __init__(self):
    pg.init()
    self.screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption(TITLE)
    self.clock = pg.time.Clock()
    self.running = True
    self.font_name = pg.font.match_font('arial')

  def new(self):
    self.score = 0
    self.all_sprites = pg.sprite.Group()
    self.platforms = pg.sprite.Group()
    self.player = Player(self)
    self.all_sprites.add(self.player)
    for plat in PLATFORM_LIST:
      p = Platform(*plat)
      self.all_sprites.add(p)
      self.platforms.add(p)
    self.run()

  def run(self):
    self.playing = True
    while self.playing:
      self.clock.tick(FPS)
      self.events()
      self.update()
      self.draw()

  def update(self):
    self.all_sprites.update()
    if self.player.vel.y > 0:
      hits = pg.sprite.spritecollide(self.player, self.platforms, False)
      if hits:
        self.player.pos.y = hits[0].rect.top
        self.player.vel.y = 0

    if self.player.rect.top <= HEIGHT / 4:
      self.player.pos.y += abs(self.player.vel.y)
      for plat in self.platforms:
        plat.rect.y += abs(self.player.vel.y)
        if plat.rect.top >= HEIGHT:
          plat.kill()
          self.score += 10

    if self.player.rect.bottom > HEIGHT:
      for sprite in self.all_sprites:
        sprite.rect.y -= max(self.player.vel.y, 10)
        if sprite.rect.bottom < 0:
          sprite.kill()
      if len(self.platforms) == 0:
        self.playing = False

      while len(self.platforms) < 6:
        width = random.randrange(50, 100)
        p = Platform(random.randrange(0, WIDTH - width),
                     random.randrange(-75, -30), width, 20)
        self.platforms.add(p)
        self.all_sprites.add(p)

  def events(self):
    for event in pg.event.get():
      if event.type == pg.QUIT:
        if self.playing:
          self.playing = False
        self.running = False
      if event.type == pg.KEYDOWN:
        if event.key == pg.K_SPACE:
          self.player.jump()

  def draw(self):
    self.screen.fill(BLACK)
    self.all_sprites.draw(self.screen)
    self.draw_text(str(self.score), 22, WHITE, WIDTH / 2, 15)
    pg.display.flip()

  def show_start_screen(self):
    pass

  def show_go_screen(self):
    pass

  def draw_text(surf, text, size, x, y):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


g = Game()
g.show_start_screen()
while g.running:
  g.new
  g.show_go_screen()

pg.quit()
