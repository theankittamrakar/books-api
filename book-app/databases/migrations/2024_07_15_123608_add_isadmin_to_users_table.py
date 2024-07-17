"""AddIsadminToUsersTable Migration."""

from masoniteorm.migrations import Migration


class AddIsadminToUsersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("users") as table:
            table.boolean('is_admin').default("false")

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("users") as table:
            table.drop_column('is_admin')
