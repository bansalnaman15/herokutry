from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.mail.yahoo.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME'] = 'pajeetsharma@yahoo.com'
app.config['MAIL_PASSWORD'] = 'nanchalchadwani'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/mail")
def index():
   msg = Message('Hello', sender = 'pajeetsharma@gmail.com', recipients = ['bansalnaman15@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail Naman"
   mail.send(msg)
   return "Sent"

@app.route('/')
def hello():
    return "Hello World!"



if __name__ == '__main__':
    app.run()