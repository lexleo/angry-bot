# -*- coding: utf-8 -*-

import config
import telebot
import random
from random import randint

bot = telebot.TeleBot(config.token)
active = True

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Иди-ка ты нахуй, {}!'.format(message.from_user.first_name))

@bot.message_handler(commands=['help'])
def help_me(message):
    bot.send_message(message.chat.id, 'Помощи он, блять, захотел!')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    global active
    text = message.text
    user = message.from_user.first_name

    # turn off
    if active and ('angrybot' in text.lower() or 'бот' in text.lower()) and ('заткнись' in text.lower() or 'усни' in text.lower()):
        bot.send_message(message.chat.id, 'Ой, ну всё!')
        active = False

    # turn on
    elif not active and ('angrybot' in text.lower() or 'бот' in text.lower()) and ('проснись' in text.lower() or 'привет' in text.lower()):
        bot.send_message(message.chat.id, 'Привет, мужики!')
        active = True

    # hi
    elif active and ('angrybot' in text.lower() or 'бот' in text.lower()) and ('здоров' in text.lower() or 'привет' in text.lower()):

        hi_list = ['Привет, {}!'.format(user), 'Приветствую тебя, {}!'.format(user), 'Здоров, {}!'.format(user), 'Здравствуй, {}!'.format(user),
                    'Привет!', 'Привет-привет!', 'Моё почтение, {}!'.format(user)]

        bot.send_message(message.chat.id, random.choice(hi_list))

    # how r u
    elif active and ('angrybot' in text.lower() or 'бот' in text.lower()) and ('как дела?' in text.lower()):

        status_list = ['Нормально, {}!'.format(user), 'Ты знаешь, {}? Хорошо!'.format(user), 'Норм',
                       'Нормально', 'Хорошо!', 'Заебись!', 'Отлично!', 'Так себе!', 'Ничо так!', 'Да не очень...',
                       '48 :)', 'В целом, пойдет!', 'Великолепно!', 'Потрясающе!']

        bot.send_message(message.chat.id, random.choice(status_list))

    # diff msgs
    elif active:
        res = ''
        if 'angrybot' in text.lower():
            bot_answer_list = ['{}, ты чё до меня доебался, а?!'.format(user),
                    'Ну хуй его знает!', 'Всё зависит от ситуации.',
                    'Это не может быть правдой!', 'Да ладно?!', 'Сам-то понял, что сказал?', 'Есть иное мнение!',
                    'Я тебе не верю!', 'Ты где это взял?', 'Ты что куришь?', 'Бухой что-ли?', 'No way!', 'А может и так.',
                    '{} - {}!'.format(user, random.choice(['хам', 'редиска', 'хамло', 'нахал, недалёкий человек'])),
                    'Хуй поспоришь!', 'Приехали...']
            res = random.choice(bot_answer_list)

        elif 'блять' in text.lower():
            if randint(0, 10) >= 5:
                res = 'Согласен!'

        elif 'гвоздика' in text.lower():
            res = 'Не пизди-ка!'

        elif text[-1] in '!':  # exclamation
            if randint(0,10) >= 8:

                excl_list = ['Вот именно!', 'Это охуенно!', 'Зашибись, да?!', 'Вот это новость!', 'Норм', 'Это не может не радовать',
                    'Мда уж...', 'Сказал - как отрезал!', 'Это достоверная информация?', 'А не пиздишь-ли как ты часом, милок?', 'И чо?',
                    'Не, ну и чо?', 'Это надо обдумать...', 'Шо то хуйня, шо это хуйня! Вот это обе хуйни, такие шо я бля ебал иво маму у рот!',
                    'Это всё объясняет!', 'Не, я на это не подписываюсь!', 'На что вы намекаешь?', 'И что из этого следует?',
                    'Хуй поспоришь!', 'Ну, йобаны-бобаны!']
                res = random.choice(excl_list)

        elif text[-1] == '?':  # question
            if randint(0,10) >= 8:

                qst_list = ['Тебе это зачем?', 'Я не по курсам', 'Не, не знаю', 'Сам-то что думаешь?', 'Ага! Щас...', 'Я не уверен в ответе',
                   'Это зависит не от меня', 'Не в этот раз!', 'А это интересно, да?', 'Что ж, поглядим...', 'Надо подумать',
                   'Вот я тоже мучаюсь этим вопросом!', 'А ведь и правда?', 'Что скажете, мужики?']
                res = random.choice(qst_list)

        if res != '':
            bot.send_message(message.chat.id, res)


if __name__ == '__main__':
    bot.polling(none_stop=True)
