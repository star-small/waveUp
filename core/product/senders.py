from django.utils import timezone

from pathlib import Path
from dotenv import load_dotenv
import telebot
import os
import collections
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


load_dotenv("/etc/environment")


class Sender:

    def __init__(self, data):
        self._time = None
        self.data = data
        self.base_dir = Path(__file__).resolve().parent.parent.parent
        self.message_body = f'Имя клиента: {self.data["name"]}\nДата: {self.time}\nНомер телефона: {self.data["phone"]}\nПочта: {self.data["email"]}\nАртикул: {self.data.get("vendor_code", "N/A")}\nКод товара: {self.data.get("code", "N/A")}\nНазвание товара: {self.data.get("product_name", "N/A")}'

    def send():
        raise NotImplementedError(
            "Метод send должен быть переопределен в дочерних классах."
        )

    @property
    def time(self):
        self._time = timezone.datetime.now().strftime("%m/%d/%Y %H:%M")
        return self._time


class TelegramSender(Sender):

    def __init__(self, data):
        super().__init__(data)
        self.message_body = f'Имя клиента: {self.data["name"]}\nДата: {self.time}\nНомер телефона: {self.data["phone"]}\nПочта: {self.data["email"]}'

    def send(self):
        API_TOKEN = os.getenv("API_TOKEN")
        CHANNEL_ID = os.getenv("MANAGER_CHANNEL_ID")
        bot = telebot.TeleBot(API_TOKEN)
        bot.send_message(CHANNEL_ID, self.message_body)


class MailSender(Sender):

    def send(self):
        # Create a MIME message object
        to_addr = "root@localhost"
        cc_addr = "top"
        subject = "Новая заявка"
        msg = MIMEMultipart()
        msg["From"] = cc_addr
        msg["To"] = to_addr
        msg["Cc"] = cc_addr
        msg["Subject"] = subject
        # Add the body to the message
        msg.attach(MIMEText(self.message_body, "plain", "utf-8"))

        # Connect to the SMTP server and send the message
        smtp_server = smtplib.SMTP("mail.novella-electric.kz")
        smtp_server.sendmail(cc_addr, [to_addr, cc_addr], msg.as_string())
        smtp_server.quit()


class GoogleSheetSender(Sender):

    def send(self):
        tb = Table()
        tb.load_data(self.data, self.time)


class AllSender(Sender):

    def send(self):
        # Выполнение метода send() у всех дочерних классов Sender
        for cls in Sender.__subclasses__()[:-1]:
            obj = cls(self.data)
            obj.send()


if __name__ == "__main__":
    from modules.sheets import Table

    data = {
        "name": "John Doe",
        "phone": "123456789",
        "email": "top@mail.novella-electric.kz",
        "vendor_code": "12345",
        "code": "54321",
        "product_name": "Sample Product",
    }
    sender = AllSender(data)
    sender.send()
else:
    from .modules.sheets import Table
