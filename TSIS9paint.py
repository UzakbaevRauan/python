import pygame 

pygame.init()

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0) 
width = 500
height = 500

screen = pygame.display.set_mode((width, height))

isPressed = False
prevPoint = (0, 0)
curPoint = (0, 0)

def drawRectangle(surface, color, x, y, w, h):
    pygame.draw.rect(surface, color, [x, y, w, h], 5)

def drawCircle(surface, color, x, y):
    pygame.draw.circle(surface, color, (x, y), 30, 3)

def drawLine(surface, color, startPos, endPos):
    pygame.draw.line(surface, color, startPos, endPos, 2)

def erase(surface, x, y):
    pygame.draw.circle(surface, BLACK, (x, y), 40)

# 0 - pencil, 1 - rectangle, 2 - circle, 3 - eraser
currentTool = 0
toolCount = 4

current_color = 0
colors = (BLUE, GREEN, RED)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                currentTool = (currentTool + 1) % toolCount
            elif event.key == pygame.K_c:
                current_color = (current_color + 1) % len(colors)
        if event.type == pygame.MOUSEBUTTONDOWN:
            isPressed = True
            prevPoint = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            isPressed = False
        elif event.type == pygame.MOUSEMOTION and isPressed == True:
            prevPoint = curPoint
            curPoint = pygame.mouse.get_pos()
        elif event.type == pygame.QUIT:
            done = True
            pygame.image.save(screen, 'screenshot.jpg')
            
    if currentTool == 0:
        drawLine(screen, colors[current_color], prevPoint, curPoint)
    elif currentTool == 1:
        drawRectangle(screen, colors[current_color], curPoint[0], curPoint[1], 100, 100)
    elif currentTool == 2:
        drawCircle(screen, colors[current_color], *curPoint)
    elif currentTool == 3:
        erase(screen, *curPoint)

    pygame.display.flip()