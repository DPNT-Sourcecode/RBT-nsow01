from dataclasses import dataclass
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
        route = dig_route(rows, columns, digging_moves)

        warren = ""
        for row_index in range(rows):
            horizontal_divider = ""
            for column_index in range(route.columns):
                if route.cell(row_index, column_index) == EnteredFrom.TOP or (
                        row_index > 0 and route.cell(row_index - 1, column_index) == EnteredFrom.BOTTOM):
                    horizontal_divider += "+   "
                else:
                    horizontal_divider += "+---"
            horizontal_divider += "+"

            vertical_divider = ""
            for column_index in range(route.columns):
                if route.cell(row_index, column_index) == EnteredFrom.LEFT or (
                    column_index > 0 and route.cell(row_index, column_index - 1) == EnteredFrom.RIGHT
                ):
                    vertical_divider += "    "
                else:
                    vertical_divider += "|   "
            vertical_divider += "|"
            warren += horizontal_divider + "\n" + vertical_divider + "\n"

        solid_horizontal_divider = "+---" * columns + "+"
        return warren + solid_horizontal_divider

class EnteredFrom:
    TOP = "↑"
    BOTTOM = "↓"
    LEFT = "←"
    RIGHT = "→"
    NOT_ENTERED = "o"


@dataclass
class Location:
    row: int = 0
    column: int = 0


class RouteMatrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self._rows_columns = [[EnteredFrom.NOT_ENTERED for _ in range(columns)] for _ in range(rows)]

    def start(self):
        self._rows_columns[0][0] = EnteredFrom.TOP
        self._location = Location(0, 0)

    def cell(self, row_index, column_index):
        return self._rows_columns[row_index][column_index]

    def move(self, direction):
        if direction == "R":
            self._location.column += 1
            enter_into_new_cell_from = EnteredFrom.LEFT
        elif direction == "L":
            self._location.column -= 1
            enter_into_new_cell_from = EnteredFrom.RIGHT
        elif direction == "U":
            self._location.row -= 1
            enter_into_new_cell_from = EnteredFrom.BOTTOM
        elif direction == "D":
            self._location.row += 1
            enter_into_new_cell_from = EnteredFrom.TOP
        else:
            raise ValueError("Invalid direction")

        self._rows_columns[self._location.row][self._location.column] = enter_into_new_cell_from

    def __str__(self):
        return "\n".join(" ".join(row) for row in self._rows_columns)


def dig_route(rows, columns, digging_moves):
    route = RouteMatrix(rows, columns)
    if digging_moves:
        route.start()
        for direction in digging_moves[1:]:
            route.move(direction)
    return route




