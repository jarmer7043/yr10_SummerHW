import pygame, sys #importing

pygame.init() #initializing

screen = pygame.display.set_mode([525, 450]) #creating the screen boundaries
#21,18

r = pygame.Color("red") #Making red into a variable
w = pygame.Color("white") #Making white into a variable
b = pygame.Color("black")
o = pygame.Color("orange")
y = pygame.Color("yellow")

frame1 = [ #Making the character
  [w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,b,w,w,w],
  [w,w,w,w,b,b,b,b,w,w,w,w,w,w,w,w,b,r,b,w,w],
  [w,w,w,b,o,o,o,o,b,w,w,w,w,w,w,w,b,r,r,b,w],
  [w,w,b,o,o,o,o,o,o,b,w,w,w,w,w,w,b,r,r,b,w],
  [w,w,b,o,o,o,o,o,o,o,b,w,w,w,w,b,r,r,r,r,b],
  [w,b,o,o,o,w,b,o,o,o,b,w,w,w,w,b,r,r,y,r,b],
  [b,o,o,o,o,b,b,o,o,o,o,b,w,w,w,b,r,y,y,r,b],
  [b,o,o,o,o,b,b,o,o,o,o,b,w,w,w,w,b,y,b,b,w],
  [w,b,o,o,o,o,o,o,o,o,o,o,b,w,w,w,b,o,b,w,w],
  [w,w,b,b,o,o,o,o,o,o,o,o,o,b,w,b,o,o,b,w,w],
  [w,w,w,w,b,b,b,o,o,b,o,o,o,b,b,o,o,b,w,w,w],
  [w,w,w,w,w,b,y,y,b,o,o,o,o,o,b,o,o,b,w,w,w],
  [w,w,w,w,w,b,y,y,y,b,b,o,o,o,b,o,b,w,w,w,w],
  [w,w,w,w,b,w,b,y,y,y,o,o,o,o,b,b,w,w,w,w,w],
  [w,w,w,w,w,b,b,b,y,y,o,o,o,b,b,w,w,w,w,w,w],
  [w,w,w,w,w,w,w,w,b,b,b,o,b,b,w,w,w,w,w,w,w],
  [w,w,w,w,w,w,w,w,w,b,w,o,w,b,w,w,w,w,w,w,w],
  [w,w,w,w,w,w,w,w,w,w,b,b,b,b,w,w,w,w,w,w,w],
  ]

frame2 = [
  [w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,b,r,b],
  [w,w,w,w,b,b,b,b,w,w,w,w,w,w,w,w,b,b,r,r,b],
  [w,w,w,b,o,o,o,o,b,w,w,w,w,w,w,w,b,r,r,r,b],
  [w,w,b,o,o,o,o,o,o,b,w,w,w,w,w,w,b,r,r,r,b],
  [w,w,b,o,o,o,o,o,o,o,b,w,w,w,w,b,r,r,y,r,b],
  [w,b,o,o,o,w,b,o,o,o,b,w,w,w,w,b,r,y,y,r,b],
  [b,o,o,o,o,b,b,o,o,o,o,b,w,w,w,b,r,y,y,r,b],
  [b,o,o,o,o,b,b,o,o,o,o,b,w,w,w,w,b,y,y,b,w],
  [w,b,o,o,o,o,o,o,o,o,o,o,b,w,w,w,b,y,b,w,w],
  [w,w,b,b,o,o,o,o,o,o,o,o,o,b,w,b,o,o,b,w,w],
  [w,w,w,w,b,b,b,o,o,b,o,o,o,b,b,o,o,b,w,w,w],
  [w,w,w,w,w,b,y,y,b,o,o,o,o,o,b,o,o,b,w,w,w],
  [w,w,w,w,w,b,y,y,y,b,b,o,o,o,b,o,b,w,w,w,w],
  [w,w,w,w,b,w,b,y,y,y,o,o,o,o,b,b,w,w,w,w,w],
  [w,w,w,w,w,b,b,b,y,y,o,o,o,b,b,w,w,w,w,w,w],
  [w,w,w,w,w,w,w,w,b,b,b,o,b,b,w,w,w,w,w,w,w],
  [w,w,w,w,w,w,w,w,w,b,w,o,w,b,w,w,w,w,w,w,w],
  [w,w,w,w,w,w,w,w,w,w,b,b,b,b,w,w,w,w,w,w,w],
  ]


def draw_frame(surface, data):
  for y, row in enumerate(data): #I don't really know
    for x, colour in enumerate(row):
      rect = pygame.Rect(x*25, y*25, 25, 25) #Making each square 25 by 25
      screen.fill(colour, rect=rect)

while True:
  draw_frame(screen, frame1)
  pygame.display.update() #Displaying each frame for half a second then swithing
  pygame.time.wait(500)   #to the other
  draw_frame(screen, frame2)
  pygame.display.update()
  pygame.time.wait(500)

