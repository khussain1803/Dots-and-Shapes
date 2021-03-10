import pygame
import random
import time
import sys
class textbox():

    def __init__(self, x,y, w, h, text=""):
        font = pygame.font.SysFont("fssas",30)
        #gives object  a pygame rectangle attribute
        #sets rectangle size and coordinates
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (0,0,0)
        self.textcolor = (0,0,0)
        #sets text and active status
        self.text = text
        self.rendertext = font.render(text, True, self.textcolor)
        #while active is false, typing inputs will not effect the text
        #displayed in the textbox, it must be clicked for active status
        #and clicked off to set it back to false
        self.active = False
        #When attribute == TRUE textbox can no longer be accessed by user
        self.end = False
    def update(self, event, score, mode, timed):
        font = pygame.font.SysFont("fssas",30)
        #checks if user has clicked on textbox
        #changes self.active attribute depending on where user clicks
        #changes textbox colour to indicate true and false active status
        #(whether the user can type in it or not)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = (255,0,0) if self.active else (0,0,0)
        #checks if user has typed an input on the keyboard
        if event.type == pygame.KEYDOWN:
            #if user has selected/clicked the textbox to type in it
            #program changes the text displayed depending on what they
            #have typed
            if self.active:
                #if user inputs enter key it will save the text in a file
                if event.key == pygame.K_RETURN:
                    #makes sure to write score and name to correct file depending on the mode
                    if mode == 'AI':
                        if timed == True:
                            scorefile = open("scorefilesquares.txt","a")
                        else:
                            scorefile = open("scorefileaitime.txt","a")
                    elif mode == 'square':
                        if timed == True:
                            scorefile = open("scorefilenoait.txt","a")
                        else:
                            scorefile = open("scorefilenoai.txt","a")
                    elif mode == 'triangle':
                        if timed == True:
                            scorefile = open("scorefiletriangletimed.txt","a")
                        else:
                            scorefile = open("scorefiletriangle.txt","a")
                    elif mode == 'hexagon':
                        if timed == True:
                            scorefile = open("scorefilehexagontimed.txt","a")
                        else:
                            scorefile = open("scorefilehexagon.txt","a")
                    elif mode == 'mixed':
                        if timed == True:
                            scorefile = open("scorefilemixedt.txt","a")
                        else:
                            scorefile = open("scorefilemixed.txt","a")
                        
                    scorefile.write(str(self.text) + "\n")
                    scorefile.write(str(score) + "\n")
                    scorefile.close()
                    self.text = ''
                    self.end = True
                #removes one character from text when backspace is pressed
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

                self.rendertext = font.render(self.text, True, self.textcolor)
    def update1(self):
        # Resize the box if the text is too long.
        width = max(200, self.rendertext.get_width()+10)
        self.rect.w = width
    #draws textbox object onto window and puts text on top of it
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect, 2)
        win.blit(self.rendertext, (self.rect.x + 5, self.rect.y + 5))
class pointdot():
    def __init__(self,color,x,y):
        self.color = color
        self.x = x
        self.y = y
    def draw(self,window):
        pygame.draw.circle(window,self.color,(self.x,self.y),12)
    def surroundedsquare(self,win,turn):
        a = pygame.Surface.get_at(win,(self.x + 38,self.y))
        b = pygame.Surface.get_at(win,(self.x - 38,self.y))
        c = pygame.Surface.get_at(win,(self.x,self.y + 38))
        d = pygame.Surface.get_at(win,(self.x,self.y - 38))
        if a == (0,0,0,255) and b == (0,0,0,255) and c == (0,0,0,255) and d == (0,0,0,255):
        #THIS MEANS THAT PLAYER1 HAS BLUE DOTS AND PLAYER 2 HAS RED EVEN THOUGH IT STATES IT SHOULD BE
        #THE OTHER WAY ROUND
        #THIS HAPPENS SINCE GET_AT FUNCION GIVES ACTUAL COLOUR ON SCREEN SND NOT CLASS STATUS COLOR SO ONLY UPDATES BY THE
        #NEXT LOOP BUT BY THEN THE TURN NUMBER HAS ALREADY CHANGED MEANING THEY MUST BE SWAPPED
        #IN 4 PLAYER CASE THE COLOURS ROTATE BY ONE PLACE BUT STILL REMAIN CONSTANT
        #THIS APPLIES FOR ALL 3 KEY EVENTS OF MOUSEBUTTONDOWN, MOUSEMOTION AND NOEVENT
            if self.color == (0,255,255):
                if turn == 1:
                    self.color = (255,0,0)
                else:
                    self.color = (0,0,255)
        else:
            self.color = (0,255,255)
    def surroundedtriangle(self,win,turn):
        a = pygame.Surface.get_at(win,(self.x,self.y + 33))
        b = pygame.Surface.get_at(win,(self.x,self.y - 32))
        if a == (255,0,0,255) or a == (0,255,0,255) or a == (255,255,0,255):
            c = pygame.Surface.get_at(win,(self.x - 19,self.y))
            d = pygame.Surface.get_at(win,(self.x + 19,self.y))
            e = pygame.Surface.get_at(win,(self.x, self.y - 32))
            if c == (0,0,0,255) and d == (0,0,0,255) and e == (0,0,0,255):
                if self.color == (0,255,255):
                    if turn == 1:
                        self.color = (255,0,0)
                    else:
                        self.color = (0,0,255)
            else:
                self.color = (0,255,255)
        elif b == (255,0,0,255) or b == (0,255,0,255) or b == (255,255,0,255):
            c = pygame.Surface.get_at(win,(self.x - 19,self.y))
            d = pygame.Surface.get_at(win,(self.x + 19,self.y))
            e = pygame.Surface.get_at(win,(self.x, self.y + 33))
            if c == (0,0,0,255) and d == (0,0,0,255) and e == (0,0,0,255):
                if self.color == (0,255,255):
                    if turn == 1:
                        self.color = (255,0,0)
                    else:
                        self.color = (0,0,255)
            else:
                self.color = (0,255,255)
    def surroundedhexagon(self,win,turn):
        a = pygame.Surface.get_at(win,(self.x + 43, self.y))
        b = pygame.Surface.get_at(win,(self.x - 43, self.y))
        c = pygame.Surface.get_at(win,(self.x +22, self.y + 38))
        d = pygame.Surface.get_at(win,(self.x +22, self.y - 38))
        e = pygame.Surface.get_at(win,(self.x - 22, self.y + 38))
        f = pygame.Surface.get_at(win,(self.x - 22, self.y - 38))
        if a == (0,0,0,255) and b == (0,0,0,255) and c == (0,0,0,255) and d == (0,0,0,255) and e == (0,0,0,255) and f == (0,0,0,255):
            if self.color == (0,255,255):
                    if turn == 1:
                        self.color = (255,0,0)
                    else:
                        self.color = (0,0,255)
        else:
            self.color = (0,255,255)
    def partlysurroundedsquare(self,win):
        #Returns how many remaining lines a square has left unfilled, and also returns the coordinates of centre points of these
        #lines and whether they are horizontal or vertical to aid in locating them in the all_lines list.
        emptylines = []
        a = pygame.Surface.get_at(win,(self.x + 38,self.y))
        b = pygame.Surface.get_at(win,(self.x - 38,self.y))
        c = pygame.Surface.get_at(win,(self.x,self.y + 38))
        d = pygame.Surface.get_at(win,(self.x,self.y - 38))
        if a != (0,0,0,255):
            emptylines.append(((self.x + 38,self.y),"vertical"))
        if b != (0,0,0,255):
            emptylines.append(((self.x - 38,self.y),"vertical"))
        if c != (0,0,0,255):
            emptylines.append(((self.x,self.y + 38),"horizontal"))
        if d != (0,0,0,255):
            emptylines.append(((self.x,self.y - 38),"horizontal"))
        if len(emptylines) == 1:
            return(1,emptylines[0])
        elif len(emptylines) == 2:
            return(2,emptylines)
        else:
            return ([0])
class line():
    def __init__(self, color,x1,y1,x2,y2,width):
        self.color = color
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.width = width
    def draw(self, win):
        pygame.draw.line(win,self.color,(self.x1,self.y1),(self.x2,self.y2),self.width)
    
class dot():
    def __init__(self, color, x,y,clicked):
        self.color = color
        self.x = x
        self.y = y
        self.clicked = clicked
    def draw(self, win):
        pygame.draw.circle(win,self.color,(self.x,self.y),8)
    def mouseon(self,position,win):
        mousecolor = pygame.Surface.get_at(win,(position[0],position[1])) 
        if position[0] > (self.x - 8) and position[0] < (self.x + 8):
            if position[1] > (self.y - 8) and position[1] < (self.y + 8):
                if mousecolor != (0,255,255,255):
                    return True
        return False
    def isclicked(self):
        if self.clicked == False:
            self.clicked = True
            self.color = (0,255,0)
        else:
            self.clicked = False
            self.color = (255,0,0)
    
    def reset(self):
        self.color = (255,0,0)
        self.clicked = False
class button():
    def __init__(self, fontsize, textcolor, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.textcolor = textcolor
        self.fontsize = fontsize
    def draw(self,win,outline=None):
        if outline:
            pygame.draw.rect(win, outline,(self.x-2,self.y-2,self.width+4,self.height+4),0)
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height),0)
        if self.text != '':
            font = pygame.font.SysFont('sitkasmallsitkatextitalicsitkasubheadingitalicsitkaheadingitalicsitkadisplayitalicsitkabanneritalic',self.fontsize)
            text = font .render(self.text,1,self.textcolor)
            win.blit(text,(self.x + (self.width/2 - text.get_width()/2),self.y + (self.height/2 - text.get_height()/2)))
    def mouseon(self, position):
        if position[0] > self.x and position[0] < self.x + self.width:
            if position[1] > self.y and position[1] <self.y + self.height:
                return True
        return False
