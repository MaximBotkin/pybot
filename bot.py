import telebot
import random
import pyowm
import datetime
import holidays

token = '1272902110:AAHb4KMzU1jOxeAW4mUNz1rYA8AMLJ0kvqs'
owm = pyowm.OWM(token, language="RU")

bot = telebot.TeleBot('1272902110:AAHb4KMzU1jOxeAW4mUNz1rYA8AMLJ0kvqs')

name_list = ['Алиса', 'Александра', 'Алёна', 'Алина', 'Алла', 'Анастасия', 'Анжелика', 'Анна', 'Валентина', 'Валерия', 'Вера', 'Вероника',
             'Виктория', 'Галина', 'Дарья', 'Диана', 'Ева', 'Ева', 'Евгения', 'Екатерина', 'Алёна', 'Елена', 'Елизавета', 'Жанна', 'Инна',
             'Ирина', 'Карина', 'Кристина', 'Ксения', 'Лариса', 'Любовь', 'Людмила', 'Маргарита', 'Марина', 'Мария', 'Мила', 'Милана',
             'Надежда', 'Наталья', 'Ника', 'Нина', 'Оксана', 'Олеся', 'Ольга', 'Полина', 'Руслана', 'Светлана', 'София', 'Софья', 'Тамара',
             'Татьяна', 'Юлия', 'Яна', 'Александр','Алексей', 'Анатолий', 'Андрей', 'Антон', 'Аркадий', 'Арсений', 'Артём', 'Артур', 'Борис',
             'Вадим', 'Валентин', 'Валерий', 'Василий', 'Виктор', 'Виталий', 'Владимир', 'Владислав', 'Вячеслав', 'Георгий', 'Глеб',
             'Григорий', 'Даниил', 'Денис', 'Дмитрий', 'Евгений', 'Егор', 'Иван', 'Игорь', 'Илья', 'Кирилл', 'Константин', 'Лев', 'Леонид',
             'Максим', 'Марк', 'Матвей', 'Михаил', 'Никита', 'Николай', 'Олег', 'Павел', 'Пётр', 'Роман', 'Руслан', 'Сергей', 'Степан', 'Тимур',
             'Фёдор', 'Юрий', 'Ярослав']


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, 'Привет, чем я могу тебе помочь?')
    elif message.text == "/help":
        bot.send_message(message.from_user.id, '1. Имя дня(/name)\n2. Рандомайзер(/number)\n3.Узнать текущую '
                                               'погоду в '
                                               'вашем городе(/weather)\n4. Узнать какой сегодня праздник(/day)')
    elif 'бот' in message.text.lower():
        bot.send_message(message.from_user.id, 'Бот - машина, машина - совершенный механизм!')
    elif '/name' in message.text.lower():
        bot.send_message(message.from_user.id, random.choice(name_list))
    elif '/number' in message.text.lower():
        bot.send_message(message.from_user.id, 'Рандомное число от 1 до 100: ')
        bot.send_message(message.from_user.id, random.randrange(1, 100, 1))
    elif '/weather' in message.text.lower():
        observation = owm.weather_at_place('Санкт-Петербург')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')['temp']
        status = w.get_temperature('celsius')
        st = w.get_detailed_status()
        now_temp, min_temp, max_temp = status['temp'], status['temp_min'], status['temp_max']
        bot.send_message(message.from_user.id, f'Температура на данный момент:  {round(now_temp)}')
        bot.send_message(message.from_user.id, f'Минимальная температура:  {int(min_temp)}')
        bot.send_message(message.from_user.id, f'Максимальная температура:  {int(max_temp)}')
        bot.send_message(message.from_user.id, f'Статус:  {st}')
    elif '/day' in message.text.lower():
        day = datetime.date.today()
        uk_holidays = holidays.UnitedKingdom()
        result = (uk_holidays.get(day))
        if result is None:
            bot.send_message(message.from_user.id, 'Сегодня нет никаких праздников:(')
        else:
            bot.send_message(message.from_user.id, result)
    elif 'пока' in message.text.lower():
        bot.send_message(message.from_user.id, 'Пока, буду тебя ждать!')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши /help.')


bot.polling(none_stop=True)
