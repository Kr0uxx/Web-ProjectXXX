import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send(email, text, person):
    mailsender = smtplib.SMTP('smtp.yandex.ru', 587)
    mailsender.starttls()
    mailsender.login('VerkTeam@yandex.ru', 'Verk2023')
    mail_subject = f'Notification from {person}'
    mail_body = 'Вам сообщение от', person, '-', text
    msg = MIMEText(mail_body, 'plain', 'utf-8')
    msg['Subject'] = Header(mail_subject, 'utf-8')
    mailsender.sendmail('VerkTeam@yandex.ru', email, msg.as_string())
    mailsender.quit()
    return f'Сообщение на адрес {email} отправлено, но может оказаться у человека в спаме!'
