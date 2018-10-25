import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

log_id = input(" Enter the username  ")
login_key = input("Enter the password ")               

server.login(log_id , login_key)

sender_id = input("Enter the sender mail ID ")
receiver_id = input("Enter the receiver mail ID ")
content = input("Enter the content of your mail  ")

server.sendmail(sender_id,receiver_id,content)

print("email is send successfully")
server.quit()
