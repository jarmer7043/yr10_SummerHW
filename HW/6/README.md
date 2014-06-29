#Computational Thinking <img src="../../Resources/brain.png" width=50px alt="Tick Sheet">


##Instructions
For this computational thinking challenge you should attempt to find a answer to problem set below. The answer to the problem is only part of your response, ***how*** you found the answer is what matters.

Once you can explain the solution you might try to write a computer program to simulate or model the solution. It might even generalise the problem and provide solutions for ***similar*** problems.

##Grading
|Grade|What must I do?|
|-----|---------------|
|D|I will be able to provide an answer to the problem.|
|C|I will be able to provide an answer to the problem, including an explanation of the algorithm / process.|
|B|I will be able to provide a clear explanation of the algorithm I developed to solve to problem.|
|A/A*|I have been able to demonstrate my understanding of the solution to this problem and represented the algorithm using a computer program.|

##The Problem - Ferrying Soliders
####A detachment of **25** soliders need to cross a deep wide river, with no bridge in sight. They spot two boys playing around in a row boat near the shore. They notice two children playing in a rowboat by the shore.
![Ferrying soldiers](../../Resources/ferrying.png)
####The boat is so tiny, however, that it can only hold the two children *or* one of the soliders. How can the soliders get across the river and leave they children in joint posession of the boat? How many times does the boat need to pass from shore to shore in your solution?

###Rules:
- All 25 soliders must end up on the other side of the river.
- The boat can carry one child by themselves, both children or a single solider.
- At the end both children must be with the boat on either shore.

####How many trips from shore to shore must the boat take?
```
100
```
####Explain you algorithm here:
```
1. Two children go across
2. One child goes back
3. One soldier goes across
4. The child on the other side comes back

Repeat all the steps until all of the soldiers are across.
```

##Extension
Can you represent the algorithm for this problem using a computer program (any language)?
eg you could show each step in the algorithm using text:

```
import pygame, sys

pygame.init()

screen = pygame.display.set_mode([300,100])

w = pygame.Color("white")
b = pygame.Color("blue")
g = pygame.Color("green")
c = pygame.Color("cyan")
p = pygame.Color("pink")
bl = pygame.Color("black")
br = pygame.Color("brown")

step1 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,c,c,c,c,c,c,c,p,p,bl],
    [g,g,g,c,c,c,c,br,br,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step2 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,c,c,c,c,c,p,p,c,c,bl],
    [g,g,g,c,c,c,c,br,br,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step3 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,c,c,c,c,p,p,c,c,c,bl],
    [g,g,g,c,c,c,br,br,c,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step4 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,c,c,c,p,p,c,c,c,c,bl],
    [g,g,g,c,c,br,br,c,c,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step5 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,c,c,p,p,c,c,c,c,c,bl],
    [g,g,g,c,br,br,c,c,c,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step6 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,c,p,p,c,c,c,c,c,c,bl],
    [g,g,g,br,br,c,c,c,c,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step7 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,p,p,c,c,c,c,c,c,c,bl],
    [g,g,g,br,br,c,c,c,c,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step8 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,p,c,p,c,c,c,c,c,c,bl],
    [g,g,g,c,br,br,c,c,c,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step9 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,p,c,c,p,c,c,c,c,c,bl],
    [g,g,g,c,c,br,br,c,c,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step10 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,p,c,c,c,p,c,c,c,c,bl],
    [g,g,g,c,c,c,br,br,c,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step11 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,p,c,c,c,c,p,c,c,c,bl],
    [g,g,g,c,c,c,c,br,br,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step12 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,p,c,c,c,c,c,p,c,c,bl],
    [g,g,g,c,c,c,c,br,br,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step13 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,p,c,c,c,c,c,c,p,c,bl],
    [g,g,g,c,c,c,c,br,br,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step14 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,p,c,c,c,c,c,c,c,p,bl],
    [g,g,g,c,c,c,c,br,br,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step15 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,p,c,c,c,c,c,c,bl,p,c],
    [g,g,g,c,c,c,c,br,br,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step16 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,p,c,c,c,c,c,bl,c,p,c],
    [g,g,g,c,c,c,c,br,br,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step17 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,p,c,c,c,c,bl,c,c,p,c],
    [g,g,g,c,c,c,br,br,c,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step18 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,p,c,c,c,bl,c,c,c,p,c],
    [g,g,g,c,c,br,br,c,c,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step19 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,p,c,c,bl,c,c,c,c,p,c],
    [g,g,g,c,br,br,c,c,c,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step20 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,p,c,bl,c,c,c,c,c,p,c],
    [g,g,g,br,br,c,c,c,c,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step21 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,p,bl,c,c,c,c,c,c,p,c],
    [g,g,g,br,br,c,c,c,c,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step22 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,bl,p,c,c,c,c,c,c,p,c],
    [g,g,g,br,br,c,c,c,c,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step23 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,bl,c,p,c,c,c,c,c,p,c],
    [g,g,g,c,br,br,c,c,c,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step24 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,bl,c,c,p,c,c,c,c,p,c],
    [g,g,g,c,c,br,br,c,c,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step25 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,bl,c,c,c,p,c,c,c,p,c],
    [g,g,g,c,c,c,br,br,c,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step26 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,bl,c,c,c,c,p,c,c,p,c],
    [g,g,g,c,c,c,c,br,br,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step27 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,bl,c,c,c,c,c,p,c,p,c],
    [g,g,g,c,c,c,c,br,br,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]

step28 = [
    [c,c,c,c,c,c,c,c,c,c,c,c],
    [c,c,bl,c,c,c,c,c,c,p,p,c],
    [g,g,g,c,c,c,c,br,br,g,g,g],
    [g,g,g,b,b,b,b,b,b,g,g,g],
    ]


print("The pink squares represent the two children\n")
print("The black square represents one soldier\n")
print("And the two brown squares represent the boat")



def draw_frame(surface, data):
  for y, row in enumerate(data):
    for x, colour in enumerate(row):
      rect = pygame.Rect(x*25, y*25, 25, 25)
      screen.fill(colour, rect=rect)

while True:
    draw_frame(screen, step1)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step2)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step3)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step4)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step5)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step6)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step7)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step8)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step9)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step10)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step11)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step12)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step13)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step14)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step15)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step16)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step17)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step18)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step19)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step20)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step21)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step22)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step23)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step24)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step25)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step26)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step27)
    pygame.display.update()
    pygame.time.wait(1000)
    draw_frame(screen, step28)
    pygame.display.update()
    pygame.time.wait(1000)
```       

For text based programs like pytohn you should create a new file in you repository
![Add new](../../Resources/new.png)

For anything else (eg scratch), email you teacher with the file and say you've done so in the comments.
