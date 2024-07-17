from app.models.User import User
from masonite.facades.Hash import Hash
from masoniteorm import Factory


def user_factory(faker):
    return {
        'name': faker.name(),
        'email': faker.email(),
        'password': Hash.make("secret"),
        'is_admin': faker.boolean(),
    }


Factory.register(User, user_factory)
