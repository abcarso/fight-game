s = 0 #initial screen
####### button dimensions
x1 = 170
x2 = 390
x3 = 610
x4 = 830
y1 = 600
l = 200
h = 100
######################### reset values
RlungeDamage = 4
RfeintDamage = 2
RblockGain = 2

RbLDamage = 4
RbFDamage = 2
RbBGain = 2

RplayerHealth = 20
RbossHealth = 20
Rattacks = [2,4]
RplayerAttack = 0

Rresponse1 = ""
Rresponse2 = ""
###############################

##################################player values
lungeDamage = 4
feintDamage = 2
blockGain = 2
playerHealth = 20

#################################boss values
bLDamage = 4
bFDamage = 2
bBGain = 2
bossHealth = 20


attacks = [2,4] #list of initial AI moves
playerAttack = 0 #player move
click = False #click value

#text values
m1 = ""
m2 = ""
m3 = ""
response1 = ""
response2 = ""


def setup(): #initializes screen rendering and file load ins
    global img, img2, img3
    
    size(1200,1000)
    frameRate(30)
    c = color(200,50,70)
    background(c)
    textAlign(CENTER)
    img = loadImage("MansionFight.jpg")
    img2 = loadImage("TheMonsterFight.png")
    img3 = loadImage("TheKnightFight.png")
    
    
    
    
    
def draw(): #draws the correct screen
    global s
    
    if s == 0:
        startScreen()
    elif s == 1:
        fightScreen()
    elif s == 2:
        loseScreen()
    elif s == 3:
        winScreen()
        
        
        
        
        
def mouseClicked(): #checks if the player has clicked a button
    global s, click
    
    if s == 0 or s == 2 or s == 3:
        x = 450
        y = 800
        print(mouseX,mouseY)
        if mouseX > x and mouseX < x+300 and mouseY > y and mouseY < y+100:
            click = True
            
    elif s == 1:
        if mouseX > x1 and mouseX < x1+l and mouseY > y1 and mouseY < y1+h:
            playerAttack = 1 #lunge
            print("You picked lunge.")
            calcAttacks(playerAttack)
            click = True
        elif mouseX > x2 and mouseX < x2+l and mouseY > y1 and mouseY < y1+h:
            playerAttack = 2 #parry
            print("You picked parry.")
            calcAttacks(playerAttack)
            click = True
        elif mouseX > x3 and mouseX < x3+l and mouseY > y1 and mouseY < y1+h:
            playerAttack = 3 #feint
            print("You picked feint.")
            calcAttacks(playerAttack)
            click = True
        elif mouseX > x4 and mouseX < x4+l and mouseY > y1 and mouseY < y1+h:
            playerAttack = 4 #block
            print("You picked block.")
            calcAttacks(playerAttack)
            click = True





def calcAttacks(p): #calculates the damage for the fight and also adjusts the AI attack list
    global attacks, playerHealth, bossHealth, lungeDamage, feintDamage, blockGain, bLDamage, bFDamage, bBGain, response1, response2
    x = len(attacks)-1
    ind = int(random(x))
    b = attacks[ind]
    
    if p == 1: #if player picks lunge
        #add opposite of 1 to the AI attack list
        attacks = attacks + [2]
        if b == 1:
            #both lunge
            response1 = "Lunge"
            response2 = "Lunge"
            playerHealth = playerHealth - bLDamage
            bossHealth = bossHealth - lungeDamage
        elif b == 2:
            #player is parried
            response1 = "Lunge"
            response2 = "Parry"
            playerHealth = playerHealth - (lungeDamage/2)
        elif b == 3:
            #player lunges boss feints
            response1 = "Lunge"
            response2 = "Feint"
            playerHealth = playerHealth - bFDamage
            bossHealth = bossHealth - lungeDamage
        elif b == 4:
            #lunge beats block
            response1 = "Lunge"
            response2 = "Block"
            bossHealth = bossHealth -lungeDamage + bBGain
            
            
    elif p == 2: #if player picks parry
        #add opposite of 2 to the AI attack list
        attacks = attacks + [3]
        if b == 1:
            #boss is parried
            response1 = "Parry"
            response2 = "Lunge"
            bossHealth = bossHealth - (bLDamage/2)
        elif b == 2:
            #both parry nothing happens
            response1 = "Parry"
            response2 = "Parry"
        elif b == 3:
            #boss feints around parry
            response1 = "Parry"
            response2 = "Feint"
            playerHealth = playerHealth - bFDamage
        elif b == 4:
            #boss gains
            response1 = "Parry"
            response2 = "Block"
            bossHealth = bossHealth + bBGain
            
    elif p == 3: #if player picks feint
        #add opposite of 3 to the AI attack list
        attacks = attacks + [4]
        if b == 1:
            #boss lunges player feints
            response1 = "Feint"
            response2 = "Lunge"
            playerHealth = playerHealth - bLDamage
            bossHealth = bossHealth - feintDamage
        elif b == 2:
            #player feints around a parry
            response1 = "Feint"
            response2 = "Parry"
            bossHealth = bossHealth - feintDamage
        elif b == 3:
            #both feint
            response1 = "Feint"
            response2 = "Feint"
            playerHealth = playerHealth - bFDamage
            bossHealth = bossHealth - feintDamage
        elif b == 4:
            #feint is blocked and boss gains
            response1 = "Feint"
            response2 = "Block"
            bossHealth = bossHealth + bBGain
            
    elif p == 4: #if player picks block
        #add opposite of 4 to the AI attack list
        attacks = attacks + [1]
        if b == 1:
            #boss lunges through block
            response1 = "Block"
            response2 = "Lunge"
            playerHealth = playerHealth - bLDamage + blockGain
        elif b == 2:
            #player gains
            response1 = "Block"
            response2 = "Parry"
            playerHealth = playerHealth + blockGain
        elif b == 3:
            #player blocks feint and gains
            response1 = "Block"
            response2 = "Feint"
            playerHealth = playerHealth + blockGain
        elif b == 4:
            #both gain
            response1 = "Block"
            response2 = "Block"
            playerHealth = playerHealth + blockGain
            bossHealth = bossHealth + bBGain
    print(attacks)
    
    
    
    
    
