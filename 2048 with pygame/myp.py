import pygame
import Mygame as g
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("2048")
sett=True
green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf', 32)

number='7'
gg=g.games()
def num(number,i,j):
 text = font.render(number, True, green, blue)
 textRect = text.get_rect()
 textRect.center = (30 +60*i + 60 // 2, 30 +60*j + 60 // 2)
 screen.blit(text, textRect)
 pygame.display.update()

def print_g():
 for i in range(4):
  for j in range(4):
   tt=gg.arrs[j][i]
   if tt==0:
    num('0',i,j)
   else:
    num(str(tt),i,j)
def print_status(n):
 if n==0:
  print_g()
 if n==1:
  num('Game Over',2,2)
 if n==2:
  num('You Won',2,2)

gg.new_random()
gg.new_random()

while sett:
  
  print_status(gg.check_over())
  gg.flag=0
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
     screen.fill(pygame.Color("black"))
     if event.key == pygame.K_LEFT:
      gg.move_left()
      
     if event.key == pygame.K_RIGHT:
      gg.move_right()
      
     if event.key == pygame.K_UP:
      gg.move_up()
      
     if event.key == pygame.K_DOWN:
      gg.move_down()
     
     if (gg.flag==1):
      gg.new_random()
     
    if event.type == pygame.QUIT:
      sett=False
  
  #pygame.draw.rect(screen, blue, pygame.Rect(30, 30, 60, 60))  
  #pygame.draw.rect(screen, (125, 125, 255), pygame.Rect(90, 90, 60, 60))  
  
  pygame.display.update()