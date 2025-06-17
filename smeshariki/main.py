import json
import telebot
import random

bot_api_key = "7588462343:AAEQhbTYcXdfgYMHAY34jkf-97Cyi_7C7VI"
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
        "test_id": 0,
        "points": 0,
        "correct_answer": 0,
        "current_question": 0,
        "current_test": 0,
        "ans_0": 0,
        "ans_1": 0,
        "ans_2": 0,
        "ans_3": 0,
        "ans_4": 0,
        "ans_5": 0,
        "ans_6": 0,
        "ans_7": 0,
        "ans_8": 0,
    }


@bot.message_handler(commands=["start"])
def reply(message: telebot.types.Message):
    add_user(str(message.from_user.id))
    save_users()
    bot.reply_to(message, "пПривЕТуЛИ")
    bot.send_message(message.from_user.id, "Хотите начать игру?\n\n" + "/go")
    send_memes(message.from_user.id)


@bot.message_handler(commands=["go"])
def reply(message: telebot.types.Message):
    bot.reply_to(message, "Итак, всё просто: это игра о жизни самых круглых мультгероев\nКаждый вопрос может "
                          "принести тебе 1 балл. Давай, будет весело!\n\n/pognali")


@bot.message_handler(commands=["pognali", "zanovo"])
def reply(message: telebot.types.Message):
    users[str(message.from_user.id)]['test_id'] = 0
    users[str(message.from_user.id)]['correct_answer'] = 0
    users[str(message.from_user.id)]['points'] = 0
    users[str(message.from_user.id)]['current_question'] = 0
    first_question(str(message.from_user.id))


@bot.message_handler(commands=["results"])
def reply(message: telebot.types.Message):
    if users[str(message.from_user.id)]['points'] < 5:
        bot.reply_to(message, "Чел, это кринж, ты абсолютный позер, кажется ты пропустил, когда выдавали детство")
    elif users[str(message.from_user.id)]['points'] < 10:
        bot.reply_to(message, "Видно, что Крош и Совунья не последние персонажи в твоей жизни, но искать смысл жизни с барашем ты ещё не готов!"
                              "Уходи и, когда будешь готов, возвращайся, чтобы доказать, что ты настоящий смешарик...")
    else:
        bot.reply_to(message, "Поздравляю! Пока у других 10к часов в CS, ты тратишь время на правильные вещи, такие как просмотр любимых смешариков! "
                              "Мы готовы принять тебя в свою команду, ведь ты настоящий круг")

    send_memes(message.from_user.id)
    bot.send_message(str(message.from_user.id), "В меню можешь посмотреть последний результат или пройти тест заново\n\n А если ты готов к самой ответственной миссии жми\n/yhyy")


@bot.message_handler(commands=["last"])
def reply(message: telebot.types.Message):
    bot.reply_to(message, f"Твой последний результат - {users[str(message.from_user.id)]['points'] :.2f} баллов\nЕсли хочешь улучшить результат, проходи заново:\n/zanovo")


@bot.message_handler(commands=["yhyy"])
def reply(message: telebot.types.Message):
    bot.reply_to(message, "Если ты ещё тут, значит всё идёт по плану... "
                          "Сейчас нам предстоит поистине ответственная миссия: понять, кто же ты из наших любимок\nжми \n/test")


