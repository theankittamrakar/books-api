from masonite.request import Request


class CorsMiddleware:
    """Cors Middleware."""

    def __init__(self, request: Request):
        """Inject Any Dependencies From The Service Container.
        Arguments:
            Request {masonite.request.Request} -- The Masonite request object
        """
        self.request = request

    def before(self):
        """Run This Middleware Before The Route Executes."""
        self.request.header('Access-Control-Allow-Origin', '*')

    def after(self):
        """Run This Middleware After The Route Executes."""
        pass