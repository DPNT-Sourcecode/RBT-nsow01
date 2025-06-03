
THREE_ROW_FOUR_COLUMN_WARREN = """\
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+"""

class RabbitHoleSolution:

    def rabbit_hole(self, rows, columns, digging_moves, rendering_options):
        if not rows or not columns:
            return ""
        horizontal_divider = "+---" * columns + "+"
        vertical_divider = "|   " * columns + "|"
        return (horizontal_divider + "\n" + vertical_divider + "\n") * rows + horizontal_divider

class RouteMatrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self._list_of_lists = [[0] * columns] * columns

    def __str__(self):
        pprint.pformat(self.rows)

def dig_route(rows, columns, digging_moves):
    return