class gobackarrow():
    def __init__(self, color):
        self.color = color
    def draw(self,win):
        pygame.draw.polygon(win, (0,0,0), ((1,30),(41,1),(41,59)))
        pygame.draw.polygon(win,self.color, ((4,30),(39,4),(39,56)))
    def mouseon(self,position,win):
        mcolor = pygame.Surface.get_at(win,(position[0],position[1]))
        if position[0] < 42 and position[1] < 57:
            if mcolor != (0,255,255,255):
                return True
            else:
                return False
                
        else:
            return False
class forwardarrow():
    def __init__(self,color):
        self.color = color
    def draw(self,win):
        pygame.draw.polygon(win, (0,0,0), ((799,30),(759,1),(759,59)))
        pygame.draw.polygon(win, self.color, ((796,30),(761,4),(761,56)))
    def mouseon(self,position,win,background):
        mcolor = pygame.Surface.get_at(win,(position[0],position[1]))
        if position[0] > 758 and position[1] < 57:
            if background:
                if mcolor != (104,188,231,255) and mcolor != (0,15,15,255) and mcolor != (97,176,217,255) and mcolor != (0,0,0,255):
                    return True
                else:
                    return False
            else:
                if mcolor != (0,255,255,255):
                    return True
                else:
                    return False
        else:
            return False
pygame.init()
main_surface = pygame.display.set_mode((800,800))
pygame.display.set_caption('Dots and Shapes')
playgamebutton = button(60,(0,0,0),(255,0,0), 400-(315/2), 80, 315 , 60, 'Play Game')
howtoplaybutton = button(60,(0,0,0),(255,0,0), 400-(360/2), 200, 360, 60, 'How to play')
leaderboardbutton = button(60,(0,0,0),(255,0,0),400-(369/2),320,369,60,'Leaderboard')
squarebutton = button(60,(0,0,0),(255,0,0),400-(200/2),65,200,60,'square')
trianglebutton = button(60,(0,0,0),(255,0,0),400-(232/2),165,232,60,'triangle')
hexagonbutton = button(60,(0,0,0),(255,0,0),400-(254/2),265,254,60,'Hexagon')
mixedbutton = button(60,(0,0,0),(255,0,0),400-(200/2),365,200,60,'Mixed')
yesbutton = button(60,(0,0,0),(255,0,0),150,370,150,60,'yes')
nobutton = button(60,(0,0,0),(255,0,0),550,370,150,60,'no')
backarrow = gobackarrow((255,0,0))
rightarrow = forwardarrow((255,0,0))
background1 = pygame.image.load("3222573.jpg")
background = pygame.image.load("shapesbackground.png")
logo = pygame.image.load("Capturelogo.jpg")
input_box1 = textbox(100,275,140,30)
input_boxes = [input_box1]
instructionsimage = pygame.image.load("instructionsimage.jpg")
instructionsimage2 = pygame.image.load("instructionsimage3.jpg")
instructionsimage3 = pygame.image.load("instructionsimaget.jpg")
instructionsimage4 = pygame.image.load("instructionsimageh.jpg")
instructionsimage5 = pygame.image.load("instructionsimagem.jpg")
controlsimage = pygame.image.load('controlsimage.png')
controlsimage1 = pygame.image.load('controlsimage1.jpg')
controlsimage2 = pygame.image.load('controlsimage2.jpg')
controlsimage3 = pygame.image.load('controlsimage3.jpg')
def firstmenu():
    
    while True:
        main_surface.fill((255,255,0))
        main_surface.blit(background1,(0,0))
        main_surface.blit(background,(0,0))
        main_surface.blit(logo,(282,520))
        playgamebutton.draw(main_surface,(0,0,0))
        howtoplaybutton.draw(main_surface,(0,0,0))
        leaderboardbutton.draw(main_surface,(0,0,0))
        ev = pygame.event.poll()
        position = pygame.mouse.get_pos()
        if ev.type == pygame.NOEVENT:
            if playgamebutton.mouseon(position):
                playgamebutton.textcolor = (0,255,255)
                howtoplaybutton.textcolor = (0,0,0)
                leaderboardbutton.textcolor = (0,0,0)
            elif howtoplaybutton.mouseon(position):
                howtoplaybutton.textcolor = (0,255,0)
                playgamebutton.textcolor = (0,0,0)
                leaderboardbutton.textcolor = (0,0,0)
            elif leaderboardbutton.mouseon(position):
                leaderboardbutton.textcolor = (255,255,255)
                playgamebutton.textcolor = (0,0,0)
                howtoplaybutton.textcolor = (0,0,0)
            else:
                playgamebutton.textcolor = (0,0,0)
                howtoplaybutton.textcolor = (0,0,0)
                leaderboardbutton.textcolor = (0,0,0)
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if playgamebutton.mouseon(position):
                playgamemenu()
            elif howtoplaybutton.mouseon(position):
                howtoplaysection()
            elif leaderboardbutton.mouseon(position):
                leaderboard('AI',False)
        if ev.type == pygame.MOUSEMOTION:
            if playgamebutton.mouseon(position):
                playgamebutton.textcolor = (0,255,255)
            elif howtoplaybutton.mouseon(position):
                howtoplaybutton.textcolor = (0,255,0)
            elif leaderboardbutton.mouseon(position):
                leaderboardbutton.textcolor = (255,255,255)
            else:
                playgamebutton.textcolor = (0,0,0)
                howtoplaybutton.textcolor = (0,0,0)
                leaderboardbutton.textcolor = (0,0,0)
        pygame.display.flip()
def playgamemenu():

    #text_colors = [(0,0,0),(255,0,144),(0,255,0)]
    #textcolor = 0
    while True:
        main_surface.fill((0,255,255))
        main_surface.blit(background,(0,0))
        main_surface.blit(logo,(60,700))
        font = pygame.font.SysFont('anyfont',50)
        mytimer = pygame.time.get_ticks()
        #if mytimer % 100 == 0:
            #if textcolor == 0:
                #textcolor = 1
            #elif textcolor == 1:
               # textcolor = 2
            #elif textcolor == 2:
               # textcolor = 0
                
        text = font.render('Select a mode',1,(0,0,0))
        main_surface.blit(text,(60,10))       
        backarrow.draw(main_surface)
        squarebutton.draw(main_surface,(0,0,0))
        trianglebutton.draw(main_surface,(0,0,0))
        hexagonbutton.draw(main_surface,(0,0,0))
        mixedbutton.draw(main_surface,(0,0,0))
        ev = pygame.event.poll()
        position = pygame.mouse.get_pos()
        mcolor = pygame.Surface.get_at(main_surface,(position[0],position[1]))
        if ev.type == pygame.NOEVENT:
            if backarrow.mouseon(position,main_surface):
                backarrow.color = (0,255,0)
            else:
                backarrow.color = (255,0,0)

        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if backarrow.mouseon(position,main_surface):
                break
            elif squarebutton.mouseon(position):
                setupmenu1('square')
            elif trianglebutton.mouseon(position):
                setupmenu1('triangle')
            elif hexagonbutton.mouseon(position):
                setupmenu1('hexagon')
            elif mixedbutton.mouseon(position):
                setupmenu1('mixed')
        if ev.type == pygame.MOUSEMOTION:
            if backarrow.mouseon(position, main_surface):
                backarrow.color = (0,255,0)
            else:
                backarrow.color = (255,0,0)
            
        pygame.display.flip()
def setupmenu1(mode):
    textfont = pygame.font.SysFont('anyfont',50)
    infotext = textfont.render('Would you like to have timed turns?',1,(0,0,0))
    if mode == 'square':
        infotext2 = textfont.render('You have chosen the SQUARES mode',1,(0,0,0))
    elif mode == 'triangle':
        infotext2 = textfont.render('You have chosen the TRIANGLES mode',1,(0,0,0))
    elif mode == 'hexagon':
        infotext2 = textfont.render('You have chosen the HEXAGONS mode',1,(0,0,0))
    elif mode == 'mixed':
        infotext2 = textfont.render('You have chosen the MIXED mode',1,(0,0,0))
    while True:
        main_surface.fill((0,255,255))
        main_surface.blit(background,(0,0))
        main_surface.blit(infotext,(125,100))
        main_surface.blit(infotext2,(122,60))
        yesbutton.draw(main_surface,(0,0,0))
        nobutton.draw(main_surface,(0,0,0))
        backarrow.draw(main_surface)
        main_surface.blit(logo,(60,700))
        ev = pygame.event.poll()
        position = pygame.mouse.get_pos()
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if yesbutton.mouseon(position):
                if mode == 'square':
                    setupmenu2(True)
                elif mode == 'triangle':
                    trianglegame(True)
                elif mode == 'hexagon':
                    hexagongame(True)
                elif mode == 'mixed':
                    mixedgame(True)
            elif nobutton.mouseon(position):
                if mode == 'square':
                    setupmenu2(False)
                elif mode == 'triangle':
                    trianglegame(False)
                elif mode == 'hexagon':
                    hexagongame(False)
                elif mode == 'mixed':
                    mixedgame(False)
            elif backarrow.mouseon(position,main_surface):
                break
        if ev.type == pygame.MOUSEMOTION:
            if backarrow.mouseon(position,main_surface):
                backarrow.color = (0,255,0)
            else:
                backarrow.color = (255,0,0)
        if ev.type == pygame.NOEVENT:
            if backarrow.mouseon(position,main_surface):
                backarrow.color = (0,255,0)
            else:
                backarrow.color = (255,0,0)
        pygame.display.flip()
