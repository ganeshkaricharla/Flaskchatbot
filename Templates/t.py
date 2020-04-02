from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer



bot = ChatBot('Chatterbot')
conv =open('chat.txt','r').readlines()
trainer=ListTrainer(bot)
trainer.train(conv)

while True:
    request=input('you:')
    response=bot.get_response(request)
    print('bot:',response)
    
 