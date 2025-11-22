from config import TOKEN
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import telebot


bot = telebot.TeleBot(your bot token)

@bot.message_handler(commands=['cmd'])
def send_keys(message):
    keyboard = ReplyKeyboardMarkup()
    keyboard.add(KeyboardButton('button 1'), KeyboardButton('button 2'), KeyboardButton('sup'), KeyboardButton('what are you?'))
    bot.send_message(message.chat.id, 'привет!', reply_markup=keyboard)



keys = ["1","2","3","4","5","6","7","8","9","0","q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
symbols = ["1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","\'","\"","/","\\",",",".",";",":"]

def keyboard(key_type="Normal"):
    markup = ReplyKeyboardMarkup(row_width=10)
    if key_type == "Normal":
        row = [KeyboardButton(x) for x in keys[:10]]
        markup.add(*row)
        row = [KeyboardButton(x) for x in keys[10:20]]
        markup.add(*row)
        row = [KeyboardButton(x) for x in keys[20:29]]
        markup.add(*row)
        row = [KeyboardButton(x) for x in keys[29:]]
        markup.add(*row)
        markup.add(KeyboardButton("Caps Lock"),KeyboardButton("Symbols"),KeyboardButton("🔙Delete"),KeyboardButton("✅Done"))
    elif key_type == "Symbols":
        row = [KeyboardButton(x) for x in symbols[:10]]
        markup.add(*row)
        row = [KeyboardButton(x) for x in symbols[10:20]]
        markup.add(*row)
        row = [KeyboardButton(x) for x in symbols[20:]]
        markup.add(*row)
        markup.add(KeyboardButton("Caps Lock"),KeyboardButton("Normal"),KeyboardButton("🔙Delete"),KeyboardButton("✅Done"))
    else:
        row = [KeyboardButton(x.upper()) for x in keys[:10]]
        markup.add(*row)
        row = [KeyboardButton(x.upper()) for x in keys[10:20]]
        markup.add(*row)
        row = [KeyboardButton(x.upper()) for x in keys[20:29]]
        markup.add(*row)
        row = [KeyboardButton(x.upper()) for x in keys[29:]]
        markup.add(*row)
        markup.add(KeyboardButton("Normal"),KeyboardButton("Symbols"),KeyboardButton("🔙Delete"),KeyboardButton("✅Done"))
    return markup

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id,"You can use the keyboard",reply_markup=keyboard())

@bot.message_handler(func=lambda message:True)
def all_messages(message):
    if message.text == "✅Done":
        markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id,"Done with Keyboard",reply_markup=markup)
    elif message.text == "Symbols":
        bot.send_message(message.from_user.id,"Special characters",reply_markup=keyboard("Symbols"))
    elif message.text == "Normal":
        bot.send_message(message.from_user.id,"Normal Keyboard",reply_markup=keyboard("Normal"))
    elif message.text == "Caps Lock":
        bot.send_message(message.from_user.id,"Caps Lock",reply_markup=keyboard("Caps"))
    elif message.text == "🔙Delete":
        bot.delete_message(message.from_user.id,message.message_id)
    else:
        bot.send_message(message.chat.id,message.text)


# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=['commands'])
def avail_commands(message):
    bot.send_message(message.chat.id, 'all available commands- /start, /hello, /heh, /poll, /cmd, /commands, /poll2')

@bot.message_handler(commands=["poll"])
def create_poll(message):
    bot.send_message(message.chat.id, "HARDEST MATH TEST THAT EVEN ALBERT EINSTEIN CANT SOLVE")
    answer_options = ["1", "2", "5", "67", '4', 'i dont know :(']

    bot.send_poll(
        chat_id=message.chat.id,
        question="2+2 = ?",
        options=answer_options,
        type="quiz",
        correct_option_id=4,
        is_anonymous=False,
    )

@bot.message_handler(commands=['poll2'])
def poller(message):
    bot.send_message(message.chat.id, 'please answer this poll')
    options = ['😊', '❤️', '🤣', '👍']

    bot.send_poll(
        chat_id=message.chat.id,
        question='your favorite emoji?',
        options=options,
        type='regular',
        is_anonymous=False,
    )

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'кнопка 1':
        bot.send_message(message.chat.id, 'you pressed button 1')
    elif message.text == 'кнопка 2':
        bot.send_message(message.chat.id, 'you pressed button 2')
    elif message.text == 'sup':
        bot.send_message(message.chat.id, 'Hello how are you')
    elif message.text == 'what are you?':
        bot.send_message(message.chat.id, 'Sup i am testing bot with some features and buttons')

bot.polling()