@bot.message_handler(commands=["res_test"])
def reply(message: telebot.types.Message):
    results = []
    for i in range(9):
        results.append(users[str(message.from_user.id)]['ans_' + str(i)])
    res = results.index(max(results))
    if res == 0:
        bot.reply_to(message, "Ты - Крош!\nЭнергичный, неугомонный, всегда готов к приключениям и новым открытиям.")
    elif res == 1:
        bot.reply_to(message, "Ты - Бараш!\nРомантичный, мечтательный, ранимый, но очень талантливый поэт.")
    elif res == 2:
        bot.reply_to(message, "Ты - Лосяш!\nЛюбознательный, эрудированный, увлеченный наукой, часто витаешь в облаках.")
    elif res == 3:
        bot.reply_to(message, "Ты - Копатыч!\nПрактичный, хозяйственный, заботливый, всегда готов прийти на помощь.")
    elif res == 4:
        bot.reply_to(message, "Ты - Пин!\nИзобретательный, технически подкованный, немного чудаковатый, но очень талантливый инженер.")
    elif res == 5:
        bot.reply_to(message, "Ты - Нюша!\nОбщительная, модная, любящая внимание, обожаешь веселье и вечеринки.")
    elif res == 6:
        bot.reply_to(message, "Ты - Совунья!\nЗаботливая, мудрая, спортивная, всегда готова дать совет и поддержать.")
    elif res == 7:
        bot.reply_to(message, "Ты - Ёжик!\nИнтеллектуальный, спокойный, любит порядок, ценит дружбу и коллекционирование.")
    elif res == 8:
        bot.reply_to(message, "Ты - Кар-Карыч!\nМудрый, опытный, загадочный, склонен к размышлениям о жизни и прошлом.")
    send_memes(message.from_user.id)
    bot.reply_to(message, "Если захочешь ещё раз попробовать свои силы в наших тестах, используй кнопки в меню бота!")


@bot.message_handler(commands=["test"])
def reply(message: telebot.types.Message):
    users[str(message.from_user.id)]['test_id'] = 1
    users[str(message.from_user.id)]['ans_0'] = 0
    users[str(message.from_user.id)]['ans_1'] = 0
    users[str(message.from_user.id)]['ans_2'] = 0
    users[str(message.from_user.id)]['ans_3'] = 0
    users[str(message.from_user.id)]['ans_4'] = 0
    users[str(message.from_user.id)]['ans_5'] = 0
    users[str(message.from_user.id)]['ans_6'] = 0
    users[str(message.from_user.id)]['ans_7'] = 0
    users[str(message.from_user.id)]['ans_8'] = 0
    bot.send_message(str(message.from_user.id),
                     "Инструкция: Ответьте на вопросы, выбирая вариант, который наиболее вам подходит. В некоторых вопросах можно выбрать несколько подходящих вариантов")
    question_1(str(message.from_user.id))


@bot.poll_answer_handler()
def poll_answer_handler(poll_answer: telebot.types.PollAnswer):
    if users[str(poll_answer.user.id)]['test_id'] == 0:
        if poll_answer.option_ids[0] == users[str(poll_answer.user.id)]['correct_answer']:
            users[str(poll_answer.user.id)]['points'] += 1
        send_next_question(str(poll_answer.user.id))
    else:
        for b in poll_answer.option_ids:
            a = str(b)
            users[str(poll_answer.user.id)]['ans_' + a] += 1
        send_next_test(str(poll_answer.user.id))


def send_memes(id):
    with open('sticker.txt', 'r') as file:
        data = file.read().split(';')
        #sticker_id = random.choice(data)
        for sticker_id in data:
            print(sticker_id)
            bot.send_sticker(id, sticker_id)



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
    elif users[id]['current_question'] == 5:
        seventh_question(id)
    elif users[id]['current_question'] == 6:
        eighth_question(id)
    elif users[id]['current_question'] == 7:
        ninth_question(id)
    elif users[id]['current_question'] == 8:
        tenth_question(id)
    elif users[id]['current_question'] == 9:
        eleventh_question(id)
    elif users[id]['current_question'] == 10:
        twelfth_question(id)
    elif users[id]['current_question'] == 11:
        thirteenth_question(id)
    else:
        bot.send_message(id, "На этом всё! Все тайны любимых мультгероев раскрыты, надеюсь тебе понравилось\nХочешь узнать результаты? Жми \n/results")


def send_next_test(id):
    if users[id]['current_test'] == 0:
        question_2(id)
    elif users[id]['current_test'] == 1:
        question_3(id)
    elif users[id]['current_test'] == 2:
        question_4(id)
    elif users[id]['current_test'] == 3:
        question_5(id)
    elif users[id]['current_test'] == 4:
        question_6(id)
    else:
        bot.send_message(id, "Отлично! Вопросы почти закончились... остался лишь один: кто же ты из смешариков?\n\n Чтобы узнать результат, \nжми /res_test")


