import telebot
import openai
openai.api_key = "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"
api = '5578853699:AAEV7CrjWrSZ9rHI54hzk3VSwNKchj4rYtg'
bot = telebot.TeleBot(api)

def rsp(question):
    prmt = "Q: {qst}\nA:".format(qst=question)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prmt,
        temperature=0,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text
@bot.message_handler(commands=['start', 'help', 'nanyadong'])
def send_welcome(message):
 bot.send_message(message.chat.id, 'gunakan /ask bro lalu pertanyaan atau peryataan yang ingin lu sampaikan bebas apa aja, karena gw bisa jawab pertanyaan apa aja asal masuk akal')
 
@bot.message_handler(func=lambda message: True) 
def echo_message(message):
 msg = message.text
 #print(msg)
 bot.send_message(message.chat.id, 'Tunggu bentar yaa beb!...')
 response = rsp(msg)
 #print(response)
 bot.send_message(message.chat.id, response)
    
 
print('bot start running')
bot.polling()
