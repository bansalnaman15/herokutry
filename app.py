
from flask import Flask,request
from flask_mail import Mail, Message

app = Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='localhost'
app.config['MAIL_PORT'] = 8062
app.config['MAIL_USERNAME'] = 'nanchalchadwani@gmail.com'
app.config['MAIL_PASSWORD'] = 'Mayank123'
app.config['MAIL_USE_TLS'] = True
mail = Mail(app)

@app.route("/mail")
def index():
   msg = Message('Hello', sender = 'nanchalchadwani@gmail.com', recipients = ['bansalnaman15@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail Naman"
   mail.send(msg)
   return "Sent"

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/url')
def url():
    return request.host_url;



if __name__ == '__main__':
    app.run()