def setupmenu2(timed):
    textfont = pygame.font.SysFont('anyfont',50)
    infotext = textfont.render('Would you like to play against the computer?',1,(0,0,0))
    infotext1 = textfont.render('Select NO if you wish to play with 2 players',1,(0,0,0))
    infotext2 = textfont.render('You have chosen the SQUARES mode',1,(0,0,0))
    if timed == True:
        infotext3 = textfont.render('You have also chosen to have time limits',1,(0,0,0))
        infotext4 = textfont.render('on players turns',1,(0,0,0))
    while True:
        main_surface.fill((0,255,255))
        main_surface.blit(background,(0,0))
        if timed == True:
            main_surface.blit(infotext,(50,195))
            main_surface.blit(infotext1,(50,235))
            main_surface.blit(infotext2,(50,75))
            main_surface.blit(infotext3,(50,115))
            main_surface.blit(infotext4,(50,155))
        else:
            main_surface.blit(infotext2,(50,75))
            main_surface.blit(infotext,(50,115))
            main_surface.blit(infotext1,(50,155))
        yesbutton.draw(main_surface,(0,0,0))
        nobutton.draw(main_surface,(0,0,0))
        backarrow.draw(main_surface)
        main_surface.blit(logo,(60,700))
        ev = pygame.event.poll()
        position = pygame.mouse.get_pos()
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if backarrow.mouseon(position,main_surface):
                break
            elif yesbutton.mouseon(position):
                if timed == True:
                    squaregameAI(True)
                else:
                    squaregameAI(False)
            elif nobutton.mouseon(position):
                if timed == True:
                    squaregame(True)
                else:
                    squaregame(False)
        if ev.type == pygame.MOUSEMOTION:
            if backarrow.mouseon(position,main_surface):
                backarrow.color = (0,255,0)
            else:
                backarrow.color = (255,0,0)
        if ev.type == pygame.NOEVENT:
            if backarrow.mouseon(position,main_surface):
                backarrow.color = (0,255,0)
            else:
                backarrow.color = (255,0,0)
        pygame.display.flip()
def howtoplaysection():
    font1 = pygame.font.SysFont('anyfont',25)
    font2 = pygame.font.SysFont('anyfont',20)
    titletext = font1.render('Basic information-',1,(0,0,0))
    text0 = font1.render('Note: completeing shapes earns players an extra turn',1,(0,0,0))
    text1 = font1.render('Note: in this digitised verstion, instead of writing initials on shapes players have completed,',1,(0,0,0))
    text2 = font1.render('a circle will be displayed at the shapes centre',1,(0,0,0))
    text3 = font1.render('Shapes completed by player 1 will be displayed with a blue circle at its centre and shapes',1,(0,0,0))
    text4 = font1.render('completed by player 2 will be displayed with a red circle at the centre',1,(0,0,0))
    text5 = font1.render('Examples can be seen on the next slide-',1,(0,0,0))
    text6 = font1.render('Different Modes-',1,(0,0,0))
    text7 = font1.render('Controls-',1,(0,0,0))
    text8 = font1.render('Squares-',1,(0,0,0))
    text9 = font1.render('Triangles-',1,(0,0,0))
    text10 = font1.render('Hexagons-',1,(0,0,0))
    text11 = font1.render('Mixed-',1,(0,0,0))
    text12 = font2.render('In the menu you can choose whether you would',1,(0,0,0))
    text13 = font2.render('like to have time limits on turns',1,(0,0,0))
    text14 = font1.render('Note: In the squares mode you can choose whether you would like to play against',1,(0,0,0))
    text141 = font1.render('the computer or another player. When playing against the computer, players are',1,(0,0,0))
    text15 = font1.render('not awarded extra turns when completing shapes to make the game more difficult',1,(0,0,0))
    text16 = font1.render('When your mouse is above a dot, it will turn yellow   to indicate you can click it,',1,(0,0,0))
    text17 = font1.render('use the left click to click the dot and click two adjacent dots to create a line.',1,(0,0,0))
    text18 = font1.render('Once a dot is clicked it will turn green to indicate that once an adjacent dot is clicked,',1,(0,0,0))
    text181 = font1.render('a line will be created.',1,(0,0,0))
    text19 =  font1.render('If you wish to undo your click, click the dot again and it will return to red.',1,(0,0,0))
    text20 = font1.render('If you accidentally click 2 unadjacent dots, your turn will not go and the dots will reset',1,(0,0,0))
    text21 = font1.render('so you can continue and attempt to successfully make a line.',1,(0,0,0))
    onetext = font1.render('1.',1,(0,0,0))
    twotext = font1.render('2.',1,(0,0,0))
    threetext = font1.render('3.',1,(0,0,0))
    text22 = font1.render('Click this arrow if you wish to pause the game or access options to return to the main menu',1,(0,0,0))
    text23 = font1.render('The game indicatess which players turn it is, make sure the correct player is clicking dots!',1,(0,0,0))
    while True:
        main_surface.fill((0,255,255))
        main_surface.blit(background,(0,0))
        backarrow.draw(main_surface)
        rightarrow.draw(main_surface)
        main_surface.blit(instructionsimage,(75,69))
        main_surface.blit(titletext,(75,50))
        main_surface.blit(text1,(10,675))
        main_surface.blit(text2,(10,700))
        main_surface.blit(text3,(10,725))
        main_surface.blit(text4,(10,750))
        main_surface.blit(text5,(10,775))
        ev = pygame.event.poll()
        position = pygame.mouse.get_pos()
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == pygame.MOUSEMOTION:
            if backarrow.mouseon(position, main_surface):
                backarrow.color = (0,255,0)
            elif rightarrow.mouseon(position,main_surface,True):
                rightarrow.color = (0,255,0)
            else:
                backarrow.color = (255,0,0)
                rightarrow.color = (255,0,0)
        if ev.type == pygame.NOEVENT:
            if backarrow.mouseon(position, main_surface):
                backarrow.color = (0,255,0)
            elif rightarrow.mouseon(position,main_surface,True):
                rightarrow.color = (0,255,0)
            else:
                backarrow.color = (255,0,0)
                rightarrow.color = (255,0,0)
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if backarrow.mouseon(position, main_surface):
                break
            elif rightarrow.mouseon(position,main_surface,True):
                while True:
                    main_surface.fill((0,255,255))
                    main_surface.blit(background,(0,0))
                    backarrow.draw(main_surface)
                    rightarrow.draw(main_surface)
                    main_surface.blit(instructionsimage2,(75,100))
                    main_surface.blit(instructionsimage3,(75,525))
                    main_surface.blit(instructionsimage4,(505,125))
                    main_surface.blit(instructionsimage5,(505,500))
                    main_surface.blit(text6,(75,50))
                    main_surface.blit(text8,(75,75))
                    main_surface.blit(text12,(362,65))
                    main_surface.blit(text13,(362,80))
                    main_surface.blit(text9,(75,500))
                    main_surface.blit(text10,(505,100))
                    main_surface.blit(text11,(505,475))
                    pygame.draw.line(main_surface,(0,0,0),(310,125),(360,85),5)
                    ev = pygame.event.poll()
                    position = pygame.mouse.get_pos()
                    if ev.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if ev.type == pygame.MOUSEMOTION:
                        if backarrow.mouseon(position, main_surface):
                            backarrow.color = (0,255,0)
                        elif rightarrow.mouseon(position,main_surface,True):
                            rightarrow.color = (0,255,0)
                        else:
                            backarrow.color = (255,0,0)
                            rightarrow.color = (255,0,0)
                    if ev.type == pygame.NOEVENT:
                        if backarrow.mouseon(position, main_surface):
                            backarrow.color = (0,255,0)
                            rightarrow.color = (255,0,0)
                        elif rightarrow.mouseon(position,main_surface,True):
                            rightarrow.color = (0,255,0)
                            backarrow.color = (255,0,0)
                        else:
                            backarrow.color = (255,0,0)
                            rightarrow.color = (255,0,0)
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        if backarrow.mouseon(position,main_surface):
                            break
                        elif rightarrow.mouseon(position,main_surface,True):
                            while True:
                                main_surface.fill((0,255,255))
                                main_surface.blit(background,(0,0))
                                backarrow.draw(main_surface)
                                main_surface.blit(controlsimage,(25,285))
                                main_surface.blit(controlsimage1,(240,173+125))
                                main_surface.blit(controlsimage2,(425,173+125))
                                main_surface.blit(onetext,(25,285))
                                main_surface.blit(twotext,(220,285))
                                main_surface.blit(threetext,(410,285))
                                main_surface.blit(text7,(75,85))
                                main_surface.blit(text14,(75,10))
                                main_surface.blit(text141,(75,35))
                                main_surface.blit(text15,(75,60))
                                main_surface.blit(text16,(75,110))
                                main_surface.blit(text17,(75,135))
                                main_surface.blit(text18,(75,160))
                                main_surface.blit(text181,(75,185))
                                main_surface.blit(text19,(75,210))
                                main_surface.blit(text20,(75,235))
                                main_surface.blit(text21,(75,260))
                                main_surface.blit(controlsimage3,(75,625))
                                main_surface.blit(text23,(25,750))
                                main_surface.blit(text22,(25,550))
                                pygame.draw.line(main_surface,(0,0,0),(100,660),(140,575),5)
                                ev = pygame.event.poll()
                                position = pygame.mouse.get_pos()
                                if ev.type == pygame.QUIT:
                                    pyhame.quit()
                                    sys.exit()
                                if ev.type == pygame.NOEVENT:
                                    if backarrow.mouseon(position, main_surface):
                                        backarrow.color = (0,255,0)
                                    else:
                                        backarrow.color = (255,0,0)
                                if ev.type == pygame.MOUSEMOTION:
                                    if backarrow.mouseon(position, main_surface):
                                        backarrow.color = (0,255,0)
                                    else:
                                        backarrow.color = (255,0,0)
                                if ev.type == pygame.MOUSEBUTTONDOWN:
                                    if backarrow.mouseon(position, main_surface):
                                        break
                                pygame.display.flip()
                                
                    pygame.display.flip()
                
                        
        pygame.display.flip()
def squaregame(timed):
    all_pointdots = []
    all_dots = []
    all_lines = []
    turn = 1
    numberofcompletelines = 0
    numberofcompletepointdots = 0
    for i in range(8):
        new_line = line((169,169,169),(100+(75*i)),(100),(100+(75*(i+1))),(100),5)
        all_lines.append(new_line)
        for j in range (8):
            new_line = line((169,169,169),(100+(75*i)),(100+(75*(j+1))),(100+(75*(i+1))),(100+(75*(j+1))),5)
            all_lines.append(new_line)
    for i in range(8):
        new_line = line((169,169,169),(100),(100+(75*i)),(100),(100+(75*(i+1))),5)
        all_lines.append(new_line)
        for j in range(8):
            new_line = line((169,169,169),(100+(75*(j+1))),(100+(75*i)),(100+(75*(j+1))),(100+(75*(i+1))),5)
            all_lines.append(new_line)
    for i in range(9):
        new_dot = dot((255,0,0),(100+(75*i)),(100),False)
        all_dots.append(new_dot)
        for j in range(8):
            new_dot = dot((255,0,0),(100+(75*i)),100+(75*(j+1)),False)
            all_dots.append(new_dot)
    for i in range(8):
        new_pointdot = pointdot((0,255,255),138+(75*i),138)
        all_pointdots.append(new_pointdot)
        for j in range(7):
            new_pointdot = pointdot((0,255,255),138+(75*i),138+(75*(j+1)))
            all_pointdots.append(new_pointdot)
    if timed == True:
        passed_time = pygame.time.get_ticks()
        timer_count = pygame.time.get_ticks()
        timeleft = 10
    while True:
        if timed == True:
            if timeleft == 0:
                timeleft = 10
            if pygame.time.get_ticks() >= (passed_time + 10000):
                if turn == 1:
                    turn = 2
                else:
                    turn = 1
                passed_time = pygame.time.get_ticks()
            if pygame.time.get_ticks() >= (timer_count + 1000):
                timeleft -= 1
                timer_count = pygame.time.get_ticks()
        points = 0
        for i in all_pointdots:
            if i.color != (0,255,255):
                points = points + 1
        if points > numberofcompletepointdots:
            numberofcompletepointdots = points
            if turn == 1:
                turn = 2
            else:
                turn = 1
        main_surface.fill((0,255,255))
        backarrow.draw(main_surface)
        turnfont = pygame.font.SysFont('anyfont',25)
        if turn == 1:
            turntext = turnfont.render('Player 1s turn',1,(0,0,0))
        else:
            turntext = turnfont.render('Player 2s turn',1,(0,0,0))
        main_surface.blit(turntext,(100,50))
        if timed == True:
            timetext = turnfont.render('Time Remaining:'+str(timeleft),1,(0,0,0))
            main_surface.blit(timetext,(400,50))
        for i in all_lines:
            i.draw(main_surface)
        for i in all_dots:
            i.draw(main_surface)
        for i in all_pointdots:
            i.draw(main_surface)
        position = pygame.mouse.get_pos()
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if backarrow.mouseon(position, main_surface):
                quitcheckmenu()

            for i in all_dots:
                if i.mouseon(position,main_surface):
                    i.isclicked()
            
        if ev.type == pygame.MOUSEMOTION:
            if backarrow.mouseon(position,main_surface):
                backarrow.color = (0,255,0)
            else:
                backarrow.color = (255,0,0)
            for i in all_dots:
                if i.color != (0,255,0):
                    if i.mouseon(position,main_surface):
                        i.color = (255,255,0)
                    else:
                        i.color = (255,0,0)
            
        if ev.type == pygame.NOEVENT:
            if backarrow.mouseon(position, main_surface):
                backarrow.color = (0,255,0)
            else:
                backarrow.color = (255,0,0)
            for i in all_dots:
                if i.color != (0,255,0):
                    if i.mouseon(position,main_surface):
                        i.color = (255,255,0)
                    else:
                        i.color = (255,0,0)
        for i in all_lines:
            a = pygame.Surface.get_at(main_surface,(i.x1,i.y1))
            b = pygame.Surface.get_at(main_surface,(i.x2,i.y2))
            if a == (0,255,0,255) and b == (0,255,0,255):
                i.color = (0,0,0)
        blacklines = 0
        for i in all_lines:
            if i.color == (0,0,0):
                blacklines = blacklines + 1
            
        if blacklines > numberofcompletelines:
            numberofcompletelines = blacklines
            if turn == 1:
                turn = 2
            else:
                turn = 1
            if timed == True:
                timeleft = 10
                passed_time = pygame.time.get_ticks()
        for i in all_pointdots:
                i.surroundedsquare(main_surface,turn)
        blacks = 0
        for i in all_lines:
            if i.color == (0,0,0):
                blacks = blacks + 1
        if blacks == 144:
            for i in all_lines:
                i.draw(main_surface)
            pygame.display.flip()
            for i in all_pointdots:
                i.surroundedsquare(main_surface,turn)
                i.draw(main_surface)
            pygame.display.flip()
            break
            
        pygame.display.flip()
        greens = 0
        for i in all_dots:
            centrecolor = pygame.Surface.get_at(main_surface,(i.x,i.y))
            if centrecolor == (0,255,0,255):
                greens = greens + 1
        if greens == 2:
            for i in all_dots:
                i.reset()
    time.sleep(5)
    endgame(all_pointdots,'square',timed)

def trianglegame(timed):
    topdot = dot((255,0,0),400,100,False)
    all_lines = []
    all_dots = []
    all_pointdots = []
    turn = 1
    numberofcompletelines = 0
    numberofcompletepointdots = 0
    all_dots.append(topdot)
    for i in range(8):
        new_dot = dot((255,0,0),400-(37*(i+1)),100+(65*(i+1)),False)
        all_dots.append(new_dot)
        for j in range(i+1):
            new_dot = dot((255,0,0),(400-(37*(i+1)))+(75*(j+1)),100+(65*(i+1)),False)
            all_dots.append(new_dot)
    for i in range(8):
        new_line = line((169,169,169),400-(37*i),100+(65*i),400-(37*(i+1)),100+(65*(i+1)),5)
        all_lines.append(new_line)
        new_line = line((169,169,169),400+(38*i),100+(65*i),400+(38*(i+1)),100+(65*(i+1)),5)
        all_lines.append(new_line)
        for j in range(i+1):
            l = 1
            new_line = line((165,165,165),(400-(37*(i+1)))+(75*j),100+(65*(i+1)),(400-(37*(i+1)))+(75*(j+1)),100+(65*(i+1)),5)
            all_lines.append(new_line)
        for j in range(i):
            new_line = line((165,165,165),(400-(37*i))+(75*(j+1)),100+(65*i),(400-(37*(i+1)))+(75*(j+1)),100+(65*(i+1)),5)
            all_lines.append(new_line)
            new_line = line((165,165,165),(400+(38*i))-(75*(j+1)),100+(65*i),(400+(38*(i+1)))-(75*(j+1)),(100+(65*(i+1))),5)
            all_lines.append(new_line)
    for i in range(8):
        new_pointdot = pointdot((0,255,255),400,132+(65*i))
        all_pointdots.append(new_pointdot)
        for j in range(i):
            new_pointdot = pointdot((0,255,255),400+(38*(j+1)),132+(65*i))
            all_pointdots.append(new_pointdot)
            new_pointdot = pointdot((0,255,255),400-(37*(j+1)),132+(65*i))
            all_pointdots.append(new_pointdot)
    for i in all_pointdots:
        #checks if object is in one of the lower rows from specific point
        if i.y > 327:
            #checks which row exactly the object is in after a certain row
            #where they need to be changed from
            #only adjusts x coordinate depending on what row they ar in
            #and how far they are from middle(by checking x coord), as lower rows have more objects
            #that need to be adjusted that are further from the middle
            if i.y < 457:
                if i.x > 400 -38 and i.x < 400 +38:
                    #adds 2 to x coord when requirements are satisfied
                    i.x += 2
            elif i.y < 522:
                if i.x > 400 - (38*2) and i.x < 400 + (38*2):
                    i.x += 2
            elif i.y < 587:
                if i.x > 400 - (38*3) and i.x < 400 + (38*3):
                    i.x += 2
            elif i.y < 652:
                if i.x > 400 - (38*4) and i.x < 400 + (38*4):
                    i.x += 2
    if timed == True:
        passed_time = pygame.time.get_ticks()
        timer_count = pygame.time.get_ticks()
        timeleft = 10        
    while True:
        if timed == True:
            if timeleft == 0:
                timeleft = 10
            if pygame.time.get_ticks() >= (passed_time + 10000):
                if turn == 1:
                    turn = 2
                else:
                    turn = 1
                passed_time = pygame.time.get_ticks()
            if pygame.time.get_ticks() >= (timer_count + 1000):
                timeleft -= 1
                timer_count = pygame.time.get_ticks()
        points = 0
        for i in all_pointdots:
            if i.color != (0,255,255):
                points = points + 1
        if points > numberofcompletepointdots:
            numberofcompletepointdots = points
            if turn == 1:
                turn = 2
            else:
                turn = 1
        main_surface.fill((0,255,255))
        backarrow.draw(main_surface)
        turnfont = pygame.font.SysFont('anyfont',25)
        if turn == 1:
            turntext = turnfont.render('Player 1s turn',1,(0,0,0))
        else:
            turntext = turnfont.render('Player 2s turn',1,(0,0,0))
        main_surface.blit(turntext,(100,50))
        if timed == True:
            timetext = turnfont.render('Time Remaining:'+str(timeleft),1,(0,0,0))
            main_surface.blit(timetext,(400,50))
        for i in all_lines:
            i.draw(main_surface)
        for i in all_dots:
            i.draw(main_surface)
        for i in all_pointdots:
            i.draw(main_surface)
        position = pygame.mouse.get_pos()
        ev = pygame.event.poll()

        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if backarrow.mouseon(position, main_surface):
                quitcheckmenu()

            for i in all_dots:
                if i.mouseon(position,main_surface):
                    i.isclicked()

        if ev.type == pygame.MOUSEMOTION:
            if backarrow.mouseon(position,main_surface):
                backarrow.color = (0,255,0)
            else:
                backarrow.color = (255,0,0)

            for i in all_dots:
                if i.color != (0,255,0):
                    if i.mouseon(position,main_surface):
                        i.color = (255,255,0)
                    else:
                        i.color = (255,0,0)

        if ev.type == pygame.NOEVENT:
            if backarrow.mouseon(position, main_surface):
                backarrow.color = (0,255,0)
            else:
                backarrow.color = (255,0,0)

            for i in all_dots:
                if i.color != (0,255,0):
                    if i.mouseon(position,main_surface):
                        i.color = (255,255,0)
                    else:
                        i.color = (255,0,0)

        for i in all_lines:
            a = pygame.Surface.get_at(main_surface,(i.x1,i.y1))
            b = pygame.Surface.get_at(main_surface,(i.x2,i.y2))
            if a == (0,255,0,255) and b == (0,255,0,255):
                i.color = (0,0,0)
        for i in all_pointdots:
            i.surroundedtriangle(main_surface,turn)

        blacklines = 0
        for i in all_lines:
            if i.color == (0,0,0):
                blacklines = blacklines + 1

        if blacklines > numberofcompletelines:
            numberofcompletelines = blacklines
            if turn == 1:
                turn = 2
            else:
                turn = 1
            if timed == True:
                timeleft = 10
                passed_time = pygame.time.get_ticks()
        blacks = 0
        for i in all_lines:
            if i.color == (0,0,0):
                blacks = blacks + 1
        if blacks == 108:
            for i in all_lines:
                i.draw(main_surface)
            for i in all_dots:
                i.draw(main_surface)
            pygame.display.flip()
            for i in all_pointdots:
                i.surroundedtriangle(main_surface,turn)
                i.draw(main_surface)
            pygame.display.flip()
            break
        pygame.display.flip()
        greens = 0
        for i in all_dots:
            centrecolor = pygame.Surface.get_at(main_surface,(i.x,i.y))
            if centrecolor == (0,255,0,255):
                greens = greens + 1
        if greens == 2:
            for i in all_dots:
                i.reset()
    time.sleep(5)
    endgame(all_pointdots,'triangle',timed)