def question_6(id):
    send_memes(id)
    bot.send_poll(id, "Какой цвет тебе больше всего нравится?",
                  ["Синий", "Фиолетовый", "Оранжевый", "Коричневый", "Серебристый", "Розовый", "Зеленый", "Серый", "Белый"],
                  type="regular", is_anonymous=False, allows_multiple_answers=False)
    users[id]['current_test'] += 1


def question_5(id):
    send_memes(id)
    bot.send_poll(id, "Какой твой любимый вид отдыха?",
                  ["Поход", "Вечер у камина с книгой", "Посещение научного музея", "Работа в огороде",
                   "Конструирование", "Вечеринка с друзьями", "Прогулка по лесу или парку", "Шахматы или решение головоломок", "Медитация на природе"],
                  type="regular", is_anonymous=False, allows_multiple_answers=True)
    users[id]['current_test'] += 1


def question_4(id):
    bot.send_poll(id, "Что для тебя самое важное в дружбе?",
                  ["Общие интересы", "Душевная близость и взаимопонимание", "Возможность учиться друг у друга", "Надежность и поддержка",
                   "Совместное творчество и изобретения", "Веселье и хорошее настроение", "Забота и помощь", "Интеллектуальные беседы", "Личное пространство"],
                  type="regular", is_anonymous=False, allows_multiple_answers=False)
    users[id]['current_test'] += 1


def question_3(id):
    send_memes(id)
    bot.send_poll(id, "Какая музыка тебе нравится?",
                  ["Бодрая и энергичная", "Мелодичная и романтическая", "Классическая", "Народная", "Техно и электронная", "Популярная и танцевальная",
                   "Спокойная и расслабляющая", "Джаз и блюз", "Медитативная и этническая"],
                  type="regular", is_anonymous=False, allows_multiple_answers=True)
    users[id]['current_test'] += 1


def question_2(id):
    send_memes(id)
    bot.send_poll(id, "Какие черты характера наиболее тебе присущи?",
                  ["Энергичность", "Романтичность", "Любознательность", "Практичность", "Изобретательность", "Общительность", "Заботливость", "Интеллектуальность", "Мудрость"],
                  type="regular", is_anonymous=False, allows_multiple_answers=True)
    users[id]['current_test'] += 1


def question_1(id):
    bot.send_poll(id, "Что тебе больше всего нравится делать в свободное время?",
                  ["Активно отдыхать, играть в спортивные игры", "Писать стихи, мечтать", "Заниматься наукой", "Заботиться о саде",
                   "Придумывать и мастерить", "Веселиться с друзьями, устраивать вечеринки", "Заботиться о других, давать советы",
                   "Читать книги, разгадывать загадки", " Медитировать и размышлять о жизни"],
                  type="regular", is_anonymous=False, allows_multiple_answers=True)
    users[id]['current_test'] = 0


def thirteenth_question(id):
    bot.send_poll(id, "Настоящее имя Копатыча - ...?",
                  ["Константин", "Косьян", "Кузьмич", "Кирилл"],
                  correct_option_id=1, type="quiz", is_anonymous=False)
    users[id]['correct_answer'] = 1
    users[id]['current_question'] += 1


def twelfth_question(id):
    send_memes(id)
    bot.send_poll(id, "Какое изобретение Пина чуть не привело к катастрофе в серии 'Эффект бабушки'?",
                  ["Машина времени", "Увеличитель предметов", "Клонирующий аппарат", "Телепорт"],
                  correct_option_id=0, type="quiz", is_anonymous=False)
    users[id]['correct_answer'] = 0
    users[id]['current_question'] += 1


