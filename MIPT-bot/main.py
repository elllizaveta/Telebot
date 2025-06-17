import json
import telebot

bot_api_key = "5706247006:AAGG8eZ6rP9vyVaGBCc-jjvTYcZMrC3jXsE"
bot = telebot.TeleBot(bot_api_key)
users = dict()


def init_users():
    global users
    try:
        users = dict(json.loads(open("users.json", 'r', encoding="utf-8").read()))
    except:
        users = dict()


def save_users():
    open("users.json", 'w', encoding="utf-8").write(json.dumps(users, ensure_ascii=False))


def get_user_by_id(user_id):
    return dict[user_id]


def add_user(user_id):
    users[user_id] = {
        "points": 0,
        "correct_answer": 0,
        "current_question": 0
    }


@bot.message_handler(commands=["results"])
def reply(message: telebot.types.Message):
    if users[str(message.from_user.id)]['points'] < 3:
        bot.reply_to(message, "Чел, это кринж, ты абсолютный хиккан и позер")
    elif users[str(message.from_user.id)]['points'] < 5:
        bot.reply_to(message, "В иерархии ты стоишь чуть ниже таракана в душе, а твоя тупая ссальная рожа не помещается на электронный пропуск")
    else:
        bot.reply_to(message, "Поздравляю, ты рил тру хайп коннектид кент физтеха и гигачад!")
    bot.send_message(str(message.from_user.id), "В меню можешь посмотреть последний результат или пройти тест заново")


def send_next_question(id):
    if users[id]['current_question'] == 0:
        second_question(id)
    elif users[id]['current_question'] == 1:
        third_question(id)
    elif users[id]['current_question'] == 2:
        fourth_question(id)
    elif users[id]['current_question'] == 3:
        fifth_question(id)
    elif users[id]['current_question'] == 4:
        sixth_question(id)
    else:
        bot.send_message(id, "На этом всё! Спонсор вопросов - посвят ФПМИшечки 2022, надеюсь тебе поннравилось\nХочешь узнать результаты? Жми \n/results")


@bot.poll_answer_handler()
def poll_answer_handler(poll_answer: telebot.types.PollAnswer):
    if poll_answer.option_ids[0] == users[str(poll_answer.user.id)]['correct_answer']:
        users[str(poll_answer.user.id)]['points'] += 1
    send_next_question(str(poll_answer.user.id))


def sixth_question(id):
    bot.send_poll(id, "Кого нет на стене нобелевский лауреатов физтеха?",
                  ["тебя", "..."],
                  correct_option_id=0, type="quiz", is_anonymous=False)
    users[id]['correct_answer'] = 0
    users[id]['current_question'] += 1



def fifth_question(id):
    bot.send_poll(id, "Представим ситуацию: ты учил английский 18 лет, в какую группу ты попадешь?",
                  ["B1", "Advanced", "Elementary", "中文"],
                  correct_option_id=3, type="quiz", is_anonymous=False)
    users[id]['correct_answer'] = 3
    users[id]['current_question'] += 1


def fourth_question(id):
    bot.send_poll(id, "Вас зажали два милиционера, ваши действия",
                  ["Мой предел - это пятера", "Позвоню Маме",
                   "Милицию переменовали в полицию ФЗ от 7 февраля 2011 года №3 О полиции", "Что за беспредел!"],
                  correct_option_id=0, type="quiz", is_anonymous=False)
    users[id]['correct_answer'] = 0
    users[id]['current_question'] += 1


def third_question(id):
    bot.send_poll(id, "К вам подходит несколько студентов и спрашивают: уважаемые коллеги, дед-факер, "
                      "кокнул на коллоке?, получил уд-3, плевать на БРС, го на нк ловить катарсис и кушать блинчики. "
                      "Ваши действия:",
                  ["Прописать веРТуху", "ФАКТы, идите домой", "Скажу: Товарищи давайте начнем, звонок уже был",
                   "Богданов"],
                  correct_option_id=2, type="quiz", is_anonymous=False)
    users[id]['correct_answer'] = 2
    users[id]['current_question'] += 1


def second_question(id):
    bot.send_poll(id, "С какой парты видно пробелы Кулапина?",
                  ["Это кто?", "Он что-то пишет?", "Ни с какой", "Богданов"],
                  correct_option_id=2, type="quiz", is_anonymous=False)
    users[id]['correct_answer'] = 2
    users[id]['current_question'] += 1


def first_question(id):
    bot.send_poll(id, "Во сколько начинаются пары Мещерина?",
                  ["в 9:00, по расписанию", "Мещерин? его ж числанули", "@mesyarik, скиньте, пожалуйста, записи",
                        "Ilya Mescherin: так, сорян, что-то опять не получилось вовремя начать"],
                  correct_option_id=3, type="quiz", is_anonymous=False)
    users[id]['correct_answer'] = 3
    users[id]['current_question'] = 0


@bot.message_handler(commands=["start"])
def reply(message: telebot.types.Message):
    add_user(str(message.from_user.id))
    save_users()
    bot.reply_to(message, "пПривЕТуЛИ")
    bot.send_message(message.from_user.id, "Хотите начать игру?\n\n" + "/go")


@bot.message_handler(commands=["go"])
def reply(message: telebot.types.Message):
    bot.reply_to(message, "Итак, всё просто: это игра о жизни на физтехе from посвят 2022 ФПМИ\nКаждый вопрос может "
                          "принести тебе 1 балл. Давай, будет весело!\n\n/pognali")


@bot.message_handler(commands=["pognali", "zanovo"])
def reply(message: telebot.types.Message):
    users[str(message.from_user.id)]['correct_answer'] = 0
    users[str(message.from_user.id)]['points'] = 0
    users[str(message.from_user.id)]['current_question'] = 0
    first_question(str(message.from_user.id))


@bot.message_handler(commands=["last"])
def reply(message: telebot.types.Message):
    bot.reply_to(message, f"Твой последний результат - {users[str(message.from_user.id)]['points'] :.2f} баллов\nЕсли хочешь улучшить результат, проходи заново:\n/zanovo")


if __name__ == "__main__":
    init_users()
    bot.infinity_polling()
    save_users()