def hexagongame(timed):
    all_lines = []
    all_dots = []
    all_pointdots = []
    turn = 1
    numberofcompletelines = 0
    numberofcompletepointdots = 0
    for i in range(5):
        new_pointdot = pointdot((0,255,255),143+(86*i),150)
        all_pointdots.append(new_pointdot)
        for j in range(3):
            new_pointdot = pointdot((0,255,255),143+(86*i),150+(100*(j+1)))
            all_pointdots.append(new_pointdot)
    for i in range(6):
        new_line = line((128,128,128),100+(86*i),125,100+(86*i),175,5)
        all_lines.append(new_line)
        for j in range(3):
            new_line = line((128,128,128),100+(86*i),125+(100*(j+1)),100+(86*i),175+(100*(j+1)),5)
            all_lines.append(new_line)
    for i in range(5):
        new_line = line((128,128,128),143+(86*i),100,(143+(86*i))-43,125,5)
        all_lines.append(new_line)
        new_line = line((128,128,128),143+(86*i),100,(143+(86*i))+43,125,5)
        all_lines.append(new_line)
        new_line = line((128,128,128),143+(86*i),200,(143+(86*i))-43,175,5)
        all_lines.append(new_line)
        new_line = line((128,128,128),143+(86*i),200,(143+(86*i))+43,175,5)
        all_lines.append(new_line)
        for j in range(3):
            new_line = line((128,128,128),143+(86*i),100+(100*(j+1)),(143+(86*i))-43,125+(100*(j+1)),5)
            all_lines.append(new_line)
            new_line = line((128,128,128),143+(86*i),100+(100*(j+1)),(143+(86*i))+43,125+(100*(j+1)),5)
            all_lines.append(new_line)
            new_line = line((128,128,128),143+(86*i),200+(100*(j+1)),(143+(86*i))-43,175+(100*(j+1)),5)
            all_lines.append(new_line)
            new_line = line((128,128,128),143+(86*i),200+(100*(j+1)),(143+(86*i))+43,175+(100*(j+1)),5)
            all_lines.append(new_line)
    for i in range(6):
        new_dot = dot((255,0,0),100+(86*i),125,False)
        all_dots.append(new_dot)
        for j in range(7):
            new_dot = dot((255,0,0),100+(86*i),125+(50*(j+1)),False)
            all_dots.append(new_dot)
    for i in range(5):
        new_dot = dot((255,0,0),143+(86*i),100,False)
        all_dots.append(new_dot)
        for j in range(4):
            new_dot = dot((255,0,0),143+(86*i),100+(100*(j+1)),False)
            all_dots.append(new_dot)
    if timed == True:
        passed_time = pygame.time.get_ticks()
        timer_count = pygame.time.get_ticks()
        timeleft = 10
    while True:
        if timed == True:
            if timeleft == 0:
                timeleft = 10
            if pygame.time.get_ticks() >= (passed_time + 10000):
                if turn == 1:
                    turn = 2
                else:
                    turn = 1
                passed_time = pygame.time.get_ticks()
            if pygame.time.get_ticks() >= (timer_count + 1000):
                timeleft -= 1
                timer_count = pygame.time.get_ticks()
        points = 0
        for i in all_pointdots:
            if i.color != (0,255,255):
                points = points + 1
        if points > numberofcompletepointdots:
            numberofcompletepointdots = points
            if turn == 1:
                turn = 2
            else:
                turn = 1
        main_surface.fill((0,255,255))
        backarrow.draw(main_surface)
        turnfont = pygame.font.SysFont('anyfont',25)
        if turn == 1:
            turntext = turnfont.render('Player 1s turn',1,(0,0,0))
        else:
            turntext = turnfont.render('Player 2s turn',1,(0,0,0))
        main_surface.blit(turntext,(100,50))
        if timed == True:
            timetext = turnfont.render('Time Remaining:'+str(timeleft),1,(0,0,0))
            main_surface.blit(timetext,(400,50))
        for i in all_lines:
            i.draw(main_surface)
        for i in all_dots:
            i.draw(main_surface)
        for i in all_pointdots:
            i.draw(main_surface)
        position = pygame.mouse.get_pos()
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if backarrow.mouseon(position, main_surface):
                quitcheckmenu()

            for i in all_dots:
                if i.mouseon(position,main_surface):
                    i.isclicked()
            for i in all_lines:
                a = pygame.Surface.get_at(main_surface,(i.x1,i.y1))
                b = pygame.Surface.get_at(main_surface,(i.x2,i.y2))
                if a == (0,255,0,255) and b == (0,255,0,255):
                    i.color = (0,0,0)
            
        if ev.type == pygame.MOUSEMOTION:
            if backarrow.mouseon(position,main_surface):
                backarrow.color = (0,255,0)
            else:
                backarrow.color = (255,0,0)
            for i in all_lines:
                a = pygame.Surface.get_at(main_surface,(i.x1,i.y1))
                b = pygame.Surface.get_at(main_surface,(i.x2,i.y2))
                if a == (0,255,0,255) and b == (0,255,0,255):
                    i.color = (0,0,0)
            for i in all_dots:
                if i.color != (0,255,0):
                    if i.mouseon(position,main_surface):
                        i.color = (255,255,0)
                    else:
                        i.color = (255,0,0)
            
        if ev.type == pygame.NOEVENT:
            if backarrow.mouseon(position, main_surface):
                backarrow.color = (0,255,0)
            else:
                backarrow.color = (255,0,0)
            for i in all_lines:
                a = pygame.Surface.get_at(main_surface,(i.x1,i.y1))
                b = pygame.Surface.get_at(main_surface,(i.x2,i.y2))
                if a == (0,255,0,255) and b == (0,255,0,255):
                    i.color = (0,0,0)
            for i in all_dots:
                if i.color != (0,255,0):
                    if i.mouseon(position,main_surface):
                        i.color = (255,255,0)
                    else:
                        i.color = (255,0,0)

        for i in all_pointdots:
            i.surroundedhexagon(main_surface,turn)
               
        blacklines = 0
        for i in all_lines:
            if i.color == (0,0,0):
                blacklines = blacklines + 1

        if blacklines > numberofcompletelines:
            numberofcompletelines = blacklines
            if turn == 1:
                turn = 2
            else:
                turn = 1
            if timed == True:
                timeleft = 10
                passed_time = pygame.time.get_ticks()
        blacks = 0
        for i in all_lines:
            if i.color == (0,0,0):
                blacks = blacks + 1
        if blacks == 104:
            for i in all_lines:
                i.draw(main_surface)
            pygame.display.flip()
            for i in all_pointdots:
                i.surroundedhexagon(main_surface,turn)
                i.draw(main_surface)
            pygame.display.flip()
            break
            
        pygame.display.flip()
        greens = 0
        for i in all_dots:
            centrecolor = pygame.Surface.get_at(main_surface,(i.x,i.y))
            if centrecolor == (0,255,0,255):
                greens = greens + 1
        if greens == 2:
            for i in all_dots:
                i.reset()
    time.sleep(5)
    endgame(all_pointdots,'hexagon',timed)
