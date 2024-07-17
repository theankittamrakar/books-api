"""CreateAuthorBookTable Migration."""

from masoniteorm.migrations import Migration


class CreateAuthorBookTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("author_book") as table:
            table.increments("id")
            table.unsigned_integer("author_id").index()
            table.foreign("author_id").references("id").on("authors")
            table.unsigned_integer("book_id").index()
            table.foreign("book_id").references("id").on("books")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("author_book")
