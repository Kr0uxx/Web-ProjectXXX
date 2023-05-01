import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send(email, text, person):
    try:
        mailsender = smtplib.SMTP('smtp.yandex.ru', 587)
        mailsender.starttls()
        #mailsender.login('VerkTeam@yandex.ru', 'Verk2023')
        mailsender.login('GlObG1@yandex.ru', 'Sorokin109977')
        mail_subject = f'Notification from {person}'
        mail_body = f'Вам сообщение от {person} - {text}'
        msg = MIMEText(mail_body, 'plain', 'utf-8')
        msg['Subject'] = Header(mail_subject, 'utf-8')
        mailsender.sendmail('GlObG1@yandex.ru', email, msg.as_string())
        mailsender.quit()
        return f'Сообщение на адрес {email} отправлено, но может оказаться у человека в спаме!'
    except Exception as e:
        return f'error while mailing - {e}'