def leaderboard(mode,timed):
    leaderboardlist = []
    if mode == 'AI':
        if timed == False:
            leaderboardfile = open("scorefilesquares.txt","r")
        else:
            leaderboardfile = open("scorefileaitime.txt","r")
    elif mode == 'square':
        if timed == True:
            leaderboardfile = open("scorefilenoait.txt","r")
        else:
            leaderboardfile = open("scorefilenoai.txt","r")
    elif mode == 'triangle':
        if timed == True:
            leaderboardfile = open("scorefiletriangletimed.txt","r")
        else:
            leaderboardfile = open("scorefiletriangle.txt","r")
    elif mode == 'hexagon':
        if timed == True:
            leaderboardfile = open("scorefilehexagontimed.txt","r")
        else:
            leaderboardfile = open("scorefilehexagon.txt","r")
    elif mode == 'mixed':
        if timed == True:
            leaderboardfile = open("scorefilemixedt.txt","r")
        else:
            leaderboardfile = open("scorefilemixed.txt","r")
    while True:
        filecontentname = leaderboardfile.readline()
        if filecontentname == '':
            break
        filecontentname = filecontentname.replace('\n','')
        filecontentscore = leaderboardfile.readline()
        filecontentscore = filecontentscore.replace('\n','')
        leaderboardlist.append([filecontentname,int(filecontentscore)])
    print(leaderboardlist)
    orderedlist = []
    while len(orderedlist)<10:
        if not len(leaderboardlist):
            break
        highest = 0
        highestindex = 0
        for x in range(len(leaderboardlist)):
            if (leaderboardlist[x][1])>highest:
                highest = (leaderboardlist[x][1])
                highestindex = x
        orderedlist.append(leaderboardlist[highestindex])
        leaderboardlist.pop(highestindex)
        print(leaderboardlist)
        print(orderedlist)
    print(orderedlist)
    font1 = pygame.font.SysFont('anyfont',50)
    text1 = font1.render('Name',1,(0,0,0))
    text2 = font1.render('Score',1,(0,0,0))
    modetext = font1.render('AI mode',1,(0,0,0))
    timedtext = font1.render('timed',1,(0,0,0))
    squaremodetext = font1.render('square 2 player mode',1,(0,0,0))
    trianglemodetext = font1.render('triangle mode',1,(0,0,0))
    hexagonmodetext = font1.render('hexagon mode',1,(0,0,0))
    mixedmodetext = font1.render('mixed mode',1,(0,0,0))
    while True:
        main_surface.fill((0,255,255))
        backarrow.draw(main_surface)
        if mode != 'mixed':
            rightarrow.draw(main_surface)
        else:
            if timed != True:
                rightarrow.draw(main_surface)
        pygame.draw.line(main_surface,(0,0,0),(400,50),(400,750),5)
        pygame.draw.line(main_surface,(0,0,0),(50,100),(750,100),5)
        main_surface.blit(text1,(170,68))
        main_surface.blit(text2,(540,68))
        if mode == 'AI':
            main_surface.blit(modetext,(50,15))
        elif mode == 'square':
            main_surface.blit(squaremodetext,(50,15))
        elif mode == 'triangle':
            main_surface.blit(trianglemodetext,(50,15))
        elif mode == 'hexagon':
            main_surface.blit(hexagonmodetext,(50,15))
        elif mode == 'mixed':
            main_surface.blit(mixedmodetext,(50,15))
        if timed == True:
            main_surface.blit(timedtext,(420,15))
        for i in range(len(orderedlist)):
            nametext = font1.render(orderedlist[i][0],1,(0,0,0))
            scoretext = font1.render(str(orderedlist[i][1]),1,(0,0,0))
            main_surface.blit(nametext,(50,105+(30*i)))
            main_surface.blit(scoretext,(405,105+(30*i)))
        ev = pygame.event.poll()
        
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        position = pygame.mouse.get_pos()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if backarrow.mouseon(position,main_surface):
                if mode == 'AI' and timed == False:
                    quitcheckmenu()
                elif mode == 'AI' and timed == True:
                    leaderboard('AI',False)
                elif mode == 'square' and timed == False:
                    leaderboard('AI',True)
                elif mode == 'square' and timed == True:
                    leaderboard('square',False)
                elif mode == 'triangle' and timed == False:
                    leaderboard('square',True)
                elif mode == 'triangle' and timed == True:
                    leaderboard('triangle',False)
                elif mode == 'hexagon' and timed == False:
                    leaderboard('triangle',True)
                elif mode == 'hexagon' and timed == True:
                    leaderboard('hexagon',False)
                elif mode == 'mixed' and timed == False:
                    leaderboard('hexagon',True)
                elif mode == 'mixed' and timed == True:
                    leaderboard('mixed',False)
            elif rightarrow.mouseon(position,main_surface,False):
                if mode == 'AI' and timed == False:
                    leaderboard('AI',True)
                elif mode == 'AI' and timed == True:
                    leaderboard('square',False)
                elif mode == 'square' and timed == False:
                    leaderboard('square',True)
                elif mode == 'square' and timed == True:
                    leaderboard('triangle',False)
                elif mode == 'triangle' and timed == False:
                    leaderboard('triangle',True)
                elif mode == 'triangle' and timed == True:
                    leaderboard('hexagon',False)
                elif mode == 'hexagon' and timed == False:
                    leaderboard('hexagon',True)
                elif mode == 'hexagon' and timed == True:
                    leaderboard('mixed',False)
                elif mode == 'mixed' and timed == False:
                    leaderboard('mixed',True)
                
        if ev.type == pygame.MOUSEMOTION:
            if backarrow.mouseon(position,main_surface):
                backarrow.color = (0,255,0)
                rightarrow.color = (255,0,0)
            elif rightarrow.mouseon(position,main_surface,False):
                rightarrow.color = (0,255,0)
                backarrow.color = (255,0,0)
            else:
                backarrow.color = (255,0,0)
                rightarrow.colr = (255,0,0)
        if ev.type == pygame.NOEVENT:
            if backarrow.mouseon(position, main_surface):
                backarrow.color = (0,255,0)
                rightarrow.color = (255,0,0)
            elif rightarrow.mouseon(position,main_surface,False):
                rightarrow.color = (0,255,0)
                backarrow.color = (255,0,0)
            else:
                backarrow.color = (255,0,0)
                rightarrow.color = (255,0,0)
        
        pygame.display.flip()
            



def mixedgame(timed):
    triangle_pointdots = []
    square_pointdots = []
    all_dots = []
    all_lines = []
    turn = 1
    numberofcompletelines = 0
    numberofcompletepointdots = 0
    for i in range(3):
        new_dot = dot((255,0,0),325+(75*i),75,False)
        all_dots.append(new_dot)
        new_line = line((169,169,169),325+(75*i),75,288+(75*i),140,5)
        all_lines.append(new_line)
        new_line = line((169,169,169),325+(75*i),75,363+(75*i),140,5)
        all_lines.append(new_line)
        new_dot = dot((255,0,0),325+(75*i),355,False)
        all_dots.append(new_dot)
        new_line = line((169,169,169),325+(75*i),355,288+(75*i),290,5)
        all_lines.append(new_line)
        new_line = line((169,169,169),325+(75*i),355,363+(75*i),290,5)
        all_lines.append(new_line)
    for i in range(4):
        new_dot = dot((255,0,0),288+(75*i),140,False)
        all_dots.append(new_dot)
        for j in range(2):
            new_dot = dot((255,0,0),288+(75*i),140+(75*(j+1)),False)
            all_dots.append(new_dot)
        for j in range(2):
            new_line = line((169,169,169),288+(75*i),140+(75*j),288+(75*i),140+(75*(j+1)),5)
            all_lines.append(new_line)
    for i in range(2):
        new_line = line((169,169,169),325+(75*i),75,400+(75*i),75,5)
        all_lines.append(new_line)
        new_line = line((169,169,169),325+(75*i),355,400+(75*i),355,5)
        all_lines.append(new_line)
    for i in range(3):
        new_line = line((169,169,169), 288+(75*i),140,288+(75*(i+1)),140,5)
        all_lines.append(new_line)
        for j in range(2):
            new_line = line((169,169,169),288+(75*i),140+(75*(j+1)),288+(75*(i+1)),140+(75*(j+1)),5)
            all_lines.append(new_line)
    for i in range(3):
        new_pointdot = pointdot((0,255,255),326+(75*i),178)
        square_pointdots.append(new_pointdot)
        new_pointdot = pointdot((0,255,255),326+(75*i),253)
        square_pointdots.append(new_pointdot)
    for i in range(5):
        new_pointdot = pointdot((0,255,255),326+(37*i),108)
        triangle_pointdots.append(new_pointdot)
        new_pointdot = pointdot((0,255,255),326+(37*i),323)
        triangle_pointdots.append(new_pointdot)
    turnfont = pygame.font.SysFont('anyfont',25)
    tipstext = turnfont.render('Tips:',1,(0,0,0))
    infotext = turnfont.render('Completing Squares gives you +2 points',1,(0,0,0))
    infotext2 = turnfont.render('Completing Triangles gives you +1 point',1,(0,0,0))
    if timed == True:
        passed_time = pygame.time.get_ticks()
        timer_count = pygame.time.get_ticks()
        timeleft = 10
    while True:
        if timed == True:
            if timeleft == 0:
                timeleft = 10
            if pygame.time.get_ticks() >= (passed_time + 10000):
                if turn == 1:
                    turn = 2
                else:
                    turn = 1
                passed_time = pygame.time.get_ticks()
            if pygame.time.get_ticks() >= (timer_count + 1000):
                timeleft -= 1
                timer_count = pygame.time.get_ticks()
        points = 0
        for i in square_pointdots:
            if i.color != (0,255,255):
                points = points + 1
        for i in triangle_pointdots:
            if i.color != (0,255,255):
                points = points + 1
        if points > numberofcompletepointdots:
            numberofcompletepointdots = points
            if turn == 1:
                turn = 2
            else:
                turn = 1
        main_surface.fill((0,255,255))
        backarrow.draw(main_surface)
        for i in all_lines:
            i.draw(main_surface)
        for i in all_dots:
            i.draw(main_surface)
        for i in square_pointdots:
            i.draw(main_surface)
        for i in triangle_pointdots:
            i.draw(main_surface)
        if turn == 1:
            turntext = turnfont.render('Turn: Player 1s turn',1,(0,0,0))
        else:
            turntext = turnfont.render('Turn: Player 2s turn',1,(0,0,0))
        main_surface.blit(turntext,(100,50))
        main_surface.blit(tipstext,(100,400))
        main_surface.blit(infotext,(100,425))
        main_surface.blit(infotext2,(100,450))
        score1 = 0
        score2 = 0
        for i in square_pointdots:
            if i.color == (0,0,255):
                score1 += 2
            elif i.color == (255,0,0):
                score2 += 2
        for i in triangle_pointdots:
            if i.color == (0,0,255):
                score1 += 1
            elif i.color == (255,0,0):
                score2 += 1
        score1text = turnfont.render('Player 1s score:'+str(score1),1,(0,0,0))
        score2text = turnfont.render('Player 2s score:'+str(score2),1,(0,0,0))
        main_surface.blit(score1text,(100,75))
        main_surface.blit(score2text,(100,100))
        if timed == True:
            timetext = turnfont.render('Time Remaining:'+str(timeleft),1,(0,0,0))
            main_surface.blit(timetext,(400,50))
        position = pygame.mouse.get_pos()
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.flip()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if backarrow.mouseon(position, main_surface):
                quitcheckmenu()

            for i in all_dots:
                if i.mouseon(position,main_surface):
                    i.isclicked()
        if ev.type == pygame.MOUSEMOTION:
            if backarrow.mouseon(position,main_surface):
                backarrow.color = (0,255,0)
            else:
                backarrow.color = (255,0,0)
            for i in all_dots:
                if i.color != (0,255,0):
                    if i.mouseon(position,main_surface):
                        i.color = (255,255,0)
                    else:
                        i.color = (255,0,0)
        if ev.type == pygame.NOEVENT:
            if backarrow.mouseon(position, main_surface):
                backarrow.color = (0,255,0)
            else:
                backarrow.color = (255,0,0)
            for i in all_dots:
                if i.color != (0,255,0):
                    if i.mouseon(position,main_surface):
                        i.color = (255,255,0)
                    else:
                        i.color = (255,0,0)
        for i in all_lines:
            a = pygame.Surface.get_at(main_surface,(i.x1,i.y1))
            b = pygame.Surface.get_at(main_surface,(i.x2,i.y2))
            if a == (0,255,0,255) and b == (0,255,0,255):
                i.color = (0,0,0)
        blacklines = 0
        for i in all_lines:
            if i.color == (0,0,0):
                blacklines = blacklines + 1
            
        if blacklines > numberofcompletelines:
            numberofcompletelines = blacklines
            if turn == 1:
                turn = 2
            else:
                turn = 1
            if timed == True:
                timeleft = 10
                passed_time = pygame.time.get_ticks()
        for i in square_pointdots:
            i.surroundedsquare(main_surface,turn)
        for i in triangle_pointdots:
            i.surroundedtriangle(main_surface,turn)
        blacks = 0
        for i in all_lines:
            if i.color == (0,0,0):
                blacks = blacks + 1
        if blacks == 33:
            for i in all_lines:
                i.draw(main_surface)
            pygame.display.flip()
            for i in square_pointdots:
                i.surroundedsquare(main_surface,turn)
                i.draw(main_surface)
            pygame.display.flip()
            for i in all_lines:
                i.draw(main_surface)
            pygame.display.flip()
            for i in triangle_pointdots:
                if i.color == (0,255,255):
                    if turn == 2:
                        i.color = (0,0,255)
                    else:
                        i.color = (255,0,0)
                i.surroundedtriangle(main_surface,turn)
                i.draw(main_surface)
            pygame.display.flip()
            score1 = 0
            score2 = 0
            for i in square_pointdots:
                if i.color == (0,0,255):
                    score1 += 2
                elif i.color == (255,0,0):
                    score2 += 2
            for i in triangle_pointdots:
                if i.color == (0,0,255):
                    score1 += 1
                elif i.color == (255,0,0):
                    score2 += 1
            score1text = turnfont.render('Player 1s score:'+str(score1),1,(0,0,0))
            score2text = turnfont.render('Player 2s score:'+str(score2),1,(0,0,0))
            main_surface.fill((0,255,255))
            backarrow.draw(main_surface)
            for i in all_lines:
                i.draw(main_surface)
            for i in all_dots:
                i.draw(main_surface)
            for i in square_pointdots:
                i.draw(main_surface)
            for i in triangle_pointdots:
                i.draw(main_surface)
            main_surface.blit(turntext,(100,50))
            main_surface.blit(tipstext,(100,400))
            main_surface.blit(infotext,(100,425))
            main_surface.blit(infotext2,(100,450))
            main_surface.blit(score1text,(100,75))
            main_surface.blit(score2text,(100,100))
            pygame.display.flip()
            break
            
        pygame.display.flip()
        greens = 0
        for i in all_dots:
            centrecolor = pygame.Surface.get_at(main_surface,(i.x,i.y))
            if centrecolor == (0,255,0,255):
                greens = greens + 1
        if greens == 2:
            for i in all_dots:
                i.reset()
    time.sleep(5)

    if score1 > score2:
        turntext = turnfont.render('Player 1 has won, enter your name into the box to upload your data to the leaderboard',1,(0,0,0))
    elif score2 > score1:
        turntext = turnfont.render('Player 2 has won, enter your name into the box to upload your data to the leaderboard',1,(0,0,0))
    elif score1 == score2:
        turntext = turnfont.render('A draw has occured',1,(0,0,0))
    for i in input_boxes:
        i.end = False
    if score1 == score2:
        for i in input_boxes:
            i.end = True
    nametext = turnfont.render('Name:',1,(0,0,0))
    questiontext = turnfont.render('Would you like to see the leaderboard?',1,(0,0,0))
    bigfont = pygame.font.SysFont('anyfont',60)
    endtext = bigfont.render('End of game',1,(0,0,0))
    while True:
        main_surface.fill((0,255,255))
        main_surface.blit(turntext,(75,200))
        if score1 != score2:
            main_surface.blit(nametext,(100,240))
        main_surface.blit(questiontext,(100,325))
        main_surface.blit(endtext,(75,75))
        yesbutton.draw(main_surface,(0,0,0))
        nobutton.draw(main_surface,(0,0,0))
        ev = pygame.event.poll()
        #Updates all text input box objects
        for i in input_boxes:
            i.update1()
            if score2 > score1:
                i.update(ev,score2,'mixed',timed)
            else:
                i.update(ev,score1,'mixed',timed)
            #draws only if its end attribute is equal to false
            #(when user has pressed the enter key while typing in it)
            if i.end == False:
                i.draw(main_surface)
        
        
        if ev.type == pygame.QUIT:
            break
        position = pygame.mouse.get_pos()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if yesbutton.mouseon(position):
                leaderboard('AI',timed)
            elif nobutton.mouseon(position):
                firstmenu()
        
        pygame.display.flip()
            
    pygame.quit()
    sys.exit()
