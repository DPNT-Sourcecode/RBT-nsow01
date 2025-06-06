import pprint

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

class EnteredFrom:
    TOP = "T"
    BOTTOM = "B"
    LEFT = "L"
    RIGHT = "R"
    NOT_ENTERED = "N"


class RouteMatrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self._rows_columns = [[EnteredFrom.NOT_ENTERED] * columns] * rows

    def start(self):
        self._rows_columns[0,0] = EnteredFrom.TOP

    def __str__(self):
        return "\n".join(" ".join(row) for row in self._rows_columns)


def dig_route(rows, columns, digging_moves):
    route = RouteMatrix(rows, columns)
    if digging_moves:
        route.start()
    return RouteMatrix(rows, columns)

