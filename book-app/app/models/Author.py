""" Author Model """

from masoniteorm.models import Model


class Author(Model):
    __fillable__ = ["firstname", "middlename", "lastname"]
