import config
import telebot
from datetime import datetime
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot(config.token)

# обработка команды /start
@bot.message_handler(commands=['start'])
def catalog(message):
    catalogKBoard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    get_info = telebot.types.KeyboardButton(text="Показать текущее время")
    features = telebot.types.KeyboardButton(text="Рассказать анекдот")
    catalogKBoard.add(get_info, features)
    bot.send_message(message.chat.id, "Выберите Раздел", reply_markup=catalogKBoard)


# обработка сообщения-кнопки времени
@bot.message_handler(func=lambda message: message.text.lower() == 'показать текущее время')
def send_welcome(message):
    current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    bot.send_message(message.chat.id, current_datetime)


# обработка сообщения-кнопки анекдота
@bot.message_handler(func=lambda message: message.text.lower() == 'рассказать анекдот')
def send_welcome(message):
    url = 'http://anekdotme.ru/random'
    response = requests.get(url)
    data = BeautifulSoup(response.text, "html.parser")
    joke = data.find("div", class_="anekdot_text").text
    bot.send_message(message.chat.id, joke)



if __name__ == '__main__':
    bot.polling(none_stop=True)
