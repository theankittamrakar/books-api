"""AdminTableSeeder Seeder."""

from app.models.User import User
from masonite.facades.Hash import Hash
from masoniteorm.seeds import Seeder


class AdminTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        User.create({
            'name': "admin",
            'email': "admin@gmail.com",
            'password': Hash.make("admin"),
            'is_admin': True,
        })
