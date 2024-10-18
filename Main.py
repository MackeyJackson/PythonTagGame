import pygame, time, datetime, sys
pygame.init()
dt = 0
fontsize = 100
font = pygame.font.SysFont('Arial', fontsize)
text_surface = font.render('Game End', False, (0, 0, 0))
vel1=1
vel2=1
modifier = 10
clock = pygame.time.Clock()
#background setup
computerRes = pygame.display.Info()
screen = pygame.display.set_mode((computerRes.current_w,computerRes.current_h - computerRes.current_h / 17.28))
pygame.display.set_caption('Tag Game')
backgroundColor = (255, 255, 255)
screen.fill(backgroundColor)
pygame.display.flip()
#primary colours
Blue=(0,0,255)
Green=(0,255,0)
Red=(255,0,0)
endGame = False
#player 1 pos
x1 = computerRes.current_w / 2.5 - 200
y1 = computerRes.current_h / 2
#player 2 pos
x2 = computerRes.current_w / 1.5 + 100
y2 = computerRes.current_h / 2
#running loop
pygame.key.set_repeat(50,50)
#varible defining
running = True
bkeya = False
bkeyd = False
bkeyw = False
bkeys = False
bkeya2 = False
bkeyd2 = False
bkeyw2 = False
bkeys2 = False
power1 = False
power2 = False
duration1 = 3
duration2 = 3
power1cooldown = 0
power2cooldown = 0
flashCounter = 0
#----timers----
def settimers():
    CooldownTimer = pygame.event.custom_type()
    pygame.time.set_timer(CooldownTimer, 1000)
    DurationTimer = pygame.event.custom_type()
    pygame.time.set_timer(DurationTimer, 1000)
    return CooldownTimer, DurationTimer
CooldownTimer, DurationTimer = settimers()
CooldownTimer2, DurationTimer2 = settimers()
#end of game
endGameTimer = pygame.event.custom_type()
pygame.time.set_timer(endGameTimer, 1000)
#        -----function definitons-----
def timerhandeling(cooldowntimer,cooldown, duration, durationtimer):
    if event.type == cooldowntimer and cooldown > 0:
        cooldown -= 1
        print(cooldown)
    if event.type == durationtimer and duration > 0:
        duration -= 1
        print(f'duration {duration}')
    return cooldowntimer,cooldown, duration, durationtimer
def powerup(powerNum, durationNum,velNum, cooldownNum):
    if powerNum == True:
        velNum = 2.5
        durationNum = 3
        cooldownNum = 15
    if durationNum == 0:
        velNum = 1
    return velNum,durationNum,cooldownNum,powerNum
def Handeling(bkeyup,bkeydown,bkeyleft,bkeyright,PlayerCoordinatex,PlayerCoordinatey,playerVel):
    if bkeyleft == True and PlayerCoordinatex >0:
        PlayerCoordinatex-=playerVel
        if bkeyleft == True and bkeyup == True and PlayerCoordinatey>computerRes.current_h / 17.28 - 50:
            PlayerCoordinatey-=playerVel
        if bkeydown == True and bkeyleft == True and PlayerCoordinatex>0 and PlayerCoordinatey < computerRes.current_h - computerRes.current_h / 17.28 - 45 -modifier and bkeyup != True:
            PlayerCoordinatey+=playerVel
    elif bkeyright == True and PlayerCoordinatex<computerRes.current_w -20:
        PlayerCoordinatex+=playerVel
        if bkeya == True and PlayerCoordinatex<computerRes.current_w -20:
            PlayerCoordinatex-=playerVel
        if bkeyright == True and bkeyup == True and PlayerCoordinatey>computerRes.current_h / 17.28 - 50:
            PlayerCoordinatey-=playerVel
        if bkeydown == True and bkeyright == True and PlayerCoordinatex>0 and PlayerCoordinatey < computerRes.current_h - computerRes.current_h / 17.28 - 45 - modifier and bkeyup != True:
            PlayerCoordinatey+=playerVel
    elif bkeyup == True and PlayerCoordinatey>computerRes.current_h / 17.28 - 50:
        PlayerCoordinatey-=playerVel
    elif bkeydown == True and PlayerCoordinatey < computerRes.current_h - computerRes.current_h / 17.28 - 45 - modifier:
        PlayerCoordinatey += playerVel
        if bkeyup == True and PlayerCoordinatey>computerRes.current_h / 17.28 - 50:
            PlayerCoordinatey-=playerVel
    return PlayerCoordinatex,PlayerCoordinatey
pygame.mouse.set_visible(False)
#----running loop----
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        CooldownTimer,power1cooldown, duration1, DurationTimer = timerhandeling(CooldownTimer,power1cooldown, duration1, DurationTimer)
        CooldownTimer2,power2cooldown, duration2, DurationTimer2 = timerhandeling(CooldownTimer2,power2cooldown, duration2, DurationTimer2)
    #         -----key inputs-----
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_a:
                    bkeya = True
                case pygame.K_d:
                    bkeyd = True
                case pygame.K_w:
                    bkeyw = True
                case pygame.K_s:
                    bkeys = True
                case pygame.K_LEFT:
                    bkeya2 = True
                case pygame.K_RIGHT:
                    bkeyd2 = True
                case pygame.K_UP:
                    bkeyw2 = True
                case pygame.K_DOWN:
                    bkeys2 = True
        if event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_a:
                    bkeya = False
                case pygame.K_d:
                    bkeyd = False
                case pygame.K_w:
                    bkeyw = False
                case pygame.K_s:
                    bkeys = False
                case pygame.K_LEFT:
                    bkeya2 = False
                case pygame.K_RIGHT:
                    bkeyd2 = False
                case pygame.K_UP:
                    bkeyw2 = False
                case pygame.K_DOWN:
                    bkeys2 = False
#             ----power up inputs----
#                 player1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT and power1cooldown == 0:
                power1 = True
                print("true")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                power1 = False
#                 player 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RSHIFT and power2cooldown == 0:
                power2 = True
                print("true2")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RSHIFT:
                power2 = False
    #basic movement keys handeling
    x1, y1 = Handeling(bkeyw,bkeys,bkeya,bkeyd,x1,y1,vel1)
    x2, y2 = Handeling(bkeyw2,bkeys2,bkeya2,bkeyd2,x2,y2,vel2)
    #powerup handeling
    vel1,duration1,power1cooldown,power1 = powerup(power1,duration1,vel1,power1cooldown)
    vel2,duration2,power2cooldown,power2 = powerup(power2,duration2,vel2,power2cooldown)  
#----collison----
#screen update and drawing
    screen.fill((255,255,255))  #done before draeing so there are no artifacts
    Player1 = pygame.draw.rect(screen,(Blue),(x1,y1, 20 + modifier,20 + modifier))
    Player2 = pygame.draw.rect(screen,(Red),(x2,y2, 20 + modifier,20 + modifier))
    chaser = Player2
    runner = Player1
    if runner.colliderect(chaser):
        endGame = True
    if endGame == True:
        vel1 = 0
        power1= False
        Player1 = pygame.draw.rect(screen,(100,100,100),(x1,y1, 20 + modifier,20 + modifier))
        screen.blit(text_surface, (computerRes.current_w / 2 -175,computerRes.current_h /2 -100))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                Player1 = pygame.draw.rect(screen,(Blue),(x1,y1, 20 + modifier,20 + modifier))
                endGame = False
    pygame.display.update()   
#delta time and fps lock
clock = pygame.time.Clock()
dt = clock.tick(60)/1000