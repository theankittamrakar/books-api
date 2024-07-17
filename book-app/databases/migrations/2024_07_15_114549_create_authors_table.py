"""CreateAuthorsTable Migration."""

from masoniteorm.migrations import Migration


class CreateAuthorsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("authors") as table:
            table.increments("id")
            table.string("firstname")
            table.string("middlename").nullable()
            table.string("lastname")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("authors")
