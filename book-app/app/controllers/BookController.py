from app.models.Book import Book
from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response


class BookController(Controller):
    def index(self, response: Response):
        books = Book.all()
        return response.json({
            "data": books.serialize()
        })

    def show(self, id, response: Response):
        book = self.get_book(id)
        if not book:
            return response.json({
                "message": "Book not found!"
            }, 404)

        return response.json({
            "data": book.serialize()
        })

    def store(self, request: Request, response: Response):
        errors = request.validate({
            'title': 'required|string',
            'slug': 'string',
            'price': 'required|numeric'
        })

        if errors:
            return response.json({
                "message": "Data validation failed!",
                "errors": errors.all()
            }, 422)

        data = request.only('title', 'slug', 'price')
        book = Book.create(data)
        return response.json({
            "data": book.serialize(),
            "message": "Book created successfully!"
        }, 201)

    def update(self, id, request: Request, response: Response):
        book = self.get_book(id)

        if not book:
            return response.json({
                "message": "Book not found!"
            }, 404)
        errors = request.validate({
            'title': 'required|string',
            'slug': 'string',
            'price': 'required|numeric'
        })

        if errors:
            return response.json({
                "message": "Data validation failed!",
                "errors": errors.all()
            }, 422)

        data = request.only('title', 'slug', 'price')
        book.update(data)

        return response.json({
            "data": book.serialize(),
            "message": "Book updated successfully!"
        }, 200)

    def destroy(self, id, request: Request, response: Response):
        book = self.get_book(id)
        if not book:
            return response.json({
                "message": "Book not found!"
            }, 404)
        book.delete()

        return response.json({
            "message": "Book deleted successfully!"
        }, 201)

    def get_book(self, id):
        return Book.find(id)
