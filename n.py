from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer ,ChatterBotCorpusTrainer
import os
 
app = Flask(__name__)
 
bot = ChatBot("Chat Bot",storage_adapter="chatterbot.storage.SQLStorageAdapter",database="botData.sqlite3")
 
trainer=ListTrainer(bot)

for _file in os.listdir('data'):
    chats=open('data/'+_file,'r').readlines()
    trainer.train(chats)

trainer =ChatterBotCorpusTrainer(bot)
trainer.train("data2/")
    
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response=bot.get_response(userText)
  
    if response.confidence >0.5:
        return str(response)
    else :
        return 'Could not understand'

if __name__ == "__main__":
    app.run()
    
    
