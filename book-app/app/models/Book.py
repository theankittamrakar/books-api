""" Book Model """

from masoniteorm.models import Model


class Book(Model):
    __fillable__ = ["title", "slug", "price"]
