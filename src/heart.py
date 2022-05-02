import pygame
import random
class heart(pygame.sprite.Sprite):
  def __init__(self, img_file):
    '''Initializes a heart object
    args: self, img_file(str)'''
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(img_file).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = random.randrange(100, 400)
    self.rect.y = random.randrange(100, 400)
    self.image = pygame.transform.scale(self.image, (50, 50))

  def update(self):
      '''Updates the heart object
    args: self'''
      self.rect.x = self.rect.x + random.choice((-1, 1))
      self.rect.y = self.rect.y + random.choice((-1,1))
  