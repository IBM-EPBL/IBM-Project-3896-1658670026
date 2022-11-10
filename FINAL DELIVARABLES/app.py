from flask import Flask,render_template

app = Flask(__name__)

@app.route('/Chatbot', methods = ['GET','POST'])

def Chatbot():
    return render_template('Chatbot.html')

if __name__ == '__main__':
 app.run()