import pygame as pgame
import time
import random

var = pgame.init()
screenW = 550
screenH = 600
gameScreen = pgame.display.set_mode((screenW,screenH))
pgame.display.set_caption('Snakes All Around!!')
clock = pgame.time.Clock()
white = (255,255,255)
red = (180,0,0)
blue = (0,180,180)
Blue = (0,10,255)
green = (0,255,0)
black = (0,0,0)
head = 10
fruitSize = 15
toMove = 10

fps = 20

def buildSnake(snakelead,col):
    for xy in snakelead:
        gameScreen.fill(col,rect = [xy[0],xy[1],head,head])

font = pgame.font.SysFont(None,25)
largeFont = pgame.font.SysFont(None,45)

def showMsg(msg,color,placing = [screenW/2,screenH/2],size = font):
    toBeShown = size.render(msg,True,color)
    msgRect = toBeShown.get_rect()
    msgRect.center = placing[0],placing[1]
    gameScreen.blit(toBeShown,msgRect)
def pause():
    paused = True
    showMsg("Paused",black,size = largeFont)
    showMsg("'C' to continue or 'Q' to quit",black,[screenW/2,screenH/2+25])
    pgame.display.update()
    while paused:
        for event in pgame.event.get():
            if event.type == pgame.QUIT:
                pgame.quit()
                quit()
            elif event.type == pgame.KEYDOWN:
                if event.key == pgame.K_c:
                    paused = False
                    break
                elif event.key == pgame.K_q:
                    main()
           

def checkThis(snakeHead):
    if snakeHead[0] > screenW:
        snakeHead[0] -= screenW
    elif snakeHead[0] < 0:
        snakeHead[0] += screenW

    if snakeHead[1] > screenH:
        snakeHead[1] -= screenH
    elif snakeHead[1] < 0:
        snakeHead[1] += screenH

    return snakeHead

