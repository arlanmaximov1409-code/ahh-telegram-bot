@bot.message_handler(commands=['cmd'])
def send_keys(message):
    keyboard = ReplyKeyboardMarkup()
    keyboard.add(KeyboardButton('button 1'), KeyboardButton('button 2'), KeyboardButton('sup'), KeyboardButton('what are you?'))
    bot.send_message(message.chat.id, 'Hello , buttons created!', reply_markup=keyboard)



#command /start, /hello handler
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Hello im am {bot.get_me().first_name}!')

# command /heh handler , laughing one)
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

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
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'button 1':
        bot.send_message(message.chat.id, 'Button 1 is pressed')
    elif message.text == 'button 2':
        bot.send_message(message.chat.id, 'Button 1 is pressed')
    elif message.text == 'sup':
        bot.send_message(message.chat.id, 'Hello , how are you?')
    elif message.text == 'what are you?':
        bot.send_message(message.chat.id, 'I am testing bot ')

bot.polling()
