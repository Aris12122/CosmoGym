import telebot

bot = telebot.TeleBot("5389276277:AAHdRYTpXvqTGin9P1f-9FE0zAQ2pYWoZlY")
# CF_handle = ""

# @bot.message_handler(commands=["start"])
# def start(message):
#     bot.send_message(message.chat.id, "Привет! Отправь мне свой хендл с Codeforces, чтобы я мог тебя опознать")

# @bot.message_handler(commands=["token"])
# def get_token(message):
#     bot.send_message(message.chat.id, message.text)


# def valid_handle(handle):
#     return handle == "Aris" or handle == "myav"

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, message.text)
    # global CF_handle

    # bot.send_message(message.chat.id, "Проверка " + message.text)
    # if valid_handle(message.text) == False:
    #     bot.send_message(message.chat.id, "Пожалуйста, проверь, что хендл верный. Ты ввел: " + message.text)
    #     return
    # if CF_handle == "":
    #     CF_handle = message.text
    #     bot.send_message(message.chat.id, "Отлично, " + message.text + ". Я записал твой хендл, теперь ты можешь запрашивать у меня токен после решения задачи)")
    #     return
    # elif CF_handle != "":
    #     bot.send_message(message.chat.id, "Ты уже вводил свой хендл с Codeforces, если ты действительно хочешь поменять его на новый, напиши @Aris12122 в телеграмм")
    #     return
    # bot.send_message(message.chat.id, "Некорректное состояние! Пожалуйста, напишите @Aris12122 в телеграмм со скриншотом своих последних сообщений боту")




bot.polling(non_stop=True)
