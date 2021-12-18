import time
import arcade
import math
import random


FONT_SIZE = 50


class Enemy(arcade.Sprite):

    def __init__(self, w, h ,speed=3):
        super().__init__(':resources:images/space_shooter/playerShip1_green.png')
        self.speed = speed
        self.center_x = random.randint(0, w)
        self.center_y = h+10  #inja az kharej safe vared mishe
        self.angle = 180
        self.width = 50
        self.height = 50
    def hit(self):
        arcade.play_sound(arcade.sound.Sound(':resources:sounds/hit3.wav'), 1.0, 0.0,False)
    def move(self):
        self.center_y -= self.speed  #az bala mire payin 


class Bullet(arcade.Sprite):
    def __init__(self, host):  #host spacei ke shelik mikone hast 
        super().__init__(':resources:images/space_shooter/laserRed01.png')
        self.speed = 4
        self.angle = host.angle
        self.center_x = host.center_x
        self.center_y = host.center_y
    
    def lunch(self):
        arcade.play_sound(arcade.sound.Sound(':resources:sounds/laser5.wav'), 0.2, 0.0,False)
    
    def move(self):
        angle_radious = math.radians(self.angle)
        self.center_x -= self.speed * math.sin(angle_radious)
        self.center_y += self.speed * math.cos(angle_radious)




class Spacecraft(arcade.Sprite):
    
    def __init__(self, w, h):
        super().__init__(':resources:images/space_shooter/playerShip3_orange.png')
        self.width = 48
        self.height = 48
        self.center_x = w//2 #in taghir nemikone (spacecraft sabet)
        self.center_y = 48
        self.change_x = 0
        self.change_y = 0
        self.angle = 0 #zavie avalie
        self.change_angle = 0
        self.bullet_list = []
        self.speed = 6
        self.score = 0 #score kaheshi mishe bashe
        self.health = 3
    
    def rotate(self):
        self.angle += self.change_angle * self.speed
    
    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
    
    def fire(self):
        self.bullet_list.append(Bullet(self))  #khodesh mizban hamin tir hast 



        
class Game(arcade.Window):
    
    def __init__(self):
        self.w = 600
        self.h = 700
        super().__init__(self.w, self.h, title=" Spacecraft\s  Hediye")
        self.background_image = arcade.load_texture('background.jpg')
        self.me = Spacecraft(self.w, self.h)
        self.enemy = Enemy(self.w, self.h)
        self.next_enemy_time = random.randint(2, 5)

         #2
        self.enemy_list = []
        self.game_start_time = time.time()

        #3
        self.start_time = time.time()
        self.health_image = arcade.load_texture('rh.png')
    
    
    def on_draw(self):
        arcade.start_render()
        if self.me.health<=0:
            arcade.draw_text('GAME OVER :(', self.w//2-200, self.h//2, arcade.color.WHITE, FONT_SIZE //2, width=400, align='center')
        else:
            arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.background_image)  #payin chap x va y - tool arz #teture aksi ke mikhaym - lrwh left right width high
            self.me.draw()
            for i in range(len(self.me.bullet_list)):
                self.me.bullet_list[i].draw()
            for i in range(len(self.enemy_list)):
                self.enemy_list[i].draw()
            for i in range(self.me.health):
                arcade.draw_lrwh_rectangle_textured(10+i*35 ,10 ,30 ,30 ,self.health_image)
            arcade.draw_text('Score: %i'%self.me.score, self.w-130, 10, arcade.color.WHITE, FONT_SIZE //2, width=200, align='left')
    
    
    def on_update(self, delta_time):  #upate va taghirat bazi dar inja 
        self.end_time = time.time()

        if self.end_time - self.start_time > self.next_enemy_time:
            self.next_enemy_time = random.randint(2, 6)
            self.enemy_list.append(Enemy(self.w, self.h, 3+(self.end_time-self.game_start_time)//24))
            self.start_time = time.time()

        self.me.rotate()
        self.me.move()

        for i in range(len(self.me.bullet_list)):
            self.me.bullet_list[i].move()

        for i in range(len(self.enemy_list)):
            self.enemy_list[i].move()

        for enemy in self.enemy_list:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(bullet, enemy):
                    enemy.hit()
                    self.me.bullet_list.remove(bullet)
                    self.enemy_list.remove(enemy)
                    self.me.score += 1


        for enemy in self.enemy_list:
            if enemy.center_y < 0:
                self.me.health -= 1
                self.enemy_list.remove(enemy)

        for bullet in self.me.bullet_list:
            if bullet.center_y>self.height or bullet.center_x<0 or bullet.center_x>self.width:
                self.me.bullet_list.remove(bullet)
    
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.me.change_y = 1
        elif key == arcade.key.DOWN:
            self.me.change_y = -1
        elif key == arcade.key.RIGHT:
            self.me.change_x = 1
        elif key == arcade.key.LEFT:
            self.me.change_x = -1
        elif key == arcade.key.C:
            self.me.change_angle = 1
        elif key == arcade.key.V:
            self.me.change_angle = -1
        elif key == arcade.key.SPACE:
            self.me.fire()
            self.me.bullet_list[-1].lunch()
    
    
    def on_key_release(self, key, modifiers):
        self.me.change_angle = 0
        self.me.change_x = 0
        self.me.change_y = 0

Game()
arcade.run()