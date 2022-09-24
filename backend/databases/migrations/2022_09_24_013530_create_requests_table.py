"""CreateRequestsTable Migration."""

from masoniteorm.migrations import Migration


class CreateRequestsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("requests") as table:
            table.increments("id")
            table.float("predit")
            table.jsonb("input_json")
            table.jsonb("output_json")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("requests")
