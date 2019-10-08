from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
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



if __name__ == '__main__':
    app.run()