def gameLoop():
    gameExit = False
    gameOver = False
    posRed_x = screenW/2
    posRed_y = screenH/2
    posBlue_x = screenW/2
    posBlue_y = screenH/2+50
    changeRed_x = 0
    changeRed_y = 0
    changeBlue_x = 0
    changeBlue_y = 0
    snakeListRed = []
    snakeLengthRed = 1
    snakeListBlue = []
    snakeLengthBlue = 1
    fruitRedX = round(random.randrange(0,screenW-fruitSize)/10.0)*10.0
    fruitRedY = round(random.randrange(0,screenH-fruitSize)/10.0)*10.0
    fruitBlueX = round(random.randrange(0,screenW-fruitSize)/10.0)*10.0
    fruitBlueY = round(random.randrange(0,screenH-fruitSize)/10.0)*10.0

    countRed = 0
    countBlue = 0
    flagR = True
    flagB = True

    while fruitRedX == fruitBlueX:
        fruitBlueX = round(random.randrange(0,screenW-fruitSize)/10.0)*10.0 
    
    while not gameExit:
        while gameOver == True:
            showMsg("Game Over, you!! Press 'P' to play again or 'Q' to quit",red,[screenW/2,screenH-50])
            pgame.display.update()
            
            for event in pgame.event.get():
                if event.type == pgame.QUIT:
                        gameExit = True
                        gameOver = False
                        break
                if event.type == pgame.KEYDOWN:
                    if event.key == pgame.K_q:
                        main()
                    elif event.key == pgame.K_p:
                        gameLoop()
                    
            
        if gameExit==True:
            continue
        
        for event in pgame.event.get():
            #print(event)
            if event.type == pgame.QUIT:
                gameExit = True
                break
            if event.type == pgame.KEYDOWN:
                if event.key == pgame.K_a:
                    changeRed_x=-toMove
                    changeRed_y = 0
                elif event.key == pgame.K_d:
                    changeRed_x=toMove
                    changeRed_y = 0
                elif event.key == pgame.K_w:
                    changeRed_y= -toMove
                    changeRed_x = 0
                elif event.key == pgame.K_s:
                    changeRed_y=toMove
                    changeRed_x = 0
                elif event.key == pgame.K_p:
                    pause()
                elif event.key == pgame.K_l:
                    changeBlue_x=toMove
                    changeBlue_y = 0
                elif event.key == pgame.K_i:
                    changeBlue_y= -toMove
                    changeBlue_x = 0
                elif event.key == pgame.K_k:
                    changeBlue_y=toMove
                    changeBlue_x = 0
                elif event.key == pgame.K_j:
                    changeBlue_x = -toMove
                    changeBlue_y = 0
            '''
            elif event.type == pgame.KEYUP:
                if event.key == pgame.K_LEFT or event.key == pgame.K_RIGHT or event.key == pgame.K_UP or event.key == pgame.K_DOWN:
                    change_x = 0
                    change_y = 0
            '''

        if not (changeRed_x == 0 and changeRed_y == 0 and changeBlue_x == 0 and changeBlue_y == 0):
            if changeRed_x == 0 and changeRed_y == 0:
                countRed += 1
            if changeBlue_x == 0 and changeBlue_y ==0:
                countBlue += 1
          
        if flagR:
            posRed_x += changeRed_x
            posRed_y += changeRed_y

        if flagB:
            posBlue_x += changeBlue_x
            posBlue_y += changeBlue_y

        if not flagB:
            if posRed_x >= screenW or posRed_x <0 or posRed_y >= screenH or posRed_y <0:
                gameOver = True

        if not flagR:
            if posBlue_x >= screenW or posBlue_x <0 or posBlue_y >= screenH or posBlue_y <0:
                gameOver = True
    
        gameScreen.fill(white)

        if flagR and flagB:
            showMsg("Score : "+str((snakeLengthRed-1 + snakeLengthBlue-1)*10),blue,[50,20])
        else:
            showMsg("Score : "+str((snakeLengthRed-1 + snakeLengthBlue-1)*5),blue,[50,20])
        
        if flagR:
            gameScreen.fill(red, rect = [fruitRedX,fruitRedY,fruitSize,fruitSize])
            gameScreen.fill(red, rect = [posRed_x,posRed_y,head,head])
            
        if flagB:
            gameScreen.fill(Blue, rect = [fruitBlueX,fruitBlueY,fruitSize,fruitSize])
            gameScreen.fill(Blue, rect = [posBlue_x,posBlue_y,head,head])
        pgame.display.update()
        
        snakeHeadRed = []
        if flagR:
            snakeHeadRed.append(posRed_x)
            snakeHeadRed.append(posRed_y)
            if flagB:
                snakeHeadRed = checkThis(snakeHeadRed)
                posRed_x,posRed_y = snakeHeadRed[0],snakeHeadRed[1]
            snakeListRed.append(snakeHeadRed)
        
        snakeHeadBlue = []
        if flagB:
            snakeHeadBlue.append(posBlue_x)
            snakeHeadBlue.append(posBlue_y)
            if flagR:
                snakeHeadBlue = checkThis(snakeHeadBlue)
                posBlue_x,posBlue_y = snakeHeadBlue[0],snakeHeadBlue[1]
            snakeListBlue.append(snakeHeadBlue)

        if flagR:
            if snakeLengthRed < len(snakeListRed):
                del snakeListRed[0]
        if flagB:
            if snakeLengthBlue < len(snakeListBlue):
                del snakeListBlue[0]

        if flagB and flagR:
            if snakeHeadRed == snakeHeadBlue:
                gameOver = True
                showMsg("Crashed to Others !!",red)
                pgame.display.update()
                continue
        
        if flagR:
            for xy in snakeListRed[:-1]:
                if xy == snakeHeadRed:
                    gameOver = True
                    showMsg("You Crashed to Yourself !!",red)
                    pgame.display.update()
                    break
                if flagB:
                    for axy in snakeListBlue[:-1]:
                        if axy == snakeHeadRed:
                            gameOver = True
                            showMsg("Red Crashed to blue !!",red)
                            pgame.display.update()
                            break

        if gameOver:
            continue
        
        if flagB:
            for xy in snakeListBlue[:-1]:
                if xy == snakeHeadBlue:
                    gameOver = True
                    showMsg("You Crashed to Yourself !!",Blue)
                    pgame.display.update()
                    break
                if flagR:
                    for axy in snakeListRed[:-1]:
                        if axy == snakeHeadBlue:
                            gameOver = True
                            showMsg("Blue Crashed to red !!",Blue)
                            pgame.display.update()
                            break
        
        if flagR:
            buildSnake(snakeListRed,red)
        if flagB:
            buildSnake(snakeListBlue,Blue)

        if gameOver:
            continue

        if flagR:
            pgame.draw.circle(gameScreen,white,(int(posRed_x + head/2),int(posRed_y + head/2)),2)
        if flagB:
            pgame.draw.circle(gameScreen,white,(int(posBlue_x + head/2),int(posBlue_y + head/2)),2)

        check = False
        if flagR:
            if posRed_x >= fruitRedX and posRed_x <= fruitRedX+head:
                if posRed_y >= fruitRedY and posRed_y <= fruitRedY+head:
                    check = True
            if fruitRedX >= posRed_x and fruitRedX <= posRed_x + head:
                if fruitRedY >= posRed_y and fruitRedY <= posRed_y + head:
                    check = True

            if check:
                snakeLengthRed += 1
                fruitRedX = round(random.randrange(0,screenW-head)/10.0)*10.0
                fruitRedY = round(random.randrange(0,screenH-head)/10.0)*10.0

        check = False         
        if flagB:
            if posBlue_x >= fruitBlueX and posBlue_x <= fruitBlueX+head:
                if posBlue_y >= fruitBlueY and posBlue_y <= fruitBlueY+head:
                    check = True
            if fruitBlueX >= posBlue_x and fruitBlueX <= posBlue_x + head:
                if fruitBlueY >= posBlue_y and fruitBlueY <= posBlue_y + head:
                    check = True

            if check:
                snakeLengthBlue += 1
                fruitBlueX = round(random.randrange(0,screenW-head)/10.0)*10.0
                fruitBlueY = round(random.randrange(0,screenH-head)/10.0)*10.0

        if flagB and flagR:
            while fruitRedX == fruitBlueX:
                fruitBlueX = round(random.randrange(0,screenW-fruitSize)/10.0)*10.0

        if countRed > fps*5:
            flagR = False
        if countBlue > fps*5:
            flagB = False
            
        pgame.display.update()
        
        clock.tick(fps)
    
    gameScreen.fill(white)
    showMsg("Good Bye",blue)
    pgame.display.update()
    time.sleep(1)
    pgame.quit()
    quit()