def endgame(all_pointdots,mode,timed):
    turnfont=pygame.font.SysFont('anyfont',25)
    blues = 0
    reds = 0
    for i in all_pointdots:
        if i.color == (255,0,0):
            reds = reds + 1
        else:
            blues = blues + 1
    if blues > reds:
        turntext = turnfont.render('Player 1 has won, enter your name into the box to upload your data to the leaderboard',1,(0,0,0))
    elif reds > blues:
        turntext = turnfont.render('Player 2 has won, enter your name into the box to upload your data to the leaderboard',1,(0,0,0))
    elif reds == blues:
        turntext = turnfont.render('A draw has occured',1,(0,0,0))
    for i in input_boxes:
        i.end = False
    if blues == reds:
        for i in input_boxes:
            i.end = True
    bigfont = pygame.font.SysFont('anyfont',60)
    endtext = bigfont.render('End of game',1,(0,0,0))
    questiontext = turnfont.render('Would you like to see the leaderboard?',1,(0,0,0))
    nametext = turnfont.render('Name:',1,(0,0,0))
    while True:
        main_surface.fill((0,255,255))
        main_surface.blit(turntext,(75,200))
        main_surface.blit(endtext,(75,75))
        main_surface.blit(questiontext,(100,325))
        if blues != reds:
            main_surface.blit(nametext,(100,240))
        yesbutton.draw(main_surface,(0,0,0))
        nobutton.draw(main_surface,(0,0,0))
        ev = pygame.event.poll()
        position = pygame.mouse.get_pos()
        #Updates all text input box objects
        for i in input_boxes:
            i.update1()
            if reds > blues:
                i.update(ev,reds,mode,timed)
            else:
                i.update(ev,blues,mode,timed)
            #draws only if its end attribute is equal to false
            #(when user has pressed the enter key while typing in it)
            if i.end == False:
                i.draw(main_surface)
        if ev.type == pygame.QUIT:
            break
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if nobutton.mouseon(position):
                firstmenu()
            elif yesbutton.mouseon(position):
                leaderboard('AI',timed)
            
        pygame.display.flip()
            
    pygame.quit()
    sys.exit()
def quitcheckmenu():
    font1 = pygame.font.SysFont('anyfont',50)
    text3 = font1.render('Would you like to return to the main menu?',1,(0,0,0))
    while True:
        main_surface.fill((0,255,255))
        main_surface.blit(background,(100,0))
        yesbutton.draw(main_surface,(0,0,0))
        nobutton.draw(main_surface,(0,0,0))
        main_surface.blit(text3,(50,50))
        position = pygame.mouse.get_pos()
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if yesbutton.mouseon(position):
                firstmenu()
            if nobutton.mouseon(position):
                break
        pygame.display.flip()