def startScreen(): #creates the start screen and button
    global s, click
    c = color(250,0,50)
    background(c)
    textAlign(CENTER)
    
    x = 450
    y = 800
    
    c = color(50,50,50)
    fill(c)
    
    rect(x-5,y+5,310,100)
    
    
    c = color(0,0,0)
    fill(c)
    
    textSize(70)
    text("The Fencing Game!",600,150)
    
    textSize(50)
    text("In this game you will take turns selecting",600,300)
    text("actions to combat the game boss.",600,400)
    text("You can attack and defend.",600,500)
    text("You win if the boss's health reaches 0.",600,600)
    text("Obviously if yours reaches 0 you die.",600,700)
    
    if click == False:
        c = color(100,100,100)
        fill(c)
        rect(x,y,300,100)
        c = color(255,255,255)
        fill(c)
        textSize(70)
        text("Start",600,y+75)
        
    else:
        c = color(70,70,70)
        fill(c)
        rect(x,y+5,300,100)
        c = color(255,255,255)
        fill(c)
        textSize(70)
        text("Start",600,y+75)
        s = 1
        click = False
        
        
def fightScreen(): #creates the fighting screen with background, buttons, and info
    global s, x1, x2, x3, x4, l, h, click, m1, m2, m3, lungeDamage, feintDamage, blockGain, response1, response2
    
    background(0)
    textAlign(CENTER)
    
    image(img,0,0,1200,1000) #background image
    image(img2,700,200,150,300) #monster image
    image(img3,300,200,150,300) #knight image
    
    
    if playerHealth <= 0: #checks for lose condition
        s = 2
        click = False
        
    elif bossHealth <= 0: #checks for win condition
        s = 3
        click = False
        
    else:
        c = color(255,255,255) #displays player and boss health
        fill(c)
        textSize(40)
        text("Player Health: " + str(playerHealth), 200, 50)
        text("Boss Health: " + str(bossHealth), 1000, 50)
        
        c = color(50,50,50) #displays shadow rectangles for the buttons
        fill(c)
        rect(x1-5,y1+5,l+10,h)
        rect(x2-5,y1+5,l+10,h)
        rect(x3-5,y1+5,l+10,h)
        rect(x4-5,y1+5,l+10,h)
        
        
        if click == False: #display buttons as not clicked
            c = color(100,100,100) 
            fill(c)
            rect(x1,y1,l,h)
            rect(x2,y1,l,h)
            rect(x3,y1,l,h)
            rect(x4,y1,l,h)        
            
            c = color(250,250,250)
            fill(c)
            textSize(60)
            text("Lunge",x1+l/2,y1+3*h/4)
            text("Parry",x2+l/2,y1+3*h/4)
            text("Feint",x3+l/2,y1+3*h/4)
            text("Block",x4+l/2,y1+3*h/4)
            
        elif click == True: #display buttons as clicked
            c = color(70,70,70)
            fill(c)
            rect(x1,y1+5,l,h)
            rect(x2,y1+5,l,h)
            rect(x3,y1+5,l,h)
            rect(x4,y1+5,l,h)        
            
            c = color(250,250,250)
            fill(c)
            textSize(60)
            text("Lunge",x1+l/2,y1+3*h/4+5)
            text("Parry",x2+l/2,y1+3*h/4+5)
            text("Feint",x3+l/2,y1+3*h/4+5)
            text("Block",x4+l/2,y1+3*h/4+5)
            
            click = False
            
            
        c = color(250,0,50) #draw the moves that were made on screen
        fill(c)
        textSize(70)
        text(response1,400,400)
        text(response2,800,400)
    
    
        c = color(250,250,250) #display text box
        fill(c)
        rect(100,y1+h+10,1000,1000-y1-h-20)
        
        if mouseX > x1 and mouseX < x1+l and mouseY > y1 and mouseY < y1+h: #display choice of action info
            m1 = "Lunge: Can attack for " + str(lungeDamage) + " damage."
            m2 = "Is parried back at you for half damage."
            m3 = "Overwhelms a block."
        elif mouseX > x2 and mouseX < x2+l and mouseY > y1 and mouseY < y1+h:
            m1 = "Parry: Defends against a lunge."
            m2 = "Can reflect a lunge back for half damage."
            m3 = "Is unable to counter a feint."
        elif mouseX > x3 and mouseX < x3+l and mouseY > y1 and mouseY < y1+h:
            m1 = "Feint: Can attack for " + str(feintDamage) + " damage."
            m2 = "Can attack despite a parry."
            m3 = "Is countered by a block."
        elif mouseX > x4 and mouseX < x4+l and mouseY > y1 and mouseY < y1+h:
            m1 = "Block: Can gain back " + str(blockGain) + " health."
            m2 = "Completely blocks a feint."
            m3 = "Is overwhelmed by a lunge."
        
        c = color(0,0,0) #display chosen text
        fill(c)
        textSize(30)
        textAlign(LEFT)
        text(m1,110,((y1+h+10)+(1000-y1-h-20)/4))
        text(m2,110,((y1+h+10)+(1000-y1-h-20)/2))
        text(m3,110,((y1+h+10)+(1000-y1-h-20)*3/4))
        
        
def loseScreen(): #draw lose screen
    global s, click
    
    c = color(100,100,100)
    background(c)
    
    x = 450
    y = 800
    
    c = color(50,50,50) #draw shadow rectangle
    fill(c)
    rect(x-5,y+5,310,100)
    
    c = color(0,0,0) #draw title text
    fill(c)
    textAlign(CENTER)
    textSize(70)
    text("You Lose",600,150)
    
    if click == False: #display button as not clicked
        c = color(100,100,100)
        fill(c)
        rect(x,y,300,100)
        c = color(255,255,255)
        fill(c)
        textSize(65)
        text("Restart?",600,y+75)
        
    else: #display button as clicked and reset to start screen
        c = color(70,70,70)
        fill(c)
        rect(x,y+5,300,100)
        c = color(255,255,255)
        fill(c)
        textSize(65)
        text("Restart?",600,y+75)
        
        reset()
        click = False
        s = 0
        
        
def winScreen(): #draw win screen
    global s, click
    c = color(255,255,255)
    background(c)
    
    x = 450
    y = 800
    
    c = color(50,50,50) #draw shadow rectangle
    fill(c)
    rect(x-5,y+5,310,100)
    
    c = color(0,0,0) #draw title text
    fill(c)
    textAlign(CENTER)
    textSize(70)
    text("You Win!",600,150)
    
    
    if click == False: #display button as not clicked
        c = color(100,100,100)
        fill(c)
        rect(x,y,300,100)
        c = color(255,255,255)
        fill(c)
        textSize(65)
        text("Restart?",600,y+75)
        
    else: #display button as clicked and reset to start screen
        c = color(70,70,70)
        fill(c)
        rect(x,y+5,300,100)
        c = color(255,255,255)
        fill(c)
        textSize(65)
        text("Restart?",600,y+75)
        
        reset()
        click = False
        s = 0
        
        
def reset(): #reset all variables
    global lungeDamage, RlungeDamage, feintDamage, RfeintDamage, blockGain, RblockGain, bLDamage, RbLDamage, bFDamage, RbFDamage, bBGain, RbBGain, playerHealth, RplayerHealth, bossHealth, RbossHealth, attacks, Rattacks, playerAttack, RplayerAttack, response1, Rresponse1, response2, Rresponse2 
    lungeDamage = RlungeDamage
    feintDamage = RfeintDamage
    blockGain = RblockGain
    bLDamage = RbLDamage
    bFDamage = RbFDamage
    bBGain = RbBGain
    
    playerHealth = RplayerHealth
    bossHealth = RbossHealth
    attacks = Rattacks
    playerAttack = RplayerAttack
    
    response1 = Rresponse1
    response2 = Rresponse2
    