def eleventh_question(id):
    send_memes(id)
    bot.send_poll(id, "В какой серии Кар-Карыч рассказывает историю о своей юности в цирке?",
                  ["Куда приводят мечты", "Только горы", "Рояль", "Билет в один конец"],
                  correct_option_id=2, type="quiz", is_anonymous=False)
    users[id]['correct_answer'] = 2
    users[id]['current_question'] += 1


def tenth_question(id):
    bot.send_poll(id, "Какое хобби есть у Ёжика, которое не разделяет Крош?",
                  ["Собирать фантики", "Собирать кактусы", "Собирать марки", "Собирать машинки"],
                  correct_option_id=0, type="quiz", is_anonymous=False)
    users[id]['correct_answer'] = 0
    users[id]['current_question'] += 1


def ninth_question(id):
    send_memes(id)
    bot.send_poll(id, "В какой серии Копатыч становится детективом?",
                  ["Эффект бабушки", "Дело о пропавшей моркови", "Новые приключения", "Рояль"],
                  correct_option_id=1, type="quiz", is_anonymous=False)
    users[id]['correct_answer'] = 1
    users[id]['current_question'] += 1


def eighth_question(id):
    send_memes(id)
    bot.send_poll(id, "Что Бараш использует в качестве источника вдохновения для своих стихов?",
                  ["Книги", "Природу", "Нюшу", "Свои сны"],
                  correct_option_id=2, type="quiz", is_anonymous=False)
    users[id]['correct_answer'] = 2
    users[id]['current_question'] += 1


def seventh_question(id):
    send_memes(id)
    bot.send_poll(id, "Как зовут инопланетного друга Пина, с которым он часто переписывается?",
                  ["Биби", "Муля", "Игого", "Дин-Дин"],
                  correct_option_id=0, type="quiz", is_anonymous=False)
    users[id]['correct_answer'] = 0
    users[id]['current_question'] += 1


def sixth_question(id):
    bot.send_poll(id, "В каком виде спорта Совунья проявляет наибольший талант?",
                  ["Теннис", "Хоккей", "Фигурное катание", "Шахматы"],
                  correct_option_id=2, type="quiz", is_anonymous=False)
    users[id]['correct_answer'] = 2
    users[id]['current_question'] += 1


def fifth_question(id):
    send_memes(id)
    bot.send_poll(id, " Какую фразу постоянно повторяет Пин?",
                  ["Однако!", "Я так думаю!", "Вот это да!", "Элементарно, Ватсон!"],
                  correct_option_id=0, type="quiz", is_anonymous=False)
    users[id]['correct_answer'] = 0
    users[id]['current_question'] += 1


def fourth_question(id):
    bot.send_poll(id, "Кто из Смешариков построил 'Музей всего'?",
                  ["Пин", "Копатыч", "Лосяш", "Бараш"],
                  correct_option_id=0, type="quiz", is_anonymous=False)
    users[id]['correct_answer'] = 0
    users[id]['current_question'] += 1


def third_question(id):
    send_memes(id)
    bot.send_poll(id, "Каким видом научной деятельности увлекается Лосяш?",
                  ["Ботаника", "Физика", "Астрономия", "Химия"],
                  correct_option_id=2, type="quiz", is_anonymous=False)
    users[id]['correct_answer'] = 2
    users[id]['current_question'] += 1


def second_question(id):
    send_memes(id)
    bot.send_poll(id, "Какой музыкальный инструмент предпочитает Кар-Карыч?",
                  ["Гитара", "Пианино", "Аккордеон", "Барабаны"],
                  correct_option_id=1, type="quiz", is_anonymous=False)
    users[id]['correct_answer'] = 1
    users[id]['current_question'] += 1


def first_question(id):
    bot.send_poll(id, "Как зовут фиолетовую зайку, которая очень любит заниматься спортом?",
                  ["Нюша", "Крошик", "Совунья", "Биби"],
                  correct_option_id=2, type="quiz", is_anonymous=False)
    users[id]['correct_answer'] = 2
    users[id]['current_question'] = 0


if __name__ == "__main__":
    init_users()
    bot.infinity_polling()
    save_users()
