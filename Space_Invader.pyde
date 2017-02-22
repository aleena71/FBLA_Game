x_pos = 90
time = 0
EX_pos = 20
EY_pos = 180
E_right = True
E_left = False
right_counter = 0
left_counter = 0
change = False
now = True
score =0
enemies_death = [False, False, False, False, False, False, False, False, False, False]
enx_pos = [20, 70, 120, 170, 220, 270, 320, 370, 420, 470]
start_ = True
bullets = []
bullets2 = []
shooting_rate = 0
Game_Over = False
start_timer = 0
flash = True
Won = False

def setup():
    frameRate(20)
    size(600, 600)

def spawn_bullets(q):
    if len(q) > 0:
        for i in range(len(q)):
            q[i][1] -= 5
            stroke(255, 255, 255)
            line(q[i][0],q[i][1],q[i][0],q[i][1] + 10)

def spawn_badbullets(q):
    if len(q) > 0:
        for i in range(len(q)):
            if q[i][1] > 450:
                q[i][1] -= 5
                stroke(255, 255, 255)
                line(q[i][0],q[i][1],q[i][0],q[i][1] + 10)

def enemy_killer():
    global score
    if len(bullets) > 0:
        for i in range(len(bullets)):
            for x in range(len(enemies_death)):
                if bullets[i][0] > enx_pos[x] and bullets[i][0] < (enx_pos[x] + 20) and bullets[i][1] < (EY_pos + 20) and enemies_death[x] == False:
                    bullets[i][0] = -10
                    enemies_death[x] = True
                    print("hit")
                    score += 10
            
            

def draw():
    global x_pos
    global time
    global EX_pos
    global EY_pos
    global E_right
    global E_left
    global right_counter
    global left_counter
    global change
    global now
    global score
    global start_
    global enemies_death
    global bullets
    global bullets2
    global shooting_rate
    global Game_Over
    global start_timer
    global flash
    global Won
    global enx_pos
    #################################### ----   Start   Screen  ------ ############################################
    if start_:
        background(0, 0, 0)
        
        start_timer += 1
        
        if (start_timer + 60) % 90 == 0:
            flash = False
        elif start_timer % 90 == 0:
            flash = True
        
        fill(255, 255, 255)
        stroke(0, 255, 0)
        
        x = loadFont("MunroNarrow-48.vlw")
        textFont(x, 80)
        text("Space Invaders", 100, 200)
        textFont(x, 40)
        if flash:
            text("Insert Coin", 230, 300)
        
        ######################  If you press the down button it will reset the game
        if keyPressed and (keyCode == DOWN):
            x_pos = 90
            time = 0
            EX_pos = 20
            EY_pos = 180
            E_right = True
            E_left = False
            right_counter = 0
            left_counter = 0
            change = False
            now = True
            score = 0
            enemies_death = [False, False, False, False, False, False, False, False, False, False]
            enx_pos = [20, 70, 120, 170, 220, 270, 320, 370, 420, 470]
            start_ = False
            bullets = []
            bullets2 = []
            shooting_rate = 0
            Game_Over = False
            start_timer = 0
            flash = True
            Won = False
    #################################### ----   Win   Screen  ------ ############################################
    elif Won:
        background(0, 0, 0)
        
        fill(255, 255, 255)
        stroke(0, 255, 0)
        
        x = loadFont("MunroNarrow-48.vlw")
        textFont(x, 60)
        ###################### displays the contgratulation text and score
        text("Congratulations FAM!", 100, 200)
        textFont(x, 40)
        text("Score: " + str(score), 220, 300)
        
        ############# if you press the down button the the screen goes to the start screen 
        if keyPressed and (keyCode == DOWN):
            start_ = True
            Game_Over = False
            Won = False
            start_timer = 0
    
    #################################### ----   Game  Play  Screen  ------ ############################################
    elif start_ == False and Game_Over == False and Won == False:
        background(0, 0, 0)
        
        img = loadImage("shootet.png")
        shield = loadImage("shield.png")
        
        time += 1
        shooting_rate += 1
        fill(0, 255, 0)
        noStroke()
        
        ############# left and right button move player
        if keyPressed and (keyCode == LEFT):
            x_pos -= 10
        if keyPressed and (keyCode == RIGHT):
            x_pos += 10
        image(img, x_pos, 480)
        
        ############################# This creates the sheilds
        image(shield, 80, 400)
        image(shield, 210, 400)
        image(shield, 340, 400)
        image(shield, 470, 400)
        
        a = x_pos  + 15
        
        ################# This appends a x value and y value for the bullet
        if keyPressed and (keyCode == UP) and shooting_rate > 10:
            if a < 80 or a > 130 and a < 210 or a > 260 and a < 340 or a > 390 and a < 470 or a > 520:
                bullets.append([x_pos + 15, 480])
                shooting_rate = 0
            else:
                bullets2.append([x_pos + 15, 480])
                shooting_rate = 0
        
        ########################  This moves the enemy 8 times and move downs then left and repeat
        if time % 40 == 0:
            if change:                                                                      
                EY_pos += 20
                now = False
            if right_counter < 8 and E_right and E_left == False and left_counter == 0 and now:
                for i in range(len(enx_pos)):
                    enx_pos[i] += 10
                right_counter += 1
            if left_counter < 8 and E_left and E_right == False and right_counter == 0 and now:
                for i in range(len(enx_pos)):
                    enx_pos[i] -= 10
                left_counter += 1
            if change:
                now  = True
                change = False
            if right_counter == 8:
                right_counter = 0
                E_right = False
                E_left = True
                change = True
            if left_counter == 8:
                left_counter = 0
                E_right = True
                E_left = False
                change = True
        
        spawn_bullets(bullets)
        spawn_badbullets(bullets2)
        
        qw = loadImage("enemy.png")
        
        enemy_killer()
        
        ##################### This create the enemies if the enemy coresponding to the boolean in the enemies_death list is True
        for i in range(10):
            if enemies_death[i] == False:
                fill(255, 255, 255)
                image(qw, enx_pos[i], EY_pos)
        
        fill(255, 255, 255)
        
        font = loadFont("MunroNarrow-48.vlw")
        textFont(font, 30)
        text("Score: " + str(score), 40, 40)
        
        ################ ends the game and move to the win screen isf the score is 100
        if score == 100:
            Won = True
        
        ############## ends the if the enemies reaches the shield
        if EY_pos == 360:
            Game_Over = True
    
    #################################### ----   Game Over Screen  ------ ############################################
    else:
        background(0, 0, 0)
        
        fill(255, 255, 255)
        stroke(0, 255, 0)
        
        x = loadFont("MunroNarrow-48.vlw")
        textFont(x, 80)
        text("Game Over", 150, 200)
        textFont(x, 40)
        text("Score: " + str(score), 230, 300)
        
        ################ move to the start screen if you press down in game over screen
        if keyPressed and (keyCode == DOWN):
            start_ = True
            Game_Over = False
            start_timer = 0
            delay(100)