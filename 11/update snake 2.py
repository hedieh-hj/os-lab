import random
import arcade
import math


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
        self.body_size=0
        self.center_x=SCREEN_WIDTH//2  #position sar
        self.center_y=SECREEN_HEIGHT//2
        self.speed=2
        self.r=10
        self.change_x = 0  #dar rastay mehvar x taghirat nadare 0 , + be rast  , -khalaf x 
        self.change_y = 0 
        self.score = 1
        self.body = []  #mokhtasat ghatat badn mar zakhir mikonim 
        #self.body.append([self.center_x,self.center_y])      #makan hay dg badan mar mishe makan ghabli sar mar  (dar def eat save mishe ) 


      

    def draw(self):
        # arcade.draw_rectangle_filled(self.center_x,self.center_y,16,16,self.color)
        # for i in self.body:
        #     arcade.draw_rectangle_filled(i[0],i[1],16,16,self.color)

        for index, item in enumerate(self.body):  
            arcade.draw_circle_filled(item[0], item[1], self.r, self.color) #daqiqn dayere nemishe chon speed kam dadidm ->
                
    

         

    def move(self):

        for i in range(len(self.body)-1, 0, -1):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][1] = self.body[i-1][1]


        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y  


        if self.body:
            self.body[0][0] += self.speed * self.change_x
            self.body[0][1] += self.speed * self.change_y  

        #self.body.append([self.center_x,self.center_y]) #makan sar save mikone 

        # if len(self.body)> self.body_size:
        #     self.body.pop(0) #avalin khone ke az hame ghadimi tare bayd hazf beshe 


        # if self.change_x==-1:  #age dare chap mire 

        #     self.center_x -=self.speed

        # if self.change_x==1:  #age dare rast mire
        #     self.center_x +=self.speed

        # else:
        #      self.center_x +=0  #mishe hichi nanevisim 


        # if self.change_y==-1:  #age dare payin mire 
        #     self.center_y -=self.speed

        # if self.change_y==1:  #age dare bala mire
        #     self.center_y +=self.speed
            
        
            

    def eat(self):

        self.body.append([self.center_x,self.center_y])
        self.score += 1  
          
    
class Pear(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__("pear.png")
        self.width = 35
        self.height = 35       
        self.center_x = random.randint(20, w-20)  #fasele dar ba hashiye bashd
        self.center_y = random.randint(20, h-20)


class Apple(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__("apple.png")
        self.width = 35
        self.height = 35
        self.center_x = random.randint(20, w-20)  #position
        self.center_y = random.randint(20, h-20)      #fasele dar ba hashiye bashd


class Shit(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__("shit.png")
        self.width = 35
        self.height = 35
        self.center_x = random.randint(20, w-20)  #fasele dar ba hashiye bashd 
        self.center_y = random.randint(20, h-20)


class game(arcade.Window) : #ers bari shode az window arcade - vizhegi ha ro mikhaym

    def __init__(self):
        arcade.Window.__init__(self, SCREEN_WIDTH, SECREEN_HEIGHT, title='hediye\'s snake game') 
        arcade.set_background_color(arcade.color.RICH_LAVENDER)
        
        self.snake = snake(SCREEN_WIDTH, SECREEN_HEIGHT)  #object az snake 
        self.apple = Apple(SCREEN_WIDTH, SECREEN_HEIGHT)  #object az class ha 
        self.pear = Pear(SCREEN_WIDTH, SECREEN_HEIGHT)
        self.shit = Shit(SCREEN_WIDTH, SECREEN_HEIGHT)



    def on_draw(self): #rasm chizi dar safe bazi - masln emtiaz - chap snake 
        arcade.start_render()  # render mikone (graphic output)
        if self.snake.score >= 0 :  
            self.snake.draw()
            self.apple.draw()
            self.pear.draw()
            self.shit.draw()

            start_x = 10  #position score
            start_y = SCREEN_WIDTH - 30 #position score
        
            arcade.draw_text('Score : %i'%self.snake.score, start_x , start_y ,arcade.color.BLACK , DEFAULT_FONT_SIZE * 5, width=SCREEN_WIDTH, align='left')
            
        
        else: 
        #if self.snake.score <= 0 or self.snake.center_x<0 or self.snake.center_x>SCREEN_WIDTH or self.snake.center_y<0 or self.snake.center_y>SECREEN_HEIGHT:
            arcade.draw_text('Game Over',SCREEN_WIDTH//2, SECREEN_HEIGHT//2,arcade.color.BLACK, DEFAULT_FONT_SIZE * 5, width=SCREEN_WIDTH, align='left')
        


    def on_update(self, delta_time: float):  #tamam mantegh bazi dar in tabe neveshte mishavad

        # AI for moving snake logically
        X=0  
        Y=0

        # find position of apple and pear to move snake to them 
        if math.sqrt((self.snake.center_x-self.apple.center_x)**2+(self.snake.center_y-self.apple.center_y)**2) < math.sqrt((self.snake.center_x-self.pear.center_x)**2+(self.snake.center_y-self.pear.center_y)**2):
            X=self.apple.center_x
            Y=self.apple.center_y
        else :
            X=self.pear.center_x   
            Y=self.pear.center_y


        key_right=True
        key_left=True
        key_up=True
        key_down=True

        if self.snake.center_x<self.shit.center_x and self.snake.center_y==self.shit.center_y:
            key_right=False
        if self.snake.center_x>self.shit.center_x and self.snake.center_y==self.shit.center_y:
            key_left=False
        if self.snake.center_x==self.shit.center_x and self.snake.center_y<self.shit.center_y:
            key_up=False
        if self.snake.center_x==self.shit.center_x and self.snake.center_y>self.shit.center_y:
            key_down=False

        if  key_left and self.snake.center_x>X:
            self.snake.change_x = -1
            self.snake.change_y = 0
            self.snake.move()
            
        elif key_right and  self.snake.center_x <X:
            self.snake.change_x = 1
            self.snake.change_y = 0
            self.snake.move()

        elif key_up and self.snake.center_y < Y:
            self.snake.change_y = 1
            self.snake.change_x = 0
            self.snake.move()

        elif key_down and self.snake.center_y>Y:
            self.snake.change_y = -1
            self.snake.change_x = 0
            self.snake.move()


        if arcade.check_for_collision(self.snake,self.apple):
            self.apple = Apple(SCREEN_WIDTH, SECREEN_HEIGHT)
            self.snake.eat()  # +1 score 


        if arcade.check_for_collision(self.snake,self.pear):
            self.pear = Pear(SCREEN_WIDTH, SECREEN_HEIGHT)    
            self.snake.eat()  # +1 score 
            self.snake.eat()  # +1 score  = +2 for pear
    

play_game=game()   # darim shey misazim va init call mikone - tabe window ke parent hast call nemishe 
arcade.run() #loop infinty baray stop nashodn 