import telebot
import config
import dbworker
from datetime import datetime

bot = telebot.TeleBot(config.token)

# обработка команды /start
@bot.message_handler(commands=['start'])
def catalog(message):
    catalogKBoard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    get_info = telebot.types.KeyboardButton(text="Добавить нового пользователя")
    features = telebot.types.KeyboardButton(text="Текущая дата")
    catalogKBoard.add(get_info, features)
    bot.send_message(message.chat.id, "Выберите Раздел", reply_markup=catalogKBoard)


# Вывести текущую дату
@bot.message_handler(func=lambda message: message.text.lower() == 'текущая дата')
def send_data(message):
    current_datetime = datetime.now().strftime("%d-%m-%Y")
    bot.send_message(message.chat.id, current_datetime)


# Начало диалога - Добавление нового пользователя
@bot.message_handler(func=lambda message: message.text.lower() == 'добавить нового пользователя')
def new_user(message):
    state = dbworker.get_current_state(message.chat.id)
    if state == config.States.S_ENTER_NAME.value:
        bot.send_message(message.chat.id, "Кажется, кто-то обещал отправить своё имя, но так и не сделал этого :( Жду...")
    elif state == config.States.S_ENTER_AGE.value:
        bot.send_message(message.chat.id, "Кажется, кто-то обещал отправить свой возраст, но так и не сделал этого :( Жду...")
    else:  # Под "остальным" понимаем состояние "0" - начало диалога
        bot.send_message(message.chat.id, "Введите имя пользователя.")
        dbworker.set_state(message.chat.id, config.States.S_ENTER_NAME.value)


# По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога
@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    bot.send_message(message.chat.id, "Начнем сначала. Как вас зовут?")
    dbworker.set_state(message.chat.id, config.States.S_ENTER_NAME.value)


# Обработка имени пользователя
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_NAME.value)
def user_entering_name(message):
    # В случае с именем не будем ничего проверять, пусть хоть "25671", хоть Евкакий
    bot.send_message(message.chat.id, "Принято! Теперь укажите возраст пользователя.")
    dbworker.set_state(message.chat.id, config.States.S_ENTER_AGE.value)


# Обработка возраста пользователя
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_AGE.value)
def user_entering_age(message):
    # А вот тут сделаем проверку
    if not message.text.isdigit():
        # Состояние не меняем, поэтому только выводим сообщение об ошибке и ждём дальше
        bot.send_message(message.chat.id, "Что-то не так, попробуйте ещё раз!")
        return
    # На данном этапе мы уверены, что message.text можно преобразовать в число, поэтому ничем не рискуем
    if int(message.text) < 5 or int(message.text) > 100:
        bot.send_message(message.chat.id, "Какой-то странный возраст. Не верю! Отвечайте честно.")
        return
    else:
        # Возраст введён корректно, можно идти дальше
        bot.send_message(message.chat.id, 'Отлично! Больше ничего не требуется. Если захотите добавить еще пользователя - '
                                          'нажмите на кнопку "Добавить нового пользователя".')
        dbworker.set_state(message.chat.id, config.States.S_START.value)



if __name__ == '__main__':
    bot.polling(none_stop=True)

