import telebot

# Replace 'YOUR_BOT_TOKEN' with the actual token of your bot
bot = telebot.TeleBot('6549292499:AAHacZBWyJ8p2ZAmdZj94II941lF638UV7Q')

# Replace USER_ID with the target user ID
USER_ID = 922758956

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Hello! This is your bot.")

# Send a message to the specified user ID
def send_message_to_user(txt):
    USER_ID = 922758956
    bot.send_message(USER_ID, txt)

# Schedule sending a message to the user
# bot.send_message(USER_ID, "Hello! This is a message from your bot.")

# Start the bot
# bot.polling()
