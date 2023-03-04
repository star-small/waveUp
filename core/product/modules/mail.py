import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.utils import timezone
# Email parameters
to_addr = 'root@localhost'
cc_addr = 'top'
subject = 'Новая заявка'


def send_mail(data):

    # Create a MIME message object
    time = timezone.datetime.now().strftime("%m/%d/%Y %H:%M")
    msg = MIMEMultipart()
    msg['From'] = cc_addr
    msg['To'] = to_addr
    msg['Cc'] = cc_addr
    msg['Subject'] = subject
    # Add the body to the message
    body = f'Имя клиента: {data["name"]}\nДата: {time}\nНомер телефона: {data["phone"]}\nПочта: {data["email"]}\nАртикул: {data["vendor_code"]}\nКод товара: {data["code"]}\nНазвание товара: {data["product_name"]}'
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    # Connect to the SMTP server and send the message
    smtp_server = smtplib.SMTP('mail.novella-electric.kz')
    smtp_server.sendmail(cc_addr, [to_addr, cc_addr], msg.as_string())
    print(data, "mail")

    smtp_server.quit()
