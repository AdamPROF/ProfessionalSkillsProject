import pygame
import random

pygame.init()

screen_width = 1600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Four Room Mini-Game")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (60, 60, 60)

font = pygame.font.SysFont(None, 80)

room1 = pygame.Rect(50, 50, 200, 150)
room2 = pygame.Rect(1350, 50, 200, 150)
room3 = pygame.Rect(50, 600, 200, 150)
room4 = pygame.Rect(1350, 600, 200, 150)

player = pygame.Rect(screen_width/2-25, screen_height/2-25, 50, 50)
player_color = white

background = pygame.image.load('wood2.png')
background = pygame.transform.scale(background, (screen_width, screen_height))

player_speed = 1
player_movement = [0, 0]

minigame = None

def start_minigame1(screen):
    global player_movement
    player_movement = [0, 0]
    player.x = 800
    player.y = 400
    button_font = pygame.font.SysFont(None, 50)
    button_text = button_font.render('Back to Main Screen', True, white)
    button_rect = button_text.get_rect(center=(screen_width/2, screen_height-50))


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                running = False

        screen.fill(white)
        screen.blit(background, (0, 0))

        
        pygame.draw.rect(screen, gray, button_rect.inflate(10, 10))
        pygame.draw.rect(screen, black, button_rect)
        screen.blit(button_text, button_rect)

        font = pygame.font.SysFont(None, 50)
        textSurface = font.render('Programming is like giving instructions to a robot or video game character', True, black)
        textRect = textSurface.get_rect(center=(screen_width/2, screen_height/2-25))
        screen.blit(textSurface, textRect)
        textSurface1 = font.render('You can create anything from a simple calculator to a complex video game or app.', True, black)
        textRect1 = textSurface1.get_rect(center=(screen_width/2, screen_height/2+25))
        screen.blit(textSurface1, textRect1)
        textSurface1 = font.render('It is like having a superpower to make your ideas come to life!', True, black)
        textRect1 = textSurface1.get_rect(center=(screen_width/2, screen_height/2+65))
        screen.blit(textSurface1, textRect1)

        


        pygame.display.update()

def start_minigame2(screen):
    global player_movement
    player_movement = [0, 0]
    player.x = 800
    player.y = 400
    button_font = pygame.font.SysFont(None, 50)
    button_text = button_font.render('Back to Main Screen', True, white)
    button_rect = button_text.get_rect(center=(screen_width/2, screen_height-50))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                running = False

        screen.fill(white)
        screen.blit(background, (0, 0))

        
        pygame.draw.rect(screen, gray, button_rect.inflate(10, 10))
        pygame.draw.rect(screen, black, button_rect)
        screen.blit(button_text, button_rect)

        font = pygame.font.SysFont(None, 50)
        textSurface = font.render('You have different coding languages for different purposes.', True, black)
        textRect = textSurface.get_rect(center=(screen_width/2, screen_height/2-65))
        screen.blit(textSurface, textRect)
        textSurface1 = font.render('Popular ones are Python, Java, CSS & HTML.', True, black)
        textRect1 = textSurface1.get_rect(center=(screen_width/2, screen_height/2-25))
        screen.blit(textSurface1, textRect1)
        textSurface1 = font.render('Simple games like The Sims is made with Python.', True, black)
        textRect1 = textSurface1.get_rect(center=(screen_width/2, screen_height/2+25))
        screen.blit(textSurface1, textRect1)
        textSurface1 = font.render('A bit larger games like minecraft is made with Java.', True, black)
        textRect1 = textSurface1.get_rect(center=(screen_width/2, screen_height/2+65))
        screen.blit(textSurface1, textRect1)
        textSurface1 = font.render('HTML & CSS are used for websites likes this one for example.', True, black)
        textRect1 = textSurface1.get_rect(center=(screen_width/2, screen_height/2+105))
        screen.blit(textSurface1, textRect1)


        pygame.display.update()

def start_minigame3(screen):
    #Setting up the basic stuffs i will need to use
    global player_movement
    player_movement = [0, 0]
    player.x = 800
    player.y = 400
    button_font = pygame.font.SysFont(None, 50)
    button_text = button_font.render('Back to Main Screen', True, white)
    button_rect = button_text.get_rect(center=(screen_width/2, screen_height-50))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                running = False

        screen.fill(white)
        screen.blit(background, (0, 0))

        
        pygame.draw.rect(screen, gray, button_rect.inflate(10, 10))
        pygame.draw.rect(screen, black, button_rect)
        screen.blit(button_text, button_rect)

        font = pygame.font.SysFont(None, 50)
        textSurface = font.render('Programming requires you to be creative.', True, black)
        textRect = textSurface.get_rect(center=(screen_width/2, screen_height/2-65))
        screen.blit(textSurface, textRect)
        textSurface1 = font.render('Someone who thinks outside of the box.', True, black)
        textRect1 = textSurface1.get_rect(center=(screen_width/2, screen_height/2-25))
        screen.blit(textSurface1, textRect1)
        textSurface1 = font.render('Someone who loves creating stuff', True, black)
        textRect1 = textSurface1.get_rect(center=(screen_width/2, screen_height/2+25))
        screen.blit(textSurface1, textRect1)
        textSurface1 = font.render('Programming is a hard genre to get into,', True, black)
        textRect1 = textSurface1.get_rect(center=(screen_width/2, screen_height/2+65))
        screen.blit(textSurface1, textRect1)
        textSurface1 = font.render('but the hardwork is getting compensated gratefully.', True, black)
        textRect1 = textSurface1.get_rect(center=(screen_width/2, screen_height/2+105))
        screen.blit(textSurface1, textRect1)


        pygame.display.update()

