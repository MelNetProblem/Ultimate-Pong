from pygame import *
window=display.set_mode((700,500))
window.fill((9,1,3))
display.set_caption("Ultimate Pong")
fps = 144
clock=time.Clock()
game= True
speed_x = 4
speed_y = 4
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y<405:
            self.rect.y += self.speed 
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y<405:
            self.rect.y += self.speed 
class Enemy(GameSprite):
    def update(self):
        global lose
        self.rect.y+=self.speed
        if self.rect.y>500:
            self.rect.y = 0
            self.rect.x = randint(100,600)
            lose+=1
platform_l= Player("dsad.png",20,200,70,70,10)
platform_r= Player("tako.png",610,200,70,70,10)
ball = GameSprite("balls.png",250,300,35,35,0)

font1 = font.Font
#aggy birsds


while game:
    window.fill((9,1,3))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if ball.rect.y > 470 or ball.rect.y < 10:
        speed_y *= -1
    if sprite.collide_rect(platform_l,ball) or sprite.collide_rect(platform_r,ball):
        speed_x *= -1
    clock.tick(fps)
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    platform_l.reset()
    platform_r.reset()
    ball.reset()
    platform_l.update_l()
    platform_r.update_r()
    display.update()    






