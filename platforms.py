import pygame, random

class Platforms(pygame.sprite.Sprite):
  def __init__(self,pos,img_path,width = 70,height = 70):
    super().__init__()
    #create new image
    self.image = pygame.Surface([width,height]).convert()
    #add platform to image
    self.image.blit(pygame.image.load(img_path).convert(), (0,0),(0,0,width,height))
    #set background to transparent
    self.image.set_colorkey((0,0,0))
    #create rectangle of image
    self.rect = self.image.get_rect()
    #move image to position
    self.rect.center = pos

  #function to make look like scrolling
  def scroll(self, change):
    #moving top of rectangle
    self.rect.top += change