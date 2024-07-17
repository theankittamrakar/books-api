from app.mailables.Welcome import Welcome
from masonite.facades import Mail
from masonite.queues import Queueable


class SendMail(Queueable):
    # def __init__(self, user, email):
    #     self.user = user

    def handle(self):
        try:
            mail: Mail
            welcome_mailable = Welcome()
            Mail.mailable(welcome_mailable).send()
        except Exception as e:
            print(f"Error sending email: {e}")
