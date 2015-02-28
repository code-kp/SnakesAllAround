import pygame as pgame
import time
import random

var = pgame.init()
screenW = 500
screenH = 600
gameScreen = pgame.display.set_mode((screenW,screenH))
pgame.display.set_caption('Snakes All Around!!')
clock = pgame.time.Clock()
white = (255,255,255)
red = (180,0,0)
blue = (0,180,180)
green = (0,255,0)
black = (0,0,0)
head = 10
fruitSize = 15
toMove = 10

font = pgame.font.SysFont(None,25)

def buildSnake(snakelead):
    for xy in snakelead:
        gameScreen.fill(red,rect = [xy[0],xy[1],head,head])

def showMsg(msg,color,placing = [screenW/2,screenH/2]):
    toBeShown = font.render(msg,True,color)
    msgRect = toBeShown.get_rect()
    msgRect.center = placing[0],placing[1]
    gameScreen.blit(toBeShown,msgRect)

def gameLoop():
    gameExit = False
    gameOver = False
    pos_x = screenW/2
    pos_y = screenW/2
    change_x = 0
    change_y = 0
    snakeList = []
    snakeLength = 1
    fruitX = round(random.randrange(0,screenW-fruitSize)/10.0)*10.0
    fruitY = round(random.randrange(0,screenH-fruitSize)/10.0)*10.0
    
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
                        gameExit = True
                        gameOver = False
                        break
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
                if event.key == pgame.K_LEFT:
                    change_x=-toMove
                    change_y = 0
                elif event.key == pgame.K_RIGHT:
                    change_x=toMove
                    change_y = 0
                if event.key == pgame.K_UP:
                    change_y= -toMove
                    change_x = 0
                elif event.key == pgame.K_DOWN:
                    change_y=toMove
                    change_x = 0
                elif event.key == pgame.K_p:
                    change_x = 0
                    change_y = 0
            '''
            elif event.type == pgame.KEYUP:
                if event.key == pgame.K_LEFT or event.key == pgame.K_RIGHT or event.key == pgame.K_UP or event.key == pgame.K_DOWN:
                    change_x = 0
                    change_y = 0
            '''

        if pos_x >= screenW or pos_x <0 or pos_y >= screenH or pos_y <0:
            gameOver = True
        
        pos_x += change_x
        pos_y += change_y

        gameScreen.fill(white)
        showMsg("Score : "+str((snakeLength-1)*5),blue,[50,20])
        gameScreen.fill(green, rect = [fruitX,fruitY,fruitSize,fruitSize])
        gameScreen.fill(red, rect = [pos_x,pos_y,head,head])
        pgame.display.update()

        snakeHead = []
        snakeHead.append(pos_x)
        snakeHead.append(pos_y)
        snakeList.append(snakeHead)

        if snakeLength < len(snakeList):
            del snakeList[0]

        for xy in snakeList[:-1]:
            if xy == snakeHead:
                gameOver = True
                showMsg("You Crashed to Yourself !!",red)
                pgame.display.update()
                break
        
        buildSnake(snakeList)
        
        if pos_x >= fruitX and pos_x <= fruitX+head:
            if pos_y >= fruitY and pos_y <= fruitY+head:
                snakeLength += 1
                fruitX = round(random.randrange(0,screenW-head)/10.0)*10.0
                fruitY = round(random.randrange(0,screenH-head)/10.0)*10.0

        pgame.display.update()
        
        clock.tick(20)
    
    gameScreen.fill(white)
    showMsg("Good Bye",blue)
    pgame.display.update()
    time.sleep(1)
    pgame.quit()
    quit()

def main():
    gameScreen.fill(white)
    showMsg("Snakes All around !!",green)
    showMsg("by kishanp",red,[screenW/2,screenH-200])
    showMsg("Press 'P' to play or 'Q' to quit.",green,[screenW/2,screenH-500])
    pgame.display.update()

    while True:
        for event in pgame.event.get():
            if event.type == pgame.QUIT:
                pgame.quit()
                quit()
            if event.type == pgame.KEYDOWN:
                if event.key == pgame.K_p:
                    pgame.display.toggle_fullscreen()
                    gameLoop()
                elif event.key == pgame.K_q:
                    gameScreen.fill(white)
                    showMsg("Good Bye",blue)
                    pgame.display.update()
                    pgame.quit()
                    quit()

if __name__=="__main__":main()


'''

cx freeze download

'''
