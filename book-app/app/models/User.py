"""User Model."""
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin
from masonite.authentication import Authenticates


class User(Model, SoftDeletesMixin, Authenticates):
    """User Model."""

    __fillable__ = ["name", "email", "password", "is_admin"]
    __hidden__ = ["password"]
    __auth__ = "email"
