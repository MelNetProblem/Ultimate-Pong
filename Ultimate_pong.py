from pygame import *
window=display.set_mode((700,500))
window.fill((9,1,3))
fps = 144
clock=time.Clock()
game= True

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
            self.rect.y -= speed
        if keys_pressed[K_s] and self.rect.y<405:
            self.rect.y += speed 
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >5:
            self.rect.y -= speed
        if keys_pressed[K_DOWN] and self.rect.y<405:
            self.rect.y += speed 
class Enemy(GameSprite):
    def update(self):
        global lose
        self.rect.y+=self.speed
        if self.rect.y>500:
            self.rect.y = 0
            self.rect.x = randint(100,600)
            lose+=1

#aggy birsds


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(fps)
    display.update()









