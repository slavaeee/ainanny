import telebot
from openai import OpenAI
import time

def ask(question):
    client = OpenAI(
    api_key="sk-dL6rDXTmiYyPRuFNMqsJGkR2F2B3shZT",
    base_url="https://api.proxyapi.ru/openai/v1")

    chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo", messages=[
        {"role": "system", "content": "Ты отвечаешь молодому родителю на бытовые вопросы про то, как обращаться с маленькими детьми"},
        {"role": "user", "content": question},
    ])
    return chat_completion.choices[0].message.content, time.time()


TOKEN = '6820885331:AAGWVB4c0_7yv9spHdUKCgHLwhTy-VNoUNU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    time_start = time.time()
    question = message.text
    question += '. В конце ответа укажи ссылки на источники, с которых взята информация.'
    response, time_stop = ask(question)
    bot.reply_to(message, response)
    print('Ответ сгенерирован за', (time_stop - time_start), 'секунд')
bot.polling()


# In[ ]:




