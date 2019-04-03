import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

#Next, log in to the server
server.starttls()
server.login("aviralsocialcops@gmail.com", "!ndicaDLS02")

def send():
    msg = """
    John!"""
    server.sendmail("aviralsocialcops@gmail.com", "aviralsocialcops@gmail.com", msg)
