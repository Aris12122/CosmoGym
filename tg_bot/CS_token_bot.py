from re import M
import telebot
from traitlets import default
from users_data import Users_data
import CF
import ans_token


udata = Users_data()

# token_format_message = "Пожалуйста, убедитесь, что вы правильно вводите команду: x Y\nГде x - номер контеста, Y - буква, соответствующая задаче\n"
error_message = "Что-то пошло не так, пожалуйста напишите @Aris12122"

links = {
    'stepik_course':    "",
    'codeforces_group': "",
    'register':         "https://forms.gle/89DsZeegTJ46XpXPA",
    'instructions':     "",
}


contest_last_letter = {
    0: "G",
    1: "J",
    2: "I",
    3: "P",
    4: "I",
    5: "L",
    6: "J",
}

first_contest = 0
last_contest = 6
current_module = 1


def get_file(path):
    with open(path) as f:
        return f.readline()

def add_to_file(path, mess):
    with open(path, 'a') as f:
        f.write(mess)


bot = telebot.TeleBot(get_file("secret/botAPI"))

cached_users = set()
cached_cf_handles = set()

def add_contestant(message, tg_handle, cf_handle):
    add_to_file("data/contestants", str(message.chat.id) + " " + tg_handle + " " + cf_handle + "\n")

def check_registered(message, tg_handle = "", cf_handle = ""):
    global cached_users
    global cached_cf_handles
    try:
        if (tg_handle == "") :
            tg_handle = message.from_user.username

        print("Checking... " + str(tg_handle))

        if cached_users.__contains__(tg_handle):
            return True

        if udata.is_user_registered(tg_handle) == False:
            print("Not registered " + str(tg_handle))
            bot.send_message(message.chat.id, "Убедитесь, пожалуйста, что вы правильно заполнили форму: " + links["register"])
            return False
        

        if (cf_handle == "") :
            cf_handle = udata.get_cf_handle_by_tg(tg_handle)
        
        # if CF.is_in_group(cf_handle) == False:
        #     bot.send_message(message.chat.id, "Убедитесь, пожалуйста, что вы присоединились к группе по ссылке: " + links["codeforces_group"])
        #     return False
    
    except Exception as e:
        bot.send_message(message.chat.id, error_message)
        print("Fail check_registered " + str(e))
        return False

    print("Successfully checked " + str(tg_handle) + " " + str(cf_handle))
    add_to_file("data/registered_users", " " + tg_handle)
    cached_users.add(tg_handle)
    cached_cf_handles.add(cf_handle)
    add_to_file("data/cf_handles", " " + cf_handle)
    add_contestant(message=message, tg_handle=tg_handle, cf_handle=cf_handle)

    return True



@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Проверка...")
    if (str(message.from_user.username) == "None"):
        print("Опять этот None")
        try:
            print(str(message))
        except:
            print("Не получилось")
        bot.send_message(message.chat.id, "Пожалуйста, пищите со своего аккаунта. Повторите попытку с помощью команды /start")
        return
    if check_registered(message=message):
        bot.send_message(message.chat.id, "Приветствую вас на нашем курсе! Вы успешно зарегистрировались!")
    else:
        bot.send_message(message.chat.id, "Регистрация не завершена. Повторите попытку с помощью команды /start")


def get_solved_full(tg_handle, cf_handle):
    print("reply to " + cf_handle + " ")
    solved = 0
    for contest_id in range(first_contest, last_contest + 1):
        solved += get_solved(tg_handle, cf_handle, contest_id)
    return solved

def get_solved(tg_handle, cf_handle, contest_id):
    print("For contest: " + str(contest_id))

    # if len(problem_id) != 1:
    #     bot.send_message(message.chat.id, token_format_message + "Название задачи должен быть одной буквой\n")
    #     return

    # if isalpha(problem_id[0]) == False:
    #     bot.send_message(message.chat.id, token_format_message + "Название задачи должен быть буквой\n")
    #     return

    # if contest_id.isnumeric() == False:
    #     bot.send_message(message.chat.id, token_format_message + "Ваш номер контеста не является числом\n")
    #     return

    cnt = 0

    for i in range(ord("A"), ord(contest_last_letter[contest_id])):
        problem_id = chr(i)
        # print(problem_id)
        try:
            if CF.is_solved(contest_id=contest_id, problem_id=problem_id, handle=cf_handle):
                cnt += 1
        except Exception as e:
            print("Error occurred with checking CF_is_solved with problem:" + problem_id)
            print("Error occurred to " + cf_handle)
            print(str(e))
    print(cnt)
    return cnt

    # if contest_id > len(contests):
    #     bot.send_message(message.chat.id, token_format_message + "Контеста с таким номером не существует\n")
    #     return

    # if problem_id[0] > contests[contest_id]:
    #     bot.send_message(message.chat.id, token_format_message + "В этом контесте нет задачи с таким названием\n")
    #     return

    

    # if CF.is_solved(contest_id=contest_id, problem_id=problem_id, handle=cf_handle):
    #     bot.send_message(message.chat.id, ans_token.get_token(contest_id, problem_id, cf_handle))
    # else:
    #     bot.send_message(message.chat.id, "Вы пока не решили эту задачу, попробуйте позже")
    


