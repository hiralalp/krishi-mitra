from flask import Flask, render_template, request
from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious")
from chatterbot.trainers import ListTrainer
import xlrd 


app = Flask(__name__)  
loc = ("agri_ques.xlsx") 
conversation=[]
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)  
#print(sheet.cell_value(0, 0)) 
r=sheet.nrows
c=sheet.ncols
for i in range(0,r):
    for j in range(0,c):
        conversation.append(sheet.cell_value(i,j))

trainer = ListTrainer(chatbot)

trainer.train(conversation)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True)
