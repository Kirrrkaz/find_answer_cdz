import finder
import telebot
import config
import urllib.parse as urlparse

bot = telebot.TeleBot(config.API_TOKEN)



@bot.message_handler(commands=['start', 'help'])
def handle_message(message):
    sent = bot.send_message(message.chat.id, "Введите ссылку :", )
    bot.register_next_step_handler(sent, save_link)
    

def save_link(message):
    my_link = message.text
    
    if urlparse.urlparse(message.text).scheme:
        
        bot.send_message(message.chat.id, "Получил! Ожидайте ответа.")
        answers = finder.get_answers(message.text)
        for i in answers:
            bot.send_message(message.chat.id,'❓ Вопрос: ' + i[0] +'\n' + '\n' + '✔️ Ответ: ' + i[1] )
    else:
        sent = bot.send_message(message.chat.id, "Ошибка")


if __name__ == '__main__':
     bot.infinity_polling()

""" bot.polling(none_stop=True) """

#https://codeby.net/threads/kak-stat-xakerom-i-kak-vzlomat-sajt-ili-begloe-znakomstvo-s-owasp-testing-guide.67997/?__cf_chl_captcha_tk__=pmd_1Yz1Z4C_Kr3VBfUUgmAVoSrFkF898q6.FUSkAJxABso-1635855476-0-gqNtZGzNA3ujcnBszQfR

#https://codeby.net/threads/virus-udalenogo-dostupa-v-telegram-cherez-python.72457/