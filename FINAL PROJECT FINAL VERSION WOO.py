import pygame
import random
import math
import sys
import time

# Define some colors
BLACK =(0, 0, 0)
GRAY = (40, 35, 35)
WHITE = (255, 255, 255)
PURPLE = (113, 70, 255)
GREEN = (120, 213, 132)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 138, 201)
BROWN = (139, 69, 19)
ORANGE = (253, 113, 6)
SKY_BLUE = (135, 206, 235)

#skin colours
SKIN1_RED = (255, 204, 153)
SKIN1_YELLOW = (255, 255, 153)
SKIN2 = (255, 212, 124)
SKIN3 = (255, 187, 118)
SKIN4 = (226, 166, 106)
SKIN5 = (153, 76, 0)
SKIN6 = (102, 51, 0)
SKIN7 = (51, 25, 0)

SKIN_COLOURS = [SKIN1_RED, SKIN1_YELLOW, SKIN2, SKIN3, SKIN4, SKIN5, SKIN6, SKIN7]
HAIR_COLOURS = [BLACK, YELLOW, BROWN, ORANGE]

pygame.init()

# Set the width and height of the screen [width, height]
size = (1000, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Coders!!")






#new code
class Tree():

    def __init__ (self, x1, x2, x3, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2

    #Draws an individual tree
    def draw (self):
        pygame.draw.rect (screen, BROWN, (self.x1 + 80, self.y1, 40, 60)) #Log
        pygame.draw.polygon (screen, GREEN, ([self.x1, self.y1],[self.x3, self.y1],[self.x2, self.y2] ))
        pygame.draw.polygon (screen, GREEN, ([self.x1, self.y1-100], [self.x3, self.y1-100],[self.x2, self.y1-230]))
        pygame.draw.polygon (screen, GREEN, ([self.x1, self.y1-200], [self.x3, self.y1-200], [self.x2, self.y1-330]))
        #pygame.draw.rect (screen, YELLOW, (self.x1, 525, 20, 10)) #Yellow Lines

    #Makes that individual tree move
    def move(self):
        self.x1 -= 5
        self.x2 -= 5
        self.x3 -= 5

class Lines():

    def __init__ (self, x):
        self.x = x

    def draw (self):
        pygame.draw.rect (screen, YELLOW, (self.x, 525, 20, 10))

    def move (self):
        self.x -= 5


class Background():
    def __init__ (self, existing_objs):
        #A list of trees is being made here and you will need to add a tree to this list every time you want to draw a new one
        self.objects = existing_objs
        
    def add_trees(self):
        self.objects.append (Tree (1000, 1100, 1200, 410, 280))
        #This method will add a tree to your list, you will want to do this to get the moving effect
        #Remember that each new tree begins on the very right and they all look the same
        #remove return None when done writing this method, it's a temporary command
        
    def draw_objects(self):
        for i in self.objects:
            i.draw ()    
        #Look through each tree object in your list (self.trees) and draw it 
        

    def move_objects(self):
        for i in self.objects:
            i.move ()
        #Traverse through each tree object in your list (self.trees) and shift it horizontally (look through the Tree methods)

    def add_yellow_line(self):
        self.objects.append (Lines (1000))


y_coor = 525

exp = 0
ex = 0

trees = []
for i in range (0, 3):
    trees.append(Tree(250+360*i, 350+360*i, 450+360*i, 410, 280))
tree = Background(trees)
lines = []
for i in range(0,11):
    lines.append(Lines(100*i))
yellow_lines = Background(lines)


#A class for the coders!!
class coders():
    def __init__(self, skin_col, interest, hair_type, hair_col, xpos):
        self.skin_col = skin_col
        self.interest = interest
        self.hair_col = hair_col
        self.hair_type = hair_type
        self.xpos = xpos
        self.pants = skin_col

    def draw(self, pos):
        self.pos = pos
        #hair ponytails
        pygame.draw.circle(screen, self.hair_col, (self.xpos - 3, 440), 33)
        pygame.draw.rect(screen, self.hair_col, (self.xpos - 36, 440, 66, 55))
        if self.hair_type == 2:
            pygame.draw.circle(screen, self.hair_col, (self.xpos - 13, 410), 10)
            pygame.draw.circle(screen, self.hair_col, (self.xpos + 2, 410), 10)

            pygame.draw.circle(screen, self.hair_col, (self.xpos - 23, 418), 10)
            pygame.draw.circle(screen, self.hair_col, (self.xpos + 15, 418), 10)

            
            pygame.draw.circle(screen, self.hair_col, (self.xpos - 33, 428), 10)
            pygame.draw.circle(screen, self.hair_col, (self.xpos + 25, 428), 10)

            pygame.draw.circle(screen, self.hair_col, (self.xpos - 13, 410), 10)
            pygame.draw.circle(screen, self.hair_col, (self.xpos + 2, 410), 10)

            pygame.draw.circle(screen, self.hair_col, (self.xpos - 23, 418), 10)
            pygame.draw.circle(screen, self.hair_col, (self.xpos + 15, 418), 10)

            pygame.draw.circle(screen, self.hair_col, (self.xpos - 36, 440), 10)
            pygame.draw.circle(screen, self.hair_col, (self.xpos - 36, 455), 10)
            pygame.draw.circle(screen, self.hair_col, (self.xpos - 36, 470), 10)
            pygame.draw.circle(screen, self.hair_col, (self.xpos - 36, 485), 10)

            pygame.draw.circle(screen, self.hair_col, (self.xpos + 30, 440), 10)
            pygame.draw.circle(screen, self.hair_col, (self.xpos + 30, 455), 10)
            pygame.draw.circle(screen, self.hair_col, (self.xpos + 30, 470), 10)
            pygame.draw.circle(screen, self.hair_col, (self.xpos + 30, 485), 10)

            pygame.draw.circle(screen, self.hair_col, (self.xpos - 23, 490), 9)
            pygame.draw.circle(screen, self.hair_col, (self.xpos - 14, 490), 9)
            pygame.draw.circle(screen, self.hair_col, (self.xpos - 5, 490), 9)
            pygame.draw.circle(screen, self.hair_col, (self.xpos + 4, 490), 9)
            pygame.draw.circle(screen, self.hair_col, (self.xpos + 14, 490), 9)
            pygame.draw.circle(screen, self.hair_col, (self.xpos + 23, 490), 9)
        #face
        pygame.draw.circle(screen, self.skin_col, (self.xpos, 450), 30)
        #eyes
        pygame.draw.circle(screen, BLACK, (self.xpos , 440), 5)
        pygame.draw.circle(screen, BLACK, (self.xpos + 15, 440), 4)
        #hair bangs
        pygame.draw.rect(screen, self.hair_col, (self.xpos - 20, 420, 40, 10))    
        #smile
        #pygame.draw.line(screen, RED, (self.xpos + 1, 453), (self.xpos + 16, 453), 3)
        #pygame.draw.circle(screen, RED, (self.xpos + 11, 458), 6)
        #pygame.draw.circle(screen, RED, (self.xpos + 5, 457), 3)
        pygame.draw.arc(screen, RED, (self.xpos, 440, 20, 20), 180/180 * math.pi, 360/180 * math.pi, 1 )


        if self.interest == 1:
            #dress
            pygame.draw.rect(screen, PINK, (self.xpos - 5, 480, 10, 41))
            pygame.draw.polygon(screen, PINK, [(self.xpos - 5, 500), (self.xpos - 5, 520), (self.xpos - 15, 520), (self.xpos - 5, 500)])
            pygame.draw.polygon(screen, PINK, [(self.xpos + 5, 500), (self.xpos + 5, 520), (self.xpos + 15, 520), (self.xpos + 5, 500)])
        elif self.interest == 2:
            pygame.draw.rect(screen, PURPLE, (self.xpos - 8, 480, 16, 30))
            pygame.draw.rect(screen, BLUE, (self.xpos - 8, 510, 16, 10))
            self.pants = BLUE
        elif self.interest == 3:
            pygame.draw.rect(screen, BLACK, (self.xpos - 8, 480, 16, 20))
            pygame.draw.rect(screen, self.skin_col, (self.xpos - 8, 500, 16, 10))
            pygame.draw.rect(screen, BLACK, (self.xpos - 8, 510, 16, 10))
            self.pants = BLACK
        
        if self.pos == 1:
            #legs
            pygame.draw.line(screen, self.pants, (self.xpos - 6, 520), (self.xpos - 6, 550), 5)
            pygame.draw.line(screen, self.pants, (self.xpos + 6, 520), (self.xpos + 2, 550), 5)
            #arms
            pygame.draw.line(screen, self.skin_col, (self.xpos - 7, 478), (self.xpos - 20, 505), 5)
            pygame.draw.line(screen, self.skin_col, (self.xpos + 7, 478), (self.xpos + 10, 505), 5)
        elif self.pos == 2:
            #legs
            pygame.draw.line(screen, self.pants, (self.xpos - 6, 520), (self.xpos - 10, 550), 5)
            pygame.draw.line(screen, self.pants, (self.xpos + 6, 520), (self.xpos + 6, 550), 5)
            #arms
            pygame.draw.line(screen, self.skin_col, (self.xpos - 7, 478), (self.xpos - 10, 505), 5)
            pygame.draw.line(screen, self.skin_col, (self.xpos + 7, 478), (self.xpos + 20, 505), 5)


insult_list = ["Girls can't code", "Stay at home!", "No education", "Don't fail!", "no STEM for girls"]
#a class for the obstacles
class obstacle():
    
    def __init__(self, num):
        self.num = num
        self.col = random.choice(SKIN_COLOURS)
        self.speech = random.choice(insult_list)

    def show(self, obs_type):
        if self.num == 1:
            pygame.draw.circle(screen, WHITE, (600, 350), 40)
            pygame.draw.circle(screen, WHITE, (650, 350), 40)
            pygame.draw.circle(screen, WHITE, (700, 350), 40)
            pygame.draw.circle(screen, WHITE, (680, 405), 10)
            pygame.draw.circle(screen, WHITE, (705, 430), 10)
            
            pygame.font.init()
            myfont = pygame.font.SysFont(None,30)
            insult = myfont.render(self.speech, 1, BLACK)
            screen.blit(insult, (570, 340))
            pygame.display.flip
            
            pygame.draw.line(screen, self.col, (790, 448), (740, 410), 10)
            pygame.draw.line(screen, self.col, (810, 448), (860, 410), 10)
            if obs_type == 1:
                pygame.draw.circle(screen, ORANGE, (800, 470), 40)
                pygame.draw.rect(screen, BLUE, (763, 485, 73, 25))
                pygame.draw.line(screen, BLUE, (770, 500), (743, 533), 15)
                pygame.draw.line(screen, BLUE, (825, 500), (856, 533), 15)
            elif obs_type == 2:
                pygame.draw.circle(screen, BLACK, (800, 340), 15)
                pygame.draw.circle(screen, BLACK, (780, 350), 15)
                pygame.draw.circle(screen, BLACK, (820, 350), 15)
                pygame.draw.line(screen, self.col, (770, 500), (753, 533), 15)
                pygame.draw.line(screen, self.col, (825, 500), (846, 533), 15)
                pygame.draw.circle(screen, PINK, (800, 470), 40)
                pygame.draw.polygon(screen, PINK, ((763, 435), (836, 435), (743, 510), (856, 510) ))
                
            pygame.draw.circle(screen, BLACK, (800, 390), 45)
            pygame.draw.circle(screen, self.col, (800, 400), 40)
            pygame.draw.line(screen, BLACK, (795, 390), (780, 375), 7)
            pygame.draw.line(screen, BLACK, (805, 390), (820, 375), 7)
            pygame.draw.circle(screen, BLACK, (790, 400), 5)
            pygame.draw.circle(screen, BLACK, (810, 400), 5)
            pygame.draw.rect(screen, BLACK, (765, 360, 65, 10))
            pygame.draw.arc(screen, RED, (790, 410, 20, 20), 0/180 * math.pi, 180/180 * math.pi, 1 )
        elif self.num == 2:
            if obs_type == 1:
                pygame.draw.ellipse(screen, WHITE, (545, 320, 170, 75))
                pygame.font.init()
                font2 = pygame.font.SysFont(None,40)
                error = font2.render("var x = 7", 1, BLACK)
                screen.blit(error, (570, 340))
                pygame.display.flip

                pygame.draw.ellipse(screen, RED, (545, 270, 170, 65))
                pygame.font.init()
                font2 = pygame.font.SysFont(None,30)
                error = font2.render("SyntaxError!!", 1, WHITE)
                screen.blit(error, (570, 295))
                pygame.display.flip
                
            elif obs_type == 2:
                pygame.draw.ellipse(screen, WHITE, (545, 320, 170, 75))
                pygame.font.init()
                font2 = pygame.font.SysFont(None,40)
                error = font2.render("if (x = 1){ }", 1, BLACK)
                screen.blit(error, (565, 340))
                pygame.display.flip

                pygame.draw.ellipse(screen, RED, (545, 270, 170, 65))
                pygame.font.init()
                font2 = pygame.font.SysFont(None,30)
                error = font2.render("SyntaxError!!", 1, WHITE)
                screen.blit(error, (570, 295))
                pygame.display.flip
        elif self.num == 3:
            if obs_type == 1:
                pygame.draw.ellipse(screen, WHITE, (545, 295, 210, 105))
                pygame.font.init()
                font = pygame.font.SysFont(None,25)
                error = font.render("var x = 5 ;", 1, BLACK)
                screen.blit(error, (600, 315))
                pygame.display.flip

                pygame.font.init()
                font2 = pygame.font.SysFont(None,25)
                error = font2.render("var y = '3' ; ", 1, BLACK)
                screen.blit(error, (600, 340))
                pygame.display.flip

                pygame.font.init()
                font2 = pygame.font.SysFont(None,25)
                error = font2.render("var z = x * y ; ", 1, BLACK)
                screen.blit(error, (600, 365))
                pygame.display.flip

                pygame.draw.ellipse(screen, RED, (545, 250, 210, 65))
                pygame.font.init()
                font2 = pygame.font.SysFont(None,25)
                error = font2.render("Find the line with error!", 1, WHITE)
                screen.blit(error, (555, 275))
                pygame.display.flip
            elif obs_type == 2:
                pygame.draw.ellipse(screen, WHITE, (545, 295, 210, 105))
                pygame.font.init()
                font = pygame.font.SysFont(None,20)
                error = font.render("for(i = 0; i < 10; i++){", 1, BLACK)
                screen.blit(error, (595, 320))
                pygame.display.flip

                pygame.font.init()
                font2 = pygame.font.SysFont(None,20)
                error = font2.render("  println(i);", 1, BLACK)
                screen.blit(error, (595, 340))
                pygame.display.flip

                pygame.font.init()
                font2 = pygame.font.SysFont(None,20)
                error = font2.render("}", 1, BLACK)
                screen.blit(error, (595, 360))
                pygame.display.flip

                pygame.draw.ellipse(screen, RED, (545, 250, 210, 65))
                pygame.font.init()
                font2 = pygame.font.SysFont(None,20)
                error = font2.render("Would this run? 1=yes, 2=no", 1, WHITE)
                screen.blit(error, (555, 275))
                pygame.display.flip
                
                
        
    

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#starter girl
skin = random.choice(SKIN_COLOURS)
ha = random.choice(HAIR_COLOURS)
ht = random.randint(1, 2)
inte = random.randint(1, 3)
girl = coders(skin, inte, ht, ha, 600)

#girl coders
girl_coders = [girl]

#variables
walking = 1
walkingcount = 1
earnedscore = False
score = 0
obstacle_showing = False
pause_time = 0
start_timer = False
number = 0
obs = obstacle(number)
obs_type = 0
keypressedfor = 0
missed = True


pygame.font.init()
font = pygame.font.SysFont("vgafix.fon", 25)
message1 = font.render ("Hey", 1, WHITE)
screen.blit(message1, (570, 340))



key = 0
#intro loop
keypressed = 1
while keypressed < 13:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    pygame.draw.rect(screen, GRAY, [0, 450, 1000, 150])
    if event.type == pygame.KEYUP:
        key = 0

    if ex != 20:
        ex = ex +1
    else:
        yellow_lines.add_yellow_line()
        ex = 0
    
    yellow_lines.draw_objects()
    yellow_lines.move_objects()
    # --- Drawing code should go here
    walkingcount = walkingcount + 1
    girl_coders[0].draw(walking)
    if walkingcount % 10 == 0:
        if walking == 1:
            walking = 2
        elif walking == 2:
            walking = 1

    # These are the slides for the intro!
    if keypressed == 1:
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 50)
        message1 = font.render ("<GIRL CODE>", 1, WHITE)
        screen.blit(message1, (350, 250))

        fontA = pygame.font.SysFont("OCR A Extended", 20)
        messageA = fontA.render ("press the space bar to skip the intro and the right arrow for the next slide", 1, RED)
        screen.blit(messageA, (20, 560))
        
    elif keypressed == 2:
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 20)
        message2 = font.render ("-Women make up half of the total U.S.", 1, WHITE)
        screen.blit (message2, (100, 50))
        
        message22 = font.render("college-educated workforce but only 29% of", 1, WHITE)
        screen.blit (message22, (100, 100))
        
        message23 = font.render ("the science and engineering workforce.", 1, WHITE)
        screen.blit (message23, (100, 150))
        
        message24 = font.render ("-Female scientists and engineers are", 1, WHITE)
        screen.blit (message24, (100, 200))
        
        message25 = font.render("concentrated in different occupations than men", 1, WHITE)
        screen.blit (message25, (100, 250))
        
        message26 = font.render ("with relatively high shares of women in ", 1, WHITE)
        screen.blit (message26, (100, 300))
        
        message27 = font.render ("the social sciences (62%) and biological,", 1, WHITE)
        screen.blit (message27, (100,350))
        
        message28 = font.render ("agricultural and environmental life sciences,",1, WHITE)
        screen.blit (message28, (100, 400))
        
        message29 = font.render ("(48%) and relatively low shares in engineering", 1, WHITE)
        screen.blit (message29, (100, 450))
        
        message30 = font.render ("(15%) and computer and mathematical sciences (25%).",1, WHITE)
        screen.blit (message30, (100, 500))

        fontA = pygame.font.SysFont("OCR A Extended", 20)
        messageA = fontA.render ("press the space bar to skip the intro and the right arrow for the next slide", 1, RED)
        screen.blit(messageA, (20, 560))
        
    elif keypressed == 3:
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 20)
        message31 = font.render ("The goal of this game is to add as many", 1, WHITE)
        screen.blit (message31, (100, 75))

        message31 = font.render ("girls to the 'movement' (the line of girls) as", 1, WHITE)
        screen.blit (message31, (100, 125))

        message32 = font.render ("possible and overcome obstacles!", 1, WHITE)
        screen.blit (message32, (100, 175))

        fontA = pygame.font.SysFont("OCR A Extended", 20)
        messageA = fontA.render ("press the space bar to skip the intro and the right arrow for the next slide", 1, RED)
        screen.blit(messageA, (20, 560))
        
    elif keypressed == 4:
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 20)
        message4 = font.render ("There are a few types of obstacles your", 1, WHITE)
        screen.blit (message4, (75, 50))

        message42 = font.render ("characters will face. Some use code!", 1, WHITE)
        screen.blit (message42, (75, 100))
        

        message43 = font.render ("There are two types of obstacles you will face:", 1, WHITE)
        screen.blit (message43, (75, 200))
        
        message44 = font.render("SYNTAX ERRORS or HATERS", 1, WHITE)
        screen.blit (message44, (75, 250))
        
        message45 = font.render("SYNTAX ERROR: A character or strong incorrectly placed", 1, WHITE)
        screen.blit(message45, (75, 300))
        
        message46 = font.render("in a command or instruction that causes", 1, WHITE)
        screen.blit (message46, (75, 350))

        message47 = font.render ("a failure in execution of code!", 1, WHITE)
        screen.blit (message47, (75, 400))

        fontA = pygame.font.SysFont("OCR A Extended", 20)
        messageA = fontA.render ("press the space bar to skip the intro and the right arrow for the next slide", 1, RED)
        screen.blit(messageA, (20, 560))
        
    elif keypressed == 5:
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 20)
        message5 = font.render ("Don't worry though!", 1, WHITE)
        screen.blit (message5, (75, 50))
        
        message52 = font.render("Every coder experiences syntax errors!", 1, WHITE)
        screen.blit (message52, (75, 100))
        
        message53 = font.render("Don't be discouraged!!!", 1, WHITE)
        screen.blit (message53, (75, 150))
        
        message54 = font.render("The only wrong decision is to give up!", 1, WHITE)
        screen.blit (message54, (75, 200))

        fontA = pygame.font.SysFont("OCR A Extended", 20)
        messageA = fontA.render ("press the space bar to skip the intro and the right arrow for the next slide", 1, RED)
        screen.blit(messageA, (20, 560))
        
    elif keypressed == 6:
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 20)
        message6 = font.render ("PUNCTUATION SYNTAX ERROR EXAMPLE:", 1, WHITE)
        screen.blit (message6, (50, 50))
        
        message62 = font.render ("';' are like the '.'s in computer languages!", 1, WHITE)
        screen.blit (message62, (50, 150))
        
        message63 = font.render ("Think of '{}'s (after functions) as ", 1, WHITE)
        screen.blit (message63, (50, 200))
        
        message64 = font.render ("paragraphs.  They let the computers know that", 1, WHITE)
        screen.blit (message64, (50, 250))
        
        message65 = font.render ("these commands belong to the function!", 1, WHITE)
        screen.blit (message65, (50, 300))

        message66 = font.render ("Your code will not run if there is not a semicolon", 1, WHITE)
        screen.blit (message66, (50, 350))

        message67 = font.render ("at the end of a statement!", 1, WHITE)
        screen.blit (message67, (50, 400))

        message68 = font.render ("EXAMPLE: x = 10; is GOOD", 1, WHITE)
        screen.blit (message68, (50, 450))

        message69 = font.render ("x = 10 is BAD because there is no semicolon!", 1, WHITE)
        screen.blit (message69, (50, 500))

        fontA = pygame.font.SysFont("OCR A Extended", 20)
        messageA = fontA.render ("press the space bar to skip the intro and the right arrow for the next slide", 1, RED)
        screen.blit(messageA, (20, 560))
        
    elif keypressed == 7:
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 20)
        message7 = font.render ("USING EQUAL SIGNS PROPERLY:", 1, WHITE)
        screen.blit (message7, (25,50))
        
        message72 = font.render ("When you want to check if a variable, such as x, equals 10,", 1, WHITE)
        screen.blit (message72, (25, 150))
        
        message73 = font.render ("you must use TWO equal signs, like this: x == 10;", 1, WHITE)
        screen.blit (message73, (25, 200))

        message74 = font.render ("x = 10 would not be correct, because there are not", 1, WHITE)
        screen.blit (message74, (25, 250))

        message75 = font.render ("TWO equal signs!", 1, WHITE)
        screen.blit (message75, (25, 300))

        fontA = pygame.font.SysFont("OCR A Extended", 20)
        messageA = fontA.render ("press the space bar to skip the intro and the right arrow for the next slide", 1, RED)
        screen.blit(messageA, (20, 560))
        
    elif keypressed == 8:
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 20)
        message8 = font.render ("DEBUGGING", 1, WHITE)
        screen.blit (message8, (35, 50))
        
        message82 = font.render ("-Debugging is a crucial aspect of mastering", 1, WHITE)
        screen.blit (message82, (35, 100))
        
        message83 = font.render ("computer science!", 1, WHITE)
        screen.blit (message83, (35, 150))
        
        message84 = font.render ("-Everyone makes mistakes!  The important thing", 1, WHITE)
        screen.blit (message84, (35, 200))
        
        message85 = font.render ("is that you learn from them!", 1, WHITE)
        screen.blit (message85, (35, 250))

        fontA = pygame.font.SysFont("OCR A Extended", 20)
        messageA = fontA.render ("press the space bar to skip the intro and the right arrow for the next slide", 1, RED)
        screen.blit(messageA, (20, 560))
        
    elif keypressed == 9:
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 20)

        message9 = font.render ("HOW TO COMBAT HATERS:", 1, WHITE)
        screen.blit (message9, (50, 50))
        
        message92 = font.render ("Sometimes when you are a girl who codes, you may ", 1, WHITE)
        screen.blit (message92, (50, 150))

        message93 = font.render ("encounter 'haters.' To defeat the", 1, WHITE)
        screen.blit (message93, (50, 200))

        message94 = font.render("haters enter the number of girls on the", 1, WHITE)
        screen.blit (message94, (50, 250))

        message95 = font.render ("screen to unite them against the haters.", 1, WHITE)
        screen.blit (message95, (50, 300))

        message96 = font.render ("EXAMPLE: if there are two girls on the screen, and you", 1, WHITE)
        screen.blit (message96, (50, 350))

        message97 = font.render ("encounter a hater, enter the number 2 on the keyboard!", 1, WHITE)
        screen.blit (message97, (50, 400))

        fontA = pygame.font.SysFont("OCR A Extended", 20)
        messageA = fontA.render ("press the space bar to skip the intro and the right arrow for the next slide", 1, RED)
        screen.blit(messageA, (20, 660))
        
    elif keypressed == 10:
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 20)
        message10 = font.render ("STRING AND INTEGER ADDITION:", 1, WHITE)
        screen.blit (message10, (50, 50))

        message101 = font.render ("You cannot add an integer", 1, WHITE)
        screen.blit (message101, (50, 100))

        message102 = font.render ("(such as a number)", 1, WHITE)
        screen.blit (message102, (50, 150))

        message103 = font.render ("and words (in a string) together.", 1, WHITE)
        screen.blit (message103, (50, 200))

        message104 = font.render ("This will cause an error!", 1, WHITE)
        screen.blit (message104, (50, 250))

        message105 = font.render ("EXAMPLE: 1 + 1 is GOOD", 1, WHITE)
        screen.blit (message105, (50, 300))

        message106 = font.render ("and '1' + 'purple' is GOOD", 1, WHITE)
        screen.blit (message106, (50, 350))

        message107 = font.render ("but 1 + '1' will not work!", 1, WHITE)
        screen.blit (message107, (50, 400))

        fontA = pygame.font.SysFont("OCR A Extended", 20)
        messageA = fontA.render ("press the space bar to skip the intro and the right arrow for the next slide", 1, RED)
        screen.blit(messageA, (20, 560))
        
    elif keypressed == 11:
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 20)
        message11 = font.render ("LOOPS:", 1, WHITE)
        screen.blit (message11, (50, 50))

        message112 = font.render ("Sometimes we use 'for' loops to make", 1, WHITE)
        screen.blit (message112, (50, 100))

        message113 = font.render ("something repeat.", 1, WHITE)
        screen.blit (message113, (50, 150))

        message114 = font.render ("When you use 'for' loops and include", 1, WHITE)
        screen.blit (message114, (50, 200))

        message115 = font.render ("variables, such as 'x',", 1, WHITE)
        screen.blit (message115, (50, 250))

        message116 = font.render ("You must declare these variables first!", 1, WHITE)
        screen.blit (message116, (50, 300))

        fontA = pygame.font.SysFont("OCR A Extended", 20)
        messageA = fontA.render ("press the space bar to skip the intro and the right arrow for the next slide", 1, RED)
        screen.blit(messageA, (20, 560))
        
    elif keypressed == 12:
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 20)
        message12 = font.render ("BEGIN THE GAME!!", 1, WHITE)
        screen.blit (message12, (50, 50))
        
        message122 = font.render ("You're now ready to take on the virtual world", 1, WHITE)
        screen.blit (message122, (50, 100))
        
        message123 = font.render ("and become a hero!  You must show women can do", 1, WHITE)
        screen.blit (message123, (50, 150))
        
        message124 = font.render ("anything!", 1, WHITE)
        screen.blit (message124, (50, 200))

        fontA = pygame.font.SysFont("OCR A Extended", 20)
        messageA = fontA.render ("press the space bar to skip the intro and the right arrow for the next slide", 1, RED)
        screen.blit(messageA, (20, 560))
        
        
    if event.type == pygame.KEYDOWN:

        # These if statements control the info part of the game.
        key = key + 1
        if key == 1 and event.key == pygame.K_RIGHT and keypressed == 1:
            keypressed = 2
            
        elif key == 1 and event.key == pygame.K_RIGHT and keypressed == 2:
            keypressed = 3
            
        elif key == 1 and event.key == pygame.K_RIGHT and keypressed == 3:
            keypressed = 4
            
        elif key == 1 and event.key == pygame.K_RIGHT and keypressed == 4:
            keypressed = 5
            
        elif key == 1 and event.key == pygame.K_RIGHT and keypressed == 5:
            keypressed = 6
            
        elif key == 1 and event.key == pygame.K_RIGHT and keypressed == 6:
            keypressed = 7
            
        elif key == 1 and event.key == pygame.K_RIGHT and keypressed == 7:
            keypressed = 8
            
        elif key == 1 and event.key == pygame.K_RIGHT and keypressed == 8:
            keypressed = 9
            
        elif key == 1 and event.key == pygame.K_RIGHT and keypressed == 9:
            keypressed = 10
            
        elif key == 1 and event.key == pygame.K_RIGHT and keypressed == 10:
            keypressed = 11
            
        elif key == 1 and event.key == pygame.K_RIGHT and keypressed == 11:
            keypressed = 12
            
        elif key == 1 and event.key == pygame.K_RIGHT and keypressed == 12:
            keypressed = 13
            
        elif key == 1 and event.key == pygame.K_SPACE:
            keypressed = 13
            
        elif key == 1 and event.key == pygame.K_LEFT and keypressed == 2:
            keypressed = 1
            
        elif key == 1 and event.key == pygame.K_LEFT and keypressed == 3:
            keypressed = 2
            
        elif key == 1 and event.key == pygame.K_LEFT and keypressed == 4:
            keypressed = 3
            
        elif key == 1 and event.key == pygame.K_LEFT and keypressed == 5:
            keypressed = 4
            
        elif key == 1 and event.key == pygame.K_LEFT and keypressed == 6:
            keypressed = 5
            
        elif key == 1 and event.key == pygame.K_LEFT and keypressed == 7:
            keypressed = 6
            
        elif key == 1 and event.key == pygame.K_LEFT and keypressed == 8:
            keypressed = 7
            
        elif key == 1 and event.key == pygame.K_LEFT and keypressed == 9:
            keypressed = 8
            
        elif key == 1 and event.key == pygame.K_LEFT and keypressed == 10:
            keypressed = 9
            
        elif key == 1 and event.key == pygame.K_LEFT and keypressed == 11:
            keypressed = 10
            
        elif key == 1 and event.key == pygame.K_LEFT and keypressed == 12:
            keypressed = 11

    if event.type == pygame.KEYUP:
        key = 0

    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)







# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    if event.type == pygame.KEYDOWN:
        keypressedfor += 1
        earnedscore = False

        # These are if statements for the different obstacles the characters face
        if event.key == pygame.K_SEMICOLON and number == 2 and obs_type == 1 and keypressedfor == 1:
            earnedscore = True
            number = 0
            obs_type = 0
            pause_time = 350
            missed = False
            
        elif event.key == pygame.K_EQUALS and number == 2 and obs_type == 2 and keypressedfor == 1:
            earnedscore = True
            number = 0
            obs_type = 0
            pause_time = 350
            missed = False
            
        elif number == 1 and pygame.key.name(event.key) == str(len(girl_coders))  and keypressedfor == 1:
            earnedscore = True
            number = 0
            obs_type = 0
            pause_time = 350
            missed = False
            
        elif number == 3 and obs_type == 1 and keypressedfor == 1 and event.key == pygame.K_2:
            earnedscore = True
            number = 0
            obs_type = 0
            pause_time = 350
            missed = False
            
        elif number == 3 and obs_type == 2 and keypressedfor == 1 and event.key == pygame.K_2:
            earnedscore = True
            number = 0
            obs_type = 0
            pause_time = 350
            missed = False
            
        elif keypressedfor == 1 and start_timer:
            score = score - 1
            
        elif score < 0 and event.key == pygame.K_UP:
            screen.fill(SKY_BLUE)
            walking = 1
            walkingcount = 1
            earnedscore = False
            score = 0
            obstacle_showing = False
            pause_time = 0
            start_timer = False
            number = 0
            obs = obstacle(number)
            obs_type = 0
            keypressedfor = 0
            missed = True
            curli = len(girl_coders) - 1
            for i in range(curli):
                girl_coders.pop()
                
        elif len(girl_coders) == 10 and event.key == pygame.K_UP:
            screen.fill(SKY_BLUE)
            walking = 1
            walkingcount = 1
            earnedscore = False
            score = 0
            obstacle_showing = False
            pause_time = 0
            start_timer = False
            number = 0
            obs = obstacle(number)
            obs_type = 0
            keypressedfor = 0
            missed = True
            for i in range(9):
                girl_coders.pop()
            
            

    if event.type == pygame.KEYUP:
        keypressedfor = 0

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(SKY_BLUE)
    pygame.draw.rect(screen, GRAY, [0, 450, 1000, 150])

    if exp != 60:
        exp = exp +1
    else:
        tree.add_trees()
        exp = 0

        
    tree.draw_objects()
    tree.move_objects()

    if ex != 20:
        ex = ex +1
    else:
        yellow_lines.add_yellow_line()
        ex = 0
    
    yellow_lines.draw_objects()
    yellow_lines.move_objects()

    

    # --- Drawing code should go here

    
    # This randomizes each girl in the game
    if earnedscore and start_timer:
        score += 1
        print(score)
        earnedscore = False
        sk = random.choice(SKIN_COLOURS)
        ha2 = random.choice(HAIR_COLOURS)
        ht2 = random.randint(1, 2)
        inte2 = random.randint(1, 3)
        xx = 600 - (65*len(girl_coders))
        girl_coders.append(coders(sk, inte2, ht2, ha2, xx))
    
    for i in range(len(girl_coders)):
        girl_coders[i].draw(walking)

    
    # This controls how often the obstacles appear
    if walkingcount % 10 == 0:
        if walking == 1:
            walking = 2
        elif walking == 2:
            walking = 1

    if walkingcount % 500 == 0:
        obstacle_showing = True

    
    # This randomizes the obstacles
    if obstacle_showing:
        number = random.randint(1,3)
        obs = obstacle(number)
        obs_type = random.randint(1, 2)
        obstacle_showing = False
        start_timer = True

    # If an obstacle is missed, then the score is deducted by one point
    if start_timer:
        pause_time += 1
        obs.show(obs_type)
        if pause_time >= 350:
            start_timer = False
            pause_time = 0
            number = 0
            obs_type = 0
            if missed:
                score = score - 1
            missed = True


    # This controls the score at the top of the screen
    walkingcount += 1
    scoreString = "SCORE: " + str(score)
    pygame.font.init()
    myfont5 = pygame.font.SysFont(None,50)
    text = myfont5.render(scoreString, 1, WHITE)
    screen.blit(text, (0, 0))
    pygame.display.flip

    if score < 0:
        walkingcount = 1
        screen.fill(PURPLE)
        pygame.font.init()
        myfont6 = pygame.font.SysFont(None,75)
        text3 = myfont6.render("GAME OVER!!", 1, WHITE)
        screen.blit(text3, (350, 300))

        # This gets displayed when the player loses :(
        fontA = pygame.font.SysFont(None, 30)
        messageA = fontA.render ("Never Give Up!! you can always try again!! press the up arrow for another chance.", 1, YELLOW)
        screen.blit(messageA, (40, 560))
        
        pygame.display.flip
        
    # This gets displayed when the player wins
    if len(girl_coders) == 10:
        screen.fill(PURPLE)
        pygame.font.init()
        myfont6 = pygame.font.SysFont(None,60)
        text3 = myfont6.render("YOU WON! 10 more girls joined the movement!", 1, WHITE)
        screen.blit(text3, (50, 300))
        pygame.display.flip

    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