def squaregameAI(timed):
    all_pointdots = []
    all_dots = []
    all_lines = []
    turn = 1
    numberofcompletelines = 0
    numberofcompletepointdots = 0
    for i in range(8):
        new_line = line((169,169,169),(100+(75*i)),(100),(100+(75*(i+1))),(100),5)
        all_lines.append(new_line)
        for j in range (8):
            new_line = line((169,169,169),(100+(75*i)),(100+(75*(j+1))),(100+(75*(i+1))),(100+(75*(j+1))),5)
            all_lines.append(new_line)
    for i in range(8):
        new_line = line((169,169,169),(100),(100+(75*i)),(100),(100+(75*(i+1))),5)
        all_lines.append(new_line)
        for j in range(8):
            new_line = line((169,169,169),(100+(75*(j+1))),(100+(75*i)),(100+(75*(j+1))),(100+(75*(i+1))),5)
            all_lines.append(new_line)
    for i in range(9):
        new_dot = dot((255,0,0),(100+(75*i)),(100),False)
        all_dots.append(new_dot)
        for j in range(8):
            new_dot = dot((255,0,0),(100+(75*i)),100+(75*(j+1)),False)
            all_dots.append(new_dot)
    for i in range(8):
        new_pointdot = pointdot((0,255,255),138+(75*i),138)
        all_pointdots.append(new_pointdot)
        for j in range(7):
            new_pointdot = pointdot((0,255,255),138+(75*i),138+(75*(j+1)))
            all_pointdots.append(new_pointdot)
    if timed == True:
        passed_time = pygame.time.get_ticks()
        timer_count = pygame.time.get_ticks()
        timeleft = 10
    #continuous game loop to allow updates to appear on screen instantly
    while True:
        if timed == True:
            if timeleft == 0:
                timeleft = 10
            if pygame.time.get_ticks() >= (passed_time + 10000):
                if turn == 1:
                    turn = 2
                else:
                    turn = 1
                passed_time = pygame.time.get_ticks()
            if pygame.time.get_ticks() >= (timer_count + 1000):
                timeleft -= 1
                timer_count = pygame.time.get_ticks()
        
        #draws background and backarrow object in its current status/colour
        main_surface.fill((0,255,255))
        backarrow.draw(main_surface)
        #displays whether it is the computers turn or players turn
        turnfont = pygame.font.SysFont('anyfont',25)
        if turn == 1:
            turntext = turnfont.render('Player 1s turn',1,(0,0,0))
        else:
            turntext = turnfont.render('Computers turn',1,(0,0,0))
        main_surface.blit(turntext,(100,50))
        if timed == True:
            timetext = turnfont.render('Time Remaining:'+str(timeleft),1,(0,0,0))
            main_surface.blit(timetext,(400,50))
        #draws all game objects onto screen in their current state
        for i in all_lines:
            i.draw(main_surface)
        for i in all_dots:
            i.draw(main_surface)
        for i in all_pointdots:
            i.draw(main_surface)
        #checks which event/user input has occured and where the mouse is and responds appropriately
        position = pygame.mouse.get_pos()
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if backarrow.mouseon(position, main_surface):
                quitcheckmenu()
            #only runs code to provide a response to certain user inputs if it is their turn
            #this is so their inputs cannot interfere with the computers turn
            if turn != 2:
                for i in all_dots:
                    if i.mouseon(position,main_surface):
                        i.isclicked()
        if ev.type == pygame.MOUSEMOTION:
            if backarrow.mouseon(position,main_surface):
                backarrow.color = (0,255,0)
            else:
                backarrow.color = (255,0,0)
            if turn != 2:
                for i in all_dots:
                    if i.color != (0,255,0):
                        if i.mouseon(position,main_surface):
                            i.color = (255,255,0)
                        else:
                            i.color = (255,0,0)
        
        if ev.type == pygame.NOEVENT:
            if backarrow.mouseon(position, main_surface):
                backarrow.color = (0,255,0)
            else:
                backarrow.color = (255,0,0)
            if turn != 2:
                for i in all_dots:
                    if i.color != (0,255,0):
                        if i.mouseon(position,main_surface):
                            i.color = (255,255,0)
                        else:
                            i.color = (255,0,0)
        #if it is the computers turn, strategicallly pick a line that the computer should fill for its turn
        if turn == 2:
            complete = False
            all_lines2 = []
            #stores all lines that are not black in a seperate list
            for i in all_lines:
                if i.color != (0,0,0):
                    all_lines2.append(i)
            all_lines3 = []
            for i in all_pointdots:
                #checks how many lines of each square has been filled^
                check = i.partlysurroundedsquare(main_surface)
                #checks if there are squares with one remaining line to fill, identifies which line object this is and turns it black
                if check[0] == 1:
                    for j in all_lines2:
                        if check[1][1] == "horizontal":
                            if j.y1 == j.y2:
                                if j.x1 < check[1][0][0] and j.x2 > check[1][0][0] and ((j.y1 <= check[1][0][1] + 5 and j.y1 > check[1][0][1] - 5)or(j.y1>=check[1][0][1]-5 and j.y1<check[1][0][1]+5)):
                                    j.color = (0,0,0)
                                    print("horizontal")
                                    #AI turn is complete- later code will not need to be run when this is True
                                    complete = True
                                    break
                        else:
                            if j.x1 == j.x2:
                                if j.y1 < check[1][0][1] and j.y2 > check[1][0][1] and ((j.x1 <= check[1][0][0] + 5 and j.x1>check[1][0][0]-5)or(j.x1>=check[1][0][0]-5 and j.x1<check[1][0][0]+5)):
                                    j.color = (0,0,0)
                                    print("vertical")
                                    complete = True
                                    break
                    break
                #Checks for shapes with 2 lines remaining, uses coordinates to check which line object it is adds to list all_lines3, to keep track of/store lines that should not be selected/turned black for the turn
                elif check[0] == 2:
                    for j in all_lines2:
                        if check[1][0][1] == "horizontal":
                            if j.y1 == j.y2:
                                if j.x1 < check[1][0][0][0] and j.x2 > check[1][0][0][0] and ((j.y1 <= check[1][0][0][1] + 5 and j.y1 > check[1][0][0][1] - 5)or(j.y1>=check[1][0][0][1]-5 and j.y1<check[1][0][0][1]+5)):
                                    if j not in all_lines3:
                                        all_lines3.append(j)
                        else:
                            if j.x1 == j.x2:
                                if j.y1 < check[1][0][0][1] and j.y2 > check[1][0][0][1] and ((j.x1 <= check[1][0][0][0] + 5 and j.x1 > check[1][0][0][0] - 5)or(j.x1>=check[1][0][0][0]-5 and j.x1<check[1][0][0][0]+5)):
                                    if j not in all_lines3:
                                        all_lines3.append(j)
                        if check[1][1][1] == "horizontal":
                            if j.y1 == j.y2:
                                if j.x1 < check[1][1][0][0] and j.x2 > check[1][1][0][0] and ((j.y1 <= check[1][1][0][1] + 5 and j.y1 > check[1][1][0][1] - 5)or(j.y1>=check[1][1][0][1]-5 and j.y1<check[1][1][0][1]+5)):
                                    if j not in all_lines3:
                                        all_lines3.append(j)
                        else:
                            if j.x1 == j.x2:
                                if j.y1 < check[1][1][0][1] and j.y2 > check[1][1][0][1] and ((j.x1 <= check[1][1][0][0] + 5 and j.x1 > check[1][1][0][0] - 5)or(j.x1>=check[1][1][0][0]-5 and j.x1<check[1][1][0][0]+5)):
                                    if j not in all_lines3:
                                        all_lines3.append(j)
            
            #checks through list of empty lines, and adds lines from that list to new list if they are also not in the all_lines3 list(list of empty lines that should not be selected-lines of squares with 2 lines remaining)
            #in order to prevent choosing them
            #picks a random line object from new list all_lines4 if it is not empty(there are available line objects to pick from) and turns it black, completes turn
            all_lines4 = []
            for i in all_lines2:
                if i not in all_lines3:
                    all_lines4.append(i)
            if len(all_lines4) != 0 and complete != True:
                randomnum = random.randint(0,len(all_lines4)-1)
                for i in all_lines:
                    if all_lines4[randomnum] == i:
                        i.color = (0,0,0)
                        complete = True
                        break
            #If there were not previously lines which earn the AI points, or lines to pick from in the all_lines4 list, the complete variable will still be false as turn is incomplete
            #Picks any random available line and turns it black to complete turn and keep game going
            if complete != True:
                all_lines2 = []
                for i in all_lines:
                    if i.color != (0,0,0):
                        all_lines2.append(i)
                randomnum = random.randint(0,len(all_lines2)-1)
                for i in all_lines2:
                    if all_lines2[randomnum] == i:
                        i.color = (0,0,0)
                        break
                complete = True
        #Makes updates to games from AI or user input
        for i in all_lines:
            a = pygame.Surface.get_at(main_surface,(i.x1,i.y1))
            b = pygame.Surface.get_at(main_surface,(i.x2,i.y2))
            if a == (0,255,0,255) and b == (0,255,0,255):
                i.color = (0,0,0)
        for i in all_pointdots:
            i.surroundedsquare(main_surface,turn)
        blacklines = 0
        for i in all_lines:
            if i.color == (0,0,0):
                blacklines = blacklines + 1
            
        if blacklines > numberofcompletelines:
            numberofcompletelines = blacklines
            if turn == 1:
                turn = 2
            else:
                turn = 1
            if timed == True:
                timeleft = 10
                passed_time = pygame.time.get_ticks()
        
        blacks = 0
        for i in all_lines:
            if i.color == (0,0,0):
                blacks = blacks + 1
        if blacks == 144:
            for i in all_lines:
                i.draw(main_surface)
            pygame.display.flip()
            for i in all_pointdots:
                i.surroundedsquare(main_surface,turn)
                i.draw(main_surface)
            pygame.display.flip()
            break
            
        pygame.display.flip()
        greens = 0
        for i in all_dots:
            centrecolor = pygame.Surface.get_at(main_surface,(i.x,i.y))
            if centrecolor == (0,255,0,255):
                greens = greens + 1
        if greens == 2:
            for i in all_dots:
                i.reset()
    time.sleep(5)
    blues = 0
    reds = 0
    for i in all_pointdots:
        if i.color == (255,0,0):
            reds = reds + 1
        else:
            blues = blues + 1
    if blues > reds:
        turntext = turnfont.render('Player 1 has won, enter your name into the box to upload your data to the leaderboard',1,(0,0,0))
    elif reds > blues:
        turntext = turnfont.render('Computer has won, enter your name into the box to upload your data to the leaderboard',1,(0,0,0))
    elif reds == blues:
        turntext = turnfont.render('A draw has occured, enter your name into the box to upload your data to the leaderboard',1,(0,0,0))
    for i in input_boxes:
        i.end = False
    bigfont = pygame.font.SysFont('anyfont',60)
    endtext = bigfont.render('End of game',1,(0,0,0))
    questiontext = turnfont.render('Would you like to see the leaderboard?',1,(0,0,0))
    nametext = turnfont.render('Name:',1,(0,0,0))
    while True:
        main_surface.fill((0,255,255))
        main_surface.blit(turntext,(75,200))
        main_surface.blit(endtext,(75,75))
        main_surface.blit(questiontext,(100,325))
        main_surface.blit(nametext,(100,240))
        yesbutton.draw(main_surface,(0,0,0))
        nobutton.draw(main_surface,(0,0,0))
        ev = pygame.event.poll()
        position = pygame.mouse.get_pos()
        #Updates all text input box objects
        for i in input_boxes:
            i.update1()
            i.update(ev,blues,'AI',timed)
            if i.end == False:
                i.draw(main_surface)
        if ev.type == pygame.QUIT:
            break
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if yesbutton.mouseon(position):
                leaderboard('AI',timed)
            elif nobutton.mouseon(position):
                firstmenu()
        pygame.display.flip()
            
    pygame.quit()
    sys.exit()        
firstmenu()

#ADD A FUNCTION TO CHANGE TURNS USING ALL_LINES AS PARAMETER

