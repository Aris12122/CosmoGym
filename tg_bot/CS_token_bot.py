from curses.ascii import isalpha
import telebot
from users_data import Users_data
import CF
import ans_token


udata = Users_data()

token_format_message = "Пожалуйста, убедитесь, что вы правильно вводите команду: x Y\nГде x - номер контеста, Y - буква, соответствующая задаче\n"

links = {   
    'stepik_course':    "",
    'codeforces_group': "",
    'register':         "https://forms.gle/89DsZeegTJ46XpXPA"
}

contests = {
    1: "G",
    2: "H",
}

def get_file(path):
    with open(path) as f:
        return f.readline()

def add_to_file(path, mess):
    with open(path, 'a') as f:
        f.write(" " + mess)


bot = telebot.TeleBot(get_file("secret/botAPI"))

cached_users = set()


@bot.message_handler(commands=["start"])
def start(message):
    if udata.is_user_registered(message.from_user.username):
        bot.send_message(message.chat.id, "Приветствую вас на нашем курсе! Всю необходимую информацию вы можете посмотреть здесь:\n" + links["stepik_course"])
    else:
        bot.send_message(message.chat.id, "Привет! Вижу вы ещё не зарегистрировались на курс. Для продолжения, пожалуйста, заполни форму по ссылке:\n" + links["register"])


def reply_token(message, contest_id, problem_id):
    print("reply")

    tg_handle = message.from_user.username
    cf_handle = udata.get_cf_handle_by_tg(tg_handle)



    bot.send_message(message.chat.id, "Проверка...")

    if check_registered(cf_handle=cf_handle, tg_handle=tg_handle, message=message) == False:
        return

    if len(problem_id) != 1:
        bot.send_message(message.chat.id, token_format_message + "Название задачи должен быть одной буквой\n")
        return

    if isalpha(problem_id[0]) == False:
        bot.send_message(message.chat.id, token_format_message + "Название задачи должен быть буквой\n")
        return

    if contest_id.isnumeric() == False:
        bot.send_message(message.chat.id, token_format_message + "Ваш номер контеста не является числом\n")
        return

    contest_id = int(contest_id)

    print(contest_id, problem_id)

    if contest_id > len(contests):
        bot.send_message(message.chat.id, token_format_message + "Контеста с таким номером не существует\n")
        return

    if problem_id[0] > contests[contest_id]:
        bot.send_message(message.chat.id, token_format_message + "В этом контесте нет задачи с таким названием\n")
        return

    

    if CF.is_solved(contest_id=contest_id, problem_id=problem_id, handle=cf_handle):
        bot.send_message(message.chat.id, ans_token.get_token(contest_id, problem_id, cf_handle))
    else:
        bot.send_message(message.chat.id, "Вы пока не решили эту задачу, попробуйте позже")
    


@bot.message_handler(commands=["token"])
def get_token(message):

    txt = message.text.split(' ')

    if len(txt) > 3:
        bot.send_message(message.chat.id, token_format_message + "Ваше сообщение содержит более двух аргументов\n")
        return
    if len(txt) < 3:
        bot.send_message(message.chat.id, token_format_message + "Ваше сообщение содержит менее двух аргументов\n")
        return
    
    contest_id = txt[1]
    problem_id = txt[2]

    reply_token(message=message, contest_id=contest_id, problem_id=problem_id)

    


@bot.message_handler(content_types=["text"])
def handle_text(message):
    txt = message.text.split(' ')

    if len(txt) > 2:
        bot.send_message(message.chat.id, token_format_message + "Ваше сообщение содержит более двух аргументов\n")
        return
    if len(txt) < 2:
        bot.send_message(message.chat.id, token_format_message + "Ваше сообщение содержит менее двух аргументов\n")
        return
    
    contest_id = txt[0]
    problem_id = txt[1]

    print("OK", contest_id, problem_id)

    reply_token(message=message, contest_id=contest_id, problem_id=problem_id)


def check_registered(cf_handle, tg_handle, message):
    if cached_users.__contains__(cf_handle):
        return True
    
    if udata.is_user_registered(tg_handle) == False:
        bot.send_message(message.chat.id, "Убедитесь, пожалуйста, что вы заполнили форму: " + links["register"])
        return False
    if CF.is_in_group(cf_handle) == False:
        bot.send_message(message.chat.id, "Убедитесь, пожалуйста, что вы присоединились к группе по ссылке: " + links["codeforces_group"])
        return False
    add_to_file("data/registered_users", cf_handle)
    cached_users.add(cf_handle)



def run():
    print("BEGIN")
    global cached_users
    cached_users = set(get_file("data/registered_users").split(' '))
    bot.polling(non_stop=True)
    
    