def start_minigame4(screen):
    global player_movement
    player_movement = [0, 0]
    player.x = 800
    player.y = 400
    questions = ['What language is used for easy games', 'What language is used for websites', 'What language is for stronger apps']
    answers = ['Python', 'HTML & CSS', 'Java']
    answersC = ['Python', 'HTML & CSS', 'Java']

    button_font = pygame.font.SysFont(None, 50)
    button_text = button_font.render('Back to Main Screen', True, white)
    button_rect = button_text.get_rect(center=(screen_width/2, screen_height-50))

    qFont = pygame.font.SysFont(None, 50)
    aFont = pygame.font.SysFont(None, 30)

    questionX = 100
    questionY = 50
    answerX = 400
    answerY = 40

    draggableO = []
    for answer in answers:
        textS = aFont.render(answer, True, black)
        rect = textS.get_rect()
        rect.x = answerX
        rect.y = answerY
        draggableO.append((textS, rect, False))
        answerY += 50
    
    droppedO = [None] * len(questions)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousePosition = pygame.mouse.get_pos()
                for i, (textS, rect, is_dragging) in enumerate(draggableO):
                    if rect.collidepoint(mousePosition):
                        draggableO[i] = (textS, rect, True)
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mousePosition = pygame.mouse.get_pos()
                for i, (textS, rect, is_dragging) in enumerate(draggableO):
                    if is_dragging:
                        for j, question in enumerate(questions):
                            questionS = qFont.render(question, True, black)
                            questionR = questionS.get_rect()
                            questionR.x = questionX
                            questionR.y = questionY + j * 50
                            if questionR.collidepoint(mousePosition):
                                droppedO[j] = textS
                                if droppedO[j] == answersC[j]:
                                    screen.blit(qFont.render("Correct answer", True, green), (questionR.right + 20, questionR.centery))
                                else:
                                    screen.blit(qFont.render("Wrong answer", True, red), (questionR.right + 20, questionR.centery))
                        draggableO[i] = (textS, rect, False)
        
        screen.fill(white)
        screen.blit(background, (0, 0))

        for i, question in enumerate(questions):
            questionS = qFont.render(question, True, black)
            questionR = questionS.get_rect()
            questionR.x = questionX
            questionR.y = questionY + i * 50
            pygame.draw.rect(screen, black, questionR, 1)
            screen.blit(questionS, questionR)

            if droppedO[i] is not None:
                answerR = droppedO[i].get_rect()
                answerR.x = questionR.right + 20
                answerR.centery = questionR.centery
                pygame.draw.rect(screen, red, answerR, 1)
                screen.blit(droppedO[i], answerR)
        
        for textSurface, rect, is_dragging in draggableO:
            if is_dragging:
                rect.center = pygame.mouse.get_pos()
            pygame.draw.rect(screen, black, rect, 1)
            screen.blit(textSurface, rect)

        pygame.draw.rect(screen, gray, button_rect.inflate(10, 10))
        pygame.draw.rect(screen, black, button_rect)
        screen.blit(button_text, button_rect)
        
        pygame.display.update()

    


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_movement[1] -= player_speed
            elif event.key == pygame.K_DOWN:
                player_movement[1] += player_speed
            elif event.key == pygame.K_LEFT:
                player_movement[0] -= player_speed
            elif event.key == pygame.K_RIGHT:
                player_movement[0] += player_speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_movement[1] += player_speed
            elif event.key == pygame.K_DOWN:
                player_movement[1] -= player_speed
            elif event.key == pygame.K_LEFT:
                player_movement[0] += player_speed
            elif event.key == pygame.K_RIGHT:
                player_movement[0] -= player_speed
    
    
    player.x += player_movement[0]
    player.y += player_movement[1]

    if player.left < 0:
        player.left = 0
    elif player.right > screen_width:
        player.right = screen_width
    if player.top < 0:
        player.top = 0
    elif player.bottom > screen_height:
        player.bottom = screen_height
    
    if player.colliderect(room1):
        game_active = True
        minigame = "game1"
        start_minigame1(screen)

    elif player.colliderect(room2):
        game_active = True
        minigame = "game2"
        start_minigame2(screen)
    elif player.colliderect(room3):
        game_active = True
        minigame = "game3"
        start_minigame3(screen)
    elif player.colliderect(room4):
        game_active = True
        minigame = "game4"
        start_minigame4(screen)
    
    screen.fill(white)
    screen.blit(background, (0, 0))
    
    pygame.draw.rect(screen, gray, room1.inflate(10, 10))
    pygame.draw.rect(screen, black, room1)
    
    pygame.draw.rect(screen, gray, room2.inflate(10, 10))
    pygame.draw.rect(screen, black, room2)
    
    pygame.draw.rect(screen, gray, room3.inflate(10, 10))
    pygame.draw.rect(screen, black, room3)
    
    pygame.draw.rect(screen, gray, room4.inflate(10, 10))
    pygame.draw.rect(screen, black, room4)
    
    pygame.draw.rect(screen, player_color, player)

    textSurface = font.render('The Detective Game', True, black)
    textRect = textSurface.get_rect(center=(screen_width/2, screen_height/2))
    screen.blit(textSurface, textRect)
    
    pygame.display.update()

pygame.quit()
