from app.mailables.Welcome import Welcome
from masonite.controllers import Controller
from masonite.mail import Mail
from masonite.views import View


class MailController(Controller):
    def index(self, mail: Mail):
        welcome_mailable = Welcome()
        mail.mailable(welcome_mailable).send()
