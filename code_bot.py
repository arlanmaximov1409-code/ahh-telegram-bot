@bot.message_handler(commands=['cmd'])
def send_keys(message):
    keyboard = ReplyKeyboardMarkup()
    keyboard.add(KeyboardButton('кнопка 1'), KeyboardButton('кнопка 2'), KeyboardButton('sup'), KeyboardButton('what are you?'))
    bot.send_message(message.chat.id, 'привет!', reply_markup=keyboard)



# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

# Обработчик команды '/heh'
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
    if message.text == 'кнопка 1':
        bot.send_message(message.chat.id, 'вы нажали кнопку 1')
    elif message.text == 'кнопка 2':
        bot.send_message(message.chat.id, 'вы нажали кнопку 2')
    elif message.text == 'sup':
        bot.send_message(message.chat.id, 'вы нажали кнопку 2')
    elif message.text == 'what are you?':
        bot.send_message(message.chat.id, 'SUp')

bot.polling()
