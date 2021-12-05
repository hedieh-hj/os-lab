import random
import arcade


# https://github.com/pythonarcade/arcade

SCREEN_WIDTH=500
SECREEN_HEIGHT=500
DEFAULT_FONT_SIZE =4 

class snake(arcade.Sprite) :  #mojodiat hay dakhel game 

    def __init__(self,w,h) -> None:
        super().__init__()  #def parent

        self.width=16
        self.height=16
        self.color=arcade.color.RICH_BLACK
        self.body=0
        self.center_x=SCREEN_WIDTH//2  #position sar
        self.center_y=SECREEN_HEIGHT//2
        self.speed=2
        self.r=10
        self.change_x = 0
        self.change_y = 0
        self.score = 1
        self.body = []
        self.body.append([self.center_x,self.center_y])       


    # def display(self): #draw             #andaze khod snake                h w sanke        rang snake
    #     arcade.draw_rectangle_filled(self.center_x , self.center_y,self.width,self.height,self.color)

    def draw(self):
        for index, item in enumerate(self.body):
             arcade.draw_circle_filled(item[0], item[1], self.r, self.color)
         

    def move(self):

        for i in range(len(self.body)-1, 0, -1):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][1] = self.body[i-1][1]

        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y

        if self.body:
            self.body[0][0] += self.speed * self.change_x
            self.body[0][1] += self.speed * self.change_y
            

    def eat(self, food):

        if  food == 'apple':
            self.score += 1
            self.body.append([self.body[len(self.body)-1][0], self.body[len(self.body)-1][1]])

        elif food == 'pear':
            self.score += 2
            self.body.append([self.body[len(self.body)-1][0], self.body[len(self.body)-1][1]])
            self.body.append([self.body[len(self.body)-1][0], self.body[len(self.body)-1][1]])

        elif food == 'shit':
            self.score -=1    
            #self.body=([self.body[len(self.body)-1][0]-1, self.body[len(self.body)-1][1]-1]) 
            self.body.pop()  #remove last item of list !
            
            
            
    
class Pear(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.image = 'pear.png'
        self.pear = arcade.Sprite(self.image, 0.05) #size
        self.pear.center_x = random.randint(20, w-20)  #fasele dar ba hashiye bashd
        self.pear.center_y = random.randint(20, h-20)

    def draw(self):
        self.pear.draw()

class Apple(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.image = 'apple.png'  #add image apple
        self.apple = arcade.Sprite(self.image, 0.08)    #size
        self.apple.center_x = random.randint(20, w-20)  #position
        self.apple.center_y = random.randint(20, h-20)      #fasele dar ba hashiye bashd

    def draw(self):
        self.apple.draw()

class Shit(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.image = 'shit.png'
        self.shit = arcade.Sprite(self.image, 0.05)     #size
        self.shit.center_x = random.randint(20, w-20)  #fasele dar ba hashiye bashd 
        self.shit.center_y = random.randint(20, h-20)

    def draw(self):
        self.shit.draw()

class game(arcade.Window) : #ers bari shode az window arcade - vizhegi ha ro mikhaym

    def __init__(self) -> None:
        super().__init__(width=SCREEN_WIDTH,height=SECREEN_HEIGHT,title='hediye\'s snake game',resizable=True)  #tabe sazande kelas ers borde shode window ham bayd seda bezane = init valed ejra mishe 
        arcade.set_background_color(arcade.color.RICH_LAVENDER)
        
        self.snake = snake(SCREEN_WIDTH, SECREEN_HEIGHT)  #object az snake 
        self.apple = Apple(SCREEN_WIDTH, SECREEN_HEIGHT)  #object az class ha 
        self.pear = Pear(SCREEN_WIDTH, SECREEN_HEIGHT)
        self.shit = Shit(SCREEN_WIDTH, SECREEN_HEIGHT)



    def on_draw(self): #rasm chizi dar safe bazi - masln emtiaz - chap snake 
        arcade.start_render()  #inja dare rangi mikone - render mikone (graphic output)
        self.snake.draw()
        self.snake.draw()
        self.apple.draw()
        self.pear.draw()
        self.shit.draw()

        start_x = 10  #position score
        start_y = SCREEN_WIDTH - 30 #position score
        
        arcade.draw_text('Score : %i'%self.snake.score, start_x , start_y ,arcade.color.BLACK , DEFAULT_FONT_SIZE * 5, width=SCREEN_WIDTH, align='left')
        
        
        if self.snake.score <= 0 or self.snake.center_x<0 or self.snake.center_x>SCREEN_WIDTH or self.snake.center_y<0 or self.snake.center_y>SECREEN_HEIGHT:
            arcade.draw_text('Game Over',SCREEN_WIDTH//2, SECREEN_HEIGHT//2,arcade.color.BLACK, DEFAULT_FONT_SIZE * 5, width=SCREEN_WIDTH, align='left')
            arcade.exit()                   #vasat safe chap kone 


    def on_update(self, delta_time: float):

        self.snake.move()

        if arcade.check_for_collision(self.snake, self.apple.apple):
            self.snake.eat('apple')
            self.apple = Apple(SCREEN_WIDTH, SECREEN_HEIGHT)

        if arcade.check_for_collision(self.snake, self.pear.pear):
            self.snake.eat('pear')
            self.pear = Pear(SCREEN_WIDTH, SECREEN_HEIGHT)
    
        if arcade.check_for_collision(self.snake,self.shit.shit):
            self.snake.eat('shit')
            self.sit = Shit(SCREEN_WIDTH, SECREEN_HEIGHT)


    def on_key_release(self, key, modifiers):
        
        if key == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
            # self.snake.center_y +=self.snake.speed
        
        elif key == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
            # self.snake.center_y -=self.snake.speed
        
        elif key == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
            # self.snake.center_x -=self.snake.speed
        
        elif key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
            # self.snake.center_x +=self.snake.speed


    

play_game=game()   # darim shey misazim va init call mikone - tabe window ke parent hast call nemishe 
arcade.run() #loop infinty baray stop nashodn 