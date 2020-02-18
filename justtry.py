import telebot
import requests
import yandex_weather_api
from bs4 import BeautifulSoup as BS
from telebot import apihelper

headers = {'User-Agent': 'Mozila/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

PROXY = 'K1nGsmaN:rdyz6v@45.139.30.189:14690'
apihelper.proxy = {'https': 'socks5h://K1nGsmaN:rdyz6v@45.139.30.189:14690'}

bot = telebot.TeleBot("721137451:AAFs7Y_DDCqi3xn1ORkIF8IvLNDVJzUyVsQ")





@bot.message_handler(commands=['weather_now'])
def send_weather_now(message):
    while True:
        r = requests.get('https://yandex.ru/pogoda/irkutsk', headers=headers)
        html = BS(r.content, 'html.parser')
        for el in html.select('.card_size_big'):
            fact_time = el.select('.fact__time-yesterday-wrap .fact__time')[0].text
            link_cond = el.select('.fact__temp-wrap .link__condition')[0].text
            temp_value = el.select('.fact__temp_size_s .temp__value')[0].text
            temp_feel = el.select('.fact__temp-wrap .temp__value')[0].text
            term_value = el.select('.fact__props .fact__humidity .term__value')[0].text
            wind_speed = el.select('.fact__props .term__value .wind-speed')[0].text
            term_press = el.select('.fact__props .fact__pressure .term__value')[0].text
            wind_rotate = el.select('.fact__props .term__value .fact__unit .icon-abbr')[0].text

            message_text = fact_time + '\n' + 'Погода: ' + link_cond + '\n' + 'Температура: ' + temp_value + 'С° (' + temp_feel + ' C°)' + '\n' + 'Влажность: ' + term_value + '\n' + 'Давление: ' + term_press + '\n' + 'Скорость ветра: ' + wind_speed + ' м/с, ' + wind_rotate
            print(message_text)
            bot.send_message(message.chat.id, message_text)
        break


bot.polling(none_stop=True)