def main():
    gameScreen.fill(white)
    showMsg("Snakes All around !!",green,[screenW/2,screenH-575])
    showMsg("Press 'P' to begin gameplay or 'E' to Exit.",green,[screenW/2,screenH-550])
    showMsg("During gameplay press 'P' to pause",green,[screenW/2,screenH-525])

    #Controls
    showMsg("Controls (color indicates the one to be controlled) in order",black)
    showMsg("W",red,[screenW/2-150,screenH/2+50])
    showMsg("A",red,[screenW/2-180,screenH/2+85])
    showMsg("S",red,[screenW/2-150,screenH/2+85])
    showMsg("D",red,[screenW/2-120,screenH/2+85])

    showMsg("Up",black,[screenW/2,screenH/2+50])
    showMsg("Left",black,[screenW/2-50,screenH/2+85])
    showMsg("Down",black,[screenW/2,screenH/2+85])
    showMsg("Right",black,[screenW/2+50,screenH/2+85])

    showMsg("I",Blue,[screenW/2+150,screenH/2+50])
    showMsg("J",Blue,[screenW/2+120,screenH/2+85])
    showMsg("K",Blue,[screenW/2+150,screenH/2+85])
    showMsg("L",Blue,[screenW/2+180,screenH/2+85])

    showMsg("(Note : If only one is played, then another disappears !!)",black,[screenW/2,screenH-125])
    showMsg("by kishanp",red,[screenW/2,screenH-75])
    showMsg("challenge : Control them if you can, alone !! gain double points",black,[screenW/2,screenH-50])
    pgame.display.update()

    while True:
        for event in pgame.event.get():
            if event.type == pgame.QUIT:
                pgame.quit()
                quit()
            if event.type == pgame.KEYDOWN:
                if event.key == pgame.K_p:
                    gameLoop()
                elif event.key == pgame.K_e:
                    gameScreen.fill(white)
                    showMsg("Good Bye",blue)
                    pgame.display.update()
                    pgame.quit()
                    quit()

if __name__=="__main__":main()
