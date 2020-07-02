#main file
import sys, pygame
from pygame.locals import*

pygame.init()
screen_info = pygame.display.Info()

#set the width and height to the size of the screen
size = (width,height) = (int(screen_info.current_w),int(screen_info.current_h))
screen = pygame.display.set_mode(size)

#create clock object
clock = pygame.time.Clock()
#create color RGB
color = (255,224,179)
#fill screen with color
screen.fill(color)
#create Sprite groups
sprite_list = pygame.sprite.Group()
platforms = pygame.sprite.Group()

#create main function
def main():
  game_over = False
  while True:
    #set maximum refresh rate
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      #check if any key is pressed
      if event.type == KEYDOWN:
        #check if it is f key
        if event.key == K_f:
          #make screen full screen
          pygame.display.set_mode(size, FULLSCREEN)
        #check if escape key pressed
        if event.key == K_ESCAPE:
          #reset to original size
          pygame.display.set_mode(size)
  #set screen color
  screen.fill(color)
  #add images to screen
  platforms.draw(screen)
  sprite_list.draw(screen)
  pygame.display.flip()

if __name__ == "__main__":
  main()

