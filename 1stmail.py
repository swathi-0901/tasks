import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login("swathi.kasikala@gmail.com","swathi123")


content = "a sample mail sent with my python script"

server.sendmail("swathi.kasikala@gmail.com","swathi.kasikala@gmail.com",content)
print("email is send successfully")
server.quit()
