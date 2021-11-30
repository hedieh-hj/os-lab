import telebot
import random
import qrcode
import datetime
import gtts




#https://github.com/eternnoir/pyTelegramBotAPI#readme = help
# id bot = Hedi_gift_Bot
bot = telebot.TeleBot("2103138353:AAEqFNS-wzGYKoh3pLn_hoafLu_eIxCQYog") #token


#################################################################################

@bot.message_handler(commands=['help'])
def help_func(message):

    bot.reply_to(message,
                 """
                 /start - welcome to my bot
/game -guess the number 🎮
/age - calculate your age 
/voice - convert text to voice 🎼
/max - find biggest number 
/argmax - find index of biggest number 
/qrcode - make Qrcode  
/help - menu""" )


#################################################################################

@bot.message_handler(commands=['start'])
def start_func(message):
    bot.send_message(message.chat.id, 'Welcome ' + (message.chat.first_name) + '!')

#################################################################################

random_num = random.randint(0, 99)

def new_randomNumber():
    global random_num
    random_num = random.randint(0, 99)

@bot.message_handler(commands=['game'])
def game_func(message):
    text = bot.send_message(message.chat.id, 'I will help you number is between 0 to 100 😉\nGuess the number ?!😈')
    bot.register_next_step_handler(text, game_play)



def game_play(text):
    test = telebot.types.ReplyKeyboardMarkup(row_width=1)
    btn1 = telebot.types.KeyboardButton('New Game')
    test.add(btn1)
    if not m.text.startswith("/"):
        try:
            if text.text == 'New Game':
                new_randomNumber()
                bot.send_message(text.chat.id, 'NEW Game begin. Guess new number:',
                                 reply_test=telebot.types.ReplyKeyboardRemove(selective=True))

                bot.register_next_step_handler_by_chat_id(text.chat.id, game_play)

            elif int(text.text) < random_num:
                text = bot.send_message(text.chat.id, 'bigger', reply_test=test)
                bot.register_next_step_handler(text, game_play)

            elif int(text.text) > random_num:
                text = bot.send_message(text.chat.id, 'lower', reply_test=test)
                bot.register_next_step_handler(text, game_play)

            elif int(text.text) == random_num:
                text = bot.send_message(text.chat.id, 'It\'s true. 👏🏻' , reply_test=telebot.types.ReplyKeyboardRemove(selective=True))

        except ValueError:
            bot.send_message(text.chat.id, 'you write a wrong input , try again!',
                             reply_test=telebot.types.ReplyKeyboardRemove(selective=True))
    else:
        bot.reply_to(text, 'I expect a number not a command. \nstart again -> write command !')
        
#################################################################################

@bot.message_handler(commands=['age'])
def age_func(m):
    message = bot.send_message(m.chat.id, 'write your birthday date (e.g. 1400/8/10)')
    bot.register_next_step_handler(message, age_play)

def age_play(m):

    bot.send_message(m.chat.id, "Loading..." )

    x = datetime.datetime.now()
    global gy
    gy=x.year
    global gm
    gm=x.month
    global gd
    gd=x.day

    yy,mm,dd = m.text.split("/")
    #bot.send_message(m.chat.id, "Loading3..."+yy+mm+dd )
    
    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    if (gm > 2):
        gy2 = gy + 1

    else:
        gy2 = gy

    days = 355666 + (365 * gy) + ((gy2 + 3) // 4) - ((gy2 + 99) // 100) + ((gy2 + 399) // 400) + gd + g_d_m[gm - 1]
    jy = -1595 + (33 * (days // 12053))
    days %= 12053
    jy += 4 * (days // 1461)
    days %= 1461

    if (days > 365):
        jy += (days - 1) // 365
        days = (days - 1) % 365
    if (days < 186):
        jm = 1 + (days // 31)
        jd = 1 + (days % 31)
    else:
        jm = 7 + ((days - 186) // 30)
        jd = 1 + ((days - 186) % 30)
    
    #print(jy,jm,jd)
    yy=int(yy)
    mm=int(mm) 
    dd=int(dd)
    
    if(jd < dd):
        jm-=1
        jd+=30
            
    if(jm < mm):
        jm += 12
        jy -= 1
    """
    if (jd < dd):
        dd=dd-jd
    else:
        dd = jd - dd
    """
    
    yy = jy - yy
    mm = jm - mm
    dd = jd - dd
    
    #bot.send_message(m.chat.id, "Loading5..." )

    if yy>=1:
        h=yy*362*24
        min=h*60
        sec=min*60
    else :
        if mm>=1:
            h=mm*7*24
            min=h*60
            sec=min*60
        else:
            h=dd*24
            min=h*60
            sec=min*60 

    bot.send_message(m.chat.id, "You are  " +str(yy) +" years  "+ str(mm) +" month "+ str(dd)+" days " )
    
#################################################################################

@bot.message_handler(commands=['voice'])
def voice_func(m):
    message = bot.send_message(m.chat.id, 'write your text (e.g. hi my name is hediye)')
    bot.register_next_step_handler(message, voice_play)


def voice_play(m):
    if not m.text.startswith('/'):
        try:
            vc = gtts.gTTS(text=m.text)
            vc.save('test.ogg')
            voice = open('test.ogg','rb')
            bot.send_voice(m.chat.id, voice)
        except:
            bot.send_message(m.chat.id, 'you write a illegal input')
    else:
        bot.reply_to(m, 'I expect a text not a command. \nstart again -> write command !')
        
#################################################################################

@bot.message_handler(commands=['max'])
def max_func(m):
    message = bot.send_message(m.chat.id, 'write your numbers  with ,  (e.g. 1,22,10,5,3)')
    bot.register_next_step_handler(message, max_play)


def max_play(m):
    if not m.text.startswith('/'):
        try:
            numbers = list(map(int, m.text.split(',')))
            bot.send_message(m.chat.id, 'biggest number: ' + str(max(numbers)))
        except:
            bot.send_message(m.chat.id, 'you write a illegal input')
    else:
        bot.reply_to(m, 'I expect a number not a command. \nstart again -> write command !')

#################################################################################       

@bot.message_handler(commands=['argmax'])
def argmax_welcome(m):
    message = bot.send_message(m.chat.id, 'write your numbers  with ,  (e.g. 1,22,10,5,3)')
    bot.register_next_step_handler(message, argmax_play)


def argmax_play(m):
    if not m.text.startswith('/'):
        try:
            numbers = list(map(int, m.text.split(',')))
            bot.send_message(m.chat.id, 'biggest number index: ' + str(numbers.index(max(numbers))))
        except:
            bot.send_message(m.chat.id, 'you write a illegal input')
    else:
        bot.reply_to(m, 'I expect a number not a command. \nstart again -> write command !')

################################################################################# 

@bot.message_handler(commands=['qrcode'])
def qrcode_func(m):
    message = bot.send_message(m.chat.id, 'write your text' )
    bot.register_next_step_handler(message, qr_play)


def qr_play(m):
    if not m.text.startswith('/'):
        try:
            img = qrcode.make(m.text)
            img.save('QRCODE.png')
            photo = open('QRCODE.png', 'rb')
            bot.send_photo(m.chat.id, photo)
        except:
            bot.send_message(m.chat.id, 'you write a illegal input')
    else:
        bot.reply_to(m, 'I expect a text not a command. \nstart again -> write command !')
        


bot.infinity_polling()  # == bot.polling(none_stop=True) 

  
