from app.jobs.SendMail import SendMail
from masonite.authentication import Auth
from masonite.controllers import Controller
from masonite.mail import Mail
from masonite.queues import Queue
from masonite.request import Request
from masonite.response import Response
from masonite.views import View


class RegisterController(Controller):
    def show(self, view: View):  # Show register page
        return view.render("auth.register")

    def store(
            self, auth: Auth, request: Request, response: Response, mail: Mail, queue: Queue
    ):  # store register user
        errors = request.validate(
            {
                "email": "required",
                "name": "required",
                "password": "required|confirmed",
            }
        )

        if errors:
            return response.back().with_errors(errors)

        user = auth.register(request.only("name", "email", "password"))
        # welcome_mailable = Welcome()
        # mail.mailable(welcome_mailable).send()
        queue.push(SendMail())
        if not user:
            return response.redirect("/register")

        return response.redirect("/home")
