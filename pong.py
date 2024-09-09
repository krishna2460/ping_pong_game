import pygame,sys,random
def ballmove():
    from pygame import gfxdraw
    
    global ballx,bally,o_score,p_score,player,user
    ball.x += ballx
    ball.y += bally
    if ball.top <=0 or ball.bottom >=height:
        bally *= -1
    if ball.right >= width or ball.left <=0 :
        if ball.right >= width:
            o_score +=1
            
        if ball.left<=0:
            p_score +=1
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(opp):
        ballx *= -1
def player_animation():
    player.y += p_speed
    if player.top <=0:
        player.top = 0
    if player.bottom>= height:
        player.bottom = height
def ball_restart():
    global ballx,bally
    ball.center = (width/2,height/2) 
    ballx *=0
    bally *=0
    opp.center =(10,height/2)
    player.center = (width-5,height/2)
# ttext variables:-
p_score = 0
o_score = 0
pygame.init()
game_font = pygame.font.Font("freesansbold.ttf",32)

width = 1024
height = 700
screen= pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
ball = pygame.Rect(width/2-15,height/2-15,30,30)
player = pygame.Rect(width-20,height/2 -100,10,140)
opp = pygame.Rect(10,height/2-100,10,180)
bg = pygame.Color("grey12")
light_grey = pygame.Color(200,200,200)
ballx=0
bally=0
p_speed = 0
o_speed = 10
a=10
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                p_speed+=a
                
            if event.key == pygame.K_UP:
                p_speed-=a
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                p_speed-=a
            if event.key == pygame.K_UP:
                p_speed+=a    
        if ballx ==0 and bally==0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    ballx=7*random.choice((1,-1))
                    bally=7*random.choice((1,-1))
                   
                    
                if event.key == pygame.K_UP:
                    ballx=7*random.choice((1,-1))
                    bally=7*random.choice((1,-1))
                    
                    
                    

    ballmove()
    player_animation()
    if(ball.x<width/2):
        if opp.top <=ball.y:
            opp.top += o_speed
        if opp.bottom >= ball.y:
            opp.bottom -= o_speed
            
    
    if opp.top <=0:
        opp.top =0
    if opp.bottom >= height:
        opp.bottom = height
    #visible
    screen.fill(bg)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opp)
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.aaline(screen,light_grey,(width/2,0),(width/2,height))
    player_text = game_font.render(f"{p_score}",False,light_grey)
    screen.blit(player_text,(640,height/2))
    opp_text = game_font.render(f"{o_score}",False,light_grey)
    screen.blit(opp_text,(320,height/2))
    pygame.display.flip()
    clock.tick(75)
