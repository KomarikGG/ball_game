from pygame import *
class Game_sprite(sprite.Sprite):
    def __init__(self, image_file, location, size,speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(image_file), size)
        self.rect = self.image.get_rect()
        self.rect.topleft = location
        self.x_speed = speed
        self.y_speed = speed
    def reset(self):
        window.blit(self.image,self.rect.topleft)
class Player(Game_sprite):
    def update_r(self): 
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.y_speed
        if keys[K_DOWN] and self.rect.bottom < win_height:
            self.rect.y += self.y_speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.y_speed
        if keys[K_s] and self.rect.bottom < win_height:
            self.rect.y += self.y_speed
back = (200,255,255)

player_1 = Player('racket.png', (30, 200), (50, 150), 4)
player_2 = Player('racket.png', (720, 200), (50, 150), 4)
ball = Game_sprite('tennis_ball.png',(200,200), (50, 50),4)
font.init()

font_style = font.SysFont('arial', 25)
lose1 = font_style.render('player_1.lost',True,'black')
lose2 = font_style.render('player_2.lost',True,'black')

win_width = 800
win_height = 600
window = display.set_mode((win_width, win_height))
display.set_icon(image.load('tennis_ball.png'))
finished = False
running = True
fps = 60

clock = time.Clock()
while running == True:
    for i in event.get():
        if i.type == QUIT:
            running = False
    if finished == False:
        window.fill(back)
        player_1.update_l()
        player_2.update_r()
        player_1.reset()
        player_2.reset()
        ball.reset()
        ball.rect.x += ball.x_speed
        ball.rect.y += ball.y_speed
        if ball.rect.x < 0 or ball.rect.x > win_width:
            ball.x_speed = -ball.x_speed
        if ball.rect.y < 0 or ball.rect.bottom > win_height:
            ball.y_speed = -ball.y_speed
        if player_1.rect.colliderect(ball.rect):
            ball.x_speed = -ball.x_speed
        if player_2.rect.colliderect(ball.rect):
            ball.x_speed = -ball.x_speed
        if ball.rect.x < player_1.rect.x:
            finished = True
            window.blit(lose1, (300, 200))
        if ball.rect.x > player_2.rect.x:
            finished = True
            window.blit(lose2, (300, 200))
        display.update()
        clock.tick(fps)