# @bot.message_handler(commands=["token"])
# def get_token(message):

#     txt = message.text.split(' ')

#     if len(txt) > 3:
#         bot.send_message(message.chat.id, token_format_message + "Ваше сообщение содержит более двух аргументов\n")
#         return
#     if len(txt) < 3:
#         bot.send_message(message.chat.id, token_format_message + "Ваше сообщение содержит менее двух аргументов\n")
#         return
    
#     contest_id = txt[1]
#     problem_id = txt[2]

#     reply_token(message=message, contest_id=contest_id, problem_id=problem_id)


#     ans_token.get_ans_token(1, 2, "Aris")
#     ans_token.get_ans_token(2, 2, "Aris")
#     ans_token.get_ans_token(1, 3, "Aris")
#     ans_token.get_ans_token(2, 3, "Aris")
#     ans_token.get_ans_token(2, 3, "aris")
#     ans_token.get_ans_token(1, 2, "myav")
#     ans_token.get_ans_token(0, 0, "myav")
#     ans_token.get_ans_token(1, 0, "myav")
#     ans_token.get_ans_token(0, 1, "myav")



# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     txt = message.text.split(' ')

#     if len(txt) > 2:
#         bot.send_message(message.chat.id, token_format_message + "Ваше сообщение содержит более двух аргументов\n")
#         return
#     if len(txt) < 2:
#         bot.send_message(message.chat.id, token_format_message + "Ваше сообщение содержит менее двух аргументов\n")
#         return
    
#     contest_id = txt[0]
#     problem_id = txt[1]

#     print("OK", contest_id, problem_id)

#     reply_token(message=message, contest_id=contest_id, problem_id=problem_id)





@bot.message_handler(commands=["print_tokens"])
def get_token(message):

    if (message.from_user.username == "Aris12122") :
        all_solved = 0
        for contest_id in range(first_contest, last_contest + 1):
            all_solved += ord(contest_last_letter[contest_id]) - ord('A')
        print("Всего решено: " + str(all_solved))
        solved = 0
        with open("data/contestants") as f:
            contestants = f.readlines()
        for i in range (21, len(contestants)):
            contestant = contestants[i].split(' ')
            message_id = contestant[0]
            tg_handle = contestant[1]
            cf_handle = contestant[2]
            if cf_handle[-1] == '\n':
                cf_handle = cf_handle[:len(cf_handle) - 1]
            print(cf_handle)
            solved = 0
            try:
                solved += get_solved_full(tg_handle=tg_handle, cf_handle=cf_handle)
            except Exception as e:
                print("Error occurred while processing " + cf_handle)
                print(str(e))
                continue
            print(cf_handle, solved)
            print(cf_handle + " Solved " + str(solved) + " of tasks")
            if solved == 0:
                continue
            token = ans_token.get_ans_token(solved, cf_handle)
            print("Token: " + str(cf_handle) + " " + token)
            bot.send_message(message_id, "Ваш токен за четверть #" + str(current_module) + ", в которой вы решили " + str(solved) + " задач:")
            bot.send_message(message_id, str(cf_handle) + " " + token)
            return
    else:
        bot.send_message(bot.chat.id, "У вас недостаточно прав для данной команды")


    
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, "К сожалению, я понимаю только команду /start")

# @bot.message_handler(commands=["print_memes"])
# def get_token(message):

#     if (message.from_user.username == "Aris12122") :
#         with open("data/contestants") as f:
#             contestants = f.readlines()
#         for i in range (0, len(contestants)):
#             contestant = contestants[i].split(' ')
#             message_id = contestant[0]
#             tg_handle = contestant[1]
#             cf_handle = contestant[2]
#             try:
#                 solved = get_solved(tg_handle=tg_handle, cf_handle=cf_handle, current_contest=current_contest)
#             except:
#                 print("Error occurred while processing " + cf_handle)
#                 return
#             print(cf_handle + " Solved ", solved, " of tasks")
#             token = get_token()
#             bot.send_message()

#     else:
#         bot.send_message(bot.chat.id, "У вас недостаточно прав для данной команды")


while True:
    try:
        print("BEGIN")
        cached_users = set(get_file("data/registered_users").split(' '))
        bot.polling(non_stop=True)
    except Exception as e:
        print("Global fail: " + str(e))
        continue
    break
