import smtplib, ssl

port = 465
password = input("Mayank123")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("nanchalchadwani@gmail.com", password)
    server.sendmail("nanchalchadwani@gmail.com","bansalnaman15@gmail.com", "Hello Naman")
