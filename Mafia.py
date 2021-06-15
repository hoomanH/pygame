import pygame
import time
import random
import os
from pygame import mixer
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
colors = {'Screen':RED, '1':GREEN,'2':GREEN,'3':GREEN,'4':GREEN,'Sq':RED}
naghsh = [ 'دکتر', 'حرفه ای', 'کارآگاه','مافیا' ]
cheackerrooz = {'Screen':WHITE,'1':GREEN,'2':GREEN,'3':GREEN,'4':GREEN,'Sq':WHITE}
roozwrite = {'1':True,'2':True,'3':True,'4':True,}
def ashteb(screen):
    pygame.font.init()
    myfont = pygame.font.Font('freesansbold.ttf', 32)
    screen.fill(WHITE)
    pygame.draw.rect(screen, WHITE, (140, 120, 150, 150))
    pygame.draw.rect(screen, WHITE, (380, 120, 150, 150))
    pygame.draw.rect(screen, WHITE, (140, 360, 150, 150))
    pygame.draw.rect(screen, WHITE, (380, 360, 150, 150))
    pygame.draw.rect(screen, WHITE, (310, 290, 50, 50))
    text = myfont.render('Marjan',True, WHITE)
    screen.blit(text,(160,180))
    text2= myfont.render('Saman',True, WHITE)
    screen.blit(text2,(400,180))
    text3= myfont.render('Hooman',True, WHITE)
    screen.blit(text3,(150,420))
    text4= myfont.render('Farham',True,WHITE)
    screen.blit(text4,(395,420))
    text5= myfont.render('PLEASE SEE YOUR ROLL!',True,RED)
    screen.blit(text5,(395,420))
    pygame.display.flip()
    time.sleep(1)
    Draw(screen,{'Screen':WHITE, '1':GREEN,'2':GREEN,'3':GREEN,'4':GREEN,'Sq':RED})
def random1():
    dic = {} 
    nam = ['1','2','3','4']
    halat = ['M','D','H','K']
    for i in nam:
        naghsh = random.choice(halat)
        dic[i] = naghsh
        halat.remove(naghsh)
    return(dic)
dic = random1()
def Cheacker(dic):
    x=1
    y=0
    for i in dic:
        if dic[i]=='M':
            x=0
        else:
            y = y + 1
    if x==1:
        return('S')
    if y==1:
        return('M')   
def GetPosition(a,b):
    if 360>a>310 and 340>b>290:
        return('shab')
    if 290>a>140 and 270>b>120:
        return('1')
    if 530>a>380 and 270>b>120:
        return('2')
    if 290>a>140 and 510>b>360:
        return('3')
    if 380<a<530 and 510>b>360:
        return('4')
    if 360>a>310 and 400>b>350:
        return('n')
    if 360>a>310 and 280>b>230:
        return('y')
def getPos():
    pygame.event.clear()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x=GetPosition(pos[0],pos[1])
                if x=='1' or x=='2' or x=='3' or x=='4' or x=='shab':
                    return(x)
            if event.type==pygame.QUIT:
                return(0)
def Draw(screen, cl):
    pygame.font.init()
    myfont = pygame.font.Font('freesansbold.ttf', 32)
    screen.fill(cl['Screen'])
    pygame.draw.rect(screen, cl['1'], (140, 120, 150, 150))
    pygame.draw.rect(screen, cl['2'], (380, 120, 150, 150))
    pygame.draw.rect(screen, cl['3'], (140, 360, 150, 150))
    pygame.draw.rect(screen, cl['4'], (380, 360, 150, 150))
    pygame.draw.rect(screen, cl['Sq'], (310, 290, 50, 50))
    text = myfont.render('Marjan',True, (0,0,0))
    screen.blit(text,(160,180))
    text2= myfont.render('Saman',True, (0,0,0))
    screen.blit(text2,(400,180))
    text3= myfont.render('Hooman',True, (0,0,0))
    screen.blit(text3,(150,420))
    text4= myfont.render('Farham',True, (0,0,0))
    screen.blit(text4,(395,420))
    pygame.display.flip()
def mus(audio3,time3=0):
    mixer.init()
    mixer.music.load(audio3)
    mixer.music.play()
    time.sleep(time3)
def asly2(dic):
    running = True
    pygame.init()
    pygame.font.init()
    mixer.init() 
    screen = pygame.display.set_mode([700,700])
    pygame.display.set_caption('Shab hay Mafia')
    Draw(screen,{'Screen':WHITE, '1':GREEN,'2':GREEN,'3':GREEN,'4':GREEN,'Sq':RED})
    for i in range(4):
        printer(dic,screen)
    while running:
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x=GetPosition(pos[0],pos[1])
                if x=='shab':
                    Draw(screen,{'Screen':BLACK, '1':GREEN,'2':GREEN,'3':GREEN,'4':GREEN,'Sq':BLACK}) 
                    mus('1.wav',2)
                    mus('2.wav',3)
                    mus('3.wav')
                    clk=getPos()
                    if (clk==0):
                        pygame.quit()
                    if dic[clk] == 'D' or dic[clk] == 'H' or dic[clk] == 'K':
                        Draw(screen,{'Screen':BLACK, '1':GREEN,'2':GREEN,'3':GREEN,'4':GREEN,'Sq':BLUE})
                        time.sleep(1)
                        Draw(screen,{'Screen':BLACK, '1':GREEN,'2':GREEN,'3':GREEN,'4':GREEN,'Sq':BLACK})
                    if dic[clk] == 'M':
                        Draw(screen,{'Screen':BLACK, '1':GREEN,'2':GREEN,'3':GREEN,'4':GREEN,'Sq':RED})
                        time.sleep(1)
                        Draw(screen,{'Screen':BLACK, '1':GREEN,'2':GREEN,'3':GREEN,'4':GREEN,'Sq':BLACK})
                    mixer.init()
                    mus('6.wav',3)
                    mus('11.wav',2)
                    mus('12.wav')
                    clk=getPos()
                    if (clk==0):
                        pygame.quit()
                    else:
                        ZX=clk
                    mus('T2.wav',2)
                    mus('13.wav',4)
                    mus('7.wav',2)
                    mus('8.wav')
                    clk = getPos()
                    if (clk==0):
                        pygame.quit()
                    if not(clk==ZX):
                        dic.pop(ZX)
                        roozwrite[ZX] = False
                    mus('9.wav',3)


                    mus('14.wav',3)
                    Draw(screen,{'Screen':BLACK, '1':GREEN,'2':GREEN,'3':GREEN,'4':GREEN,'Sq':RED})
                    clk = getPos()
                    if not (clk =='shab'):
                        Draw(screen,{'Screen':BLACK, '1':GREEN,'2':GREEN,'3':GREEN,'4':GREEN,'Sq':BLACK})
                        if dic[clk]=='M':
                            dic.pop(clk)
                            roozwrite[clk] = False
                        else:
                            for i in dic:
                                if dic[i]=='H':
                                    dic.pop(i)
                                    roozwrite[i]=False
                                    break

                        mus('16.wav')

                    else:
                        Draw(screen,{'Screen':BLACK, '1':GREEN,'2':GREEN,'3':GREEN,'4':GREEN,'Sq':BLACK})
                        mus('16.wav')


                    time.sleep(3)
                    Draw(screen,{'Screen':WHITE, '1':GREEN,'2':GREEN,'3':GREEN,'4':GREEN,'Sq':WHITE})
                    for i in roozwrite:
                        if roozwrite[i] == False:
                            cheackerrooz[i] = RED
                    mus('S.wav')
                    Draw(screen,cheackerrooz)
                    winner = Cheacker(dic)
                    if winner == 'M':
                        Draw(screen,{'Screen':RED, '1':GREEN,'2':GREEN,'3':GREEN,'4':GREEN,'Sq':RED})
                        time.sleep(4)
                        pygame.quit()
                    if winner == 'S':
                        Draw(screen,{'Screen':BLUE, '1':GREEN,'2':GREEN,'3':GREEN,'4':GREEN,'Sq':BLUE})
                        time.sleep(4)
                        pygame.quit()
                    else:
                        Draw(screen,cheackerrooz)
                        clk = getPos()
                        if clk == '1' or clk == '2' or clk == '3' or clk == '4':
                            dic.pop(clk)
                            roozwrite[clk] = False
                            Draw(screen,cheackerrooz)
                            time.sleep(2)
                            winner = Cheacker(dic)
                            if winner == 'M':
                                Draw(screen,{'Screen':RED, '1':GREEN,'2':GREEN,'3':GREEN,'4':GREEN,'Sq':RED})
                                time.sleep(4)
                                pygame.quit()
                            if winner == 'S':
                                Draw(screen,{'Screen':BLUE, '1':GREEN,'2':GREEN,'3':GREEN,'4':GREEN,'Sq':BLUE})
                                time.sleep(4)
                                pygame.quit()
                            else:
                                clk = getPos()
                                if clk == '1' or clk == '2' or clk == '3' or clk == '4':
                                    dic.pop(clk)
                                    roozwrite[clk] = False
                                    Draw(screen,cheackerrooz)
                                    time.sleep(2)
                                    winner = Cheacker(dic)
                                    if winner == 'M':
                                        Draw(screen,{'Screen':RED, '1':GREEN,'2':GREEN,'3':GREEN,'4':GREEN,'Sq':RED})
                                        time.sleep(4)
                                        pygame.quit()
                                    if winner == 'S':
                                        Draw(screen,{'Screen':BLUE, '1':GREEN,'2':GREEN,'3':GREEN,'4':GREEN,'Sq':BLUE})
                                        time.sleep(4)
                                        pygame.quit()
def printer(dic,screen):
    clk = getPos()
    ckl = dic[clk]
    if ckl == 'M':
        myphoto = pygame.image.load('M.jpg')
        myphoto = pygame.transform.scale(myphoto, (700,700))
        screen.blit(myphoto, (0,0))
        pygame.display.flip()
    if ckl == 'D':
        myphoto = pygame.image.load('D.jpg')
        myphoto = pygame.transform.scale(myphoto, (700,700))
        screen.blit(myphoto, (0,0))
        pygame.display.flip()
    if ckl == 'K':
        myphoto = pygame.image.load('K.jpg')
        myphoto = pygame.transform.scale(myphoto, (700,700))
        screen.blit(myphoto, (0,0))
        pygame.display.flip()
    if ckl == 'H':
        myphoto = pygame.image.load('H.jpg')
        myphoto = pygame.transform.scale(myphoto, (700,700))
        screen.blit(myphoto, (0,0))
        pygame.display.flip()
    time.sleep(1)
    Draw(screen,{'Screen':WHITE, '1':GREEN,'2':GREEN,'3':GREEN,'4':GREEN,'Sq':RED}) 
asly2(dic)