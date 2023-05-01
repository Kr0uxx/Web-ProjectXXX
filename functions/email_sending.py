import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send(email, text):
    mailsender = smtplib.SMTP('smtp.yandex.ru', 587)
    mailsender.starttls()
    mailsender.login('VerkTeam@yandex.ru', 'Verk2023')
    mail_subject = 'Notification from Verk Team'
    mail_body = text
    msg = MIMEText(mail_body, 'plain', 'utf-8')
    msg['Subject'] = Header(mail_subject, 'utf-8')
    mailsender.sendmail('VerkTeam@yandex.ru', email, msg.as_string())
    mailsender.quit()
    return f'Сообщение на адрес {email} отправлено'
