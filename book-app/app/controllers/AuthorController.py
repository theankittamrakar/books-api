from app.models.Author import Author
from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response


class AuthorController(Controller):
    def index(self, response: Response):
        authors = Author.all()
        return response.json({
            "data": authors.serialize()
        })

    def show(self, id, response: Response):
        author = self.get_author(id)
        if not author:
            return response.json({
                "message": "Author not found!"
            }, 404)

        return response.json({
            "data": author.serialize()
        })

    def store(self, request: Request, response: Response):
        errors = request.validate({
            'firstname': 'required|string',
            'middlename': 'string',
            'lastname': 'required|string'
        })

        if errors:
            return response.json({
                "message": "Data validation failed!",
                "errors": errors.all()
            }, 422)

        data = request.only('firstname', 'middlename', 'lastname')
        author = Author.create(data)
        return response.json({
            "data": author.serialize(),
            "message": "Author created successfully!"
        }, 201)

    def update(self, id, request: Request, response: Response):
        author = self.get_author(id)
        if not author:
            return response.json({
                "message": "Author not found!"
            }, 404)

        errors = request.validate({
            'firstname': 'required|string',
            'middlename': 'string',
            'lastname': 'required|string'
        })

        if errors:
            return response.json({
                "message": "Data validation failed!",
                "errors": errors.all()
            }, 422)

        data = request.only('firstname', 'middlename', 'lastname')
        author.update(data)

        return response.json({
            "data": author.serialize(),
            "message": "Author updated successfully!"
        }, 200)

    def destroy(self, id, request: Request, response: Response):
        author = self.get_author(id)
        if not author:
            return response.json({
                "message": "Author not found!"
            }, 404)

        author.delete()
        return response.json({
            "message": "Author deleted successfully!"
        }, 201)

    def get_author(self, id):
        return Author.find(id)
