
import openai
import telebot

openai.api_key =""
bot=telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Здравствуйте. Я глубоко обученная ии для помощи вам. Я могу придумать название для компании, написать сочинение, решить логические задачки и многое другое')

@bot.message_handler(func=lambda _: True)
def handke_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    bot.send_message(chat_id= message.from_user.id,text=response['choices'][0]['text'])
bot.polling()

