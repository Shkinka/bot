import openai
import telebot

class Enviroment:
    openai_apk = "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"
    telegram_apk = "6315503381:AAFJ2HizQwkR9nx7typiLQl522-DYRbC6ww"
    
openai_key = Enviroment.openai_apk
telegram_key = Enviroment.telegram_apk


openai.api_key = openai_key
bot = telebot.TeleBot(telegram_key)

@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= message.text,
        temperature=0.5,
        max_tokens=400,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])

bot.polling()