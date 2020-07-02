import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self,pos,images):
    super().__init__()
    self.images = images
    self.image = images["p1_jump"]
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.xy_speed = pygame.math.Vector2(0,0)
    self.facing = "R"
  
  def update(self):
    #update the image and direction
    if self.facing == "L":
      #flip on x-axis
      self.image = pygame.transform.flip(self.image,True,False)

  def left(self):
    #set facing variable to L(left)
    self.facing == "L"

  def right(self):
    #set facing variable to R(right)
    self.facing == "R"