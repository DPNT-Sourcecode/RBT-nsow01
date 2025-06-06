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

        if rendering_options is None:
            rendering_options = {}

        horizontal_scale = int(rendering_options.get("HORIZONTAL_SCALE", "3"))
        vertical_scale = int(rendering_options.get("VERTICAL_SCALE", "1"))
        rendering_theme = rendering_options.get("RENDERING_THEME", "ASCII")
        if rendering_theme == "UNICODE":
            components = UnicodeComponents
        else:
            components = AsciiComponents

        warren = ""
        for row_index in range(rows):
            horizontal_divider = ""
            for column_index in range(route.columns):
                if route.no_walls_touch_top_left(row_index, column_index):
                    horizontal_divider += " " * (horizontal_scale + 1)
                elif route.has_tunnelling_at_top_of_cell(row_index, column_index):
                    horizontal_divider += "+" + " " * horizontal_scale
                else:
                    horizontal_divider += "+" + components.horizontal_wall * horizontal_scale

            horizontal_divider += "+"

            vertical_divider = ""
            for column_index in range(route.columns):
                if route.has_tunnelling_at_left_of_cell(row_index, column_index):
                    vertical_divider += " " * (horizontal_scale + 1)
                else:
                    vertical_divider += components.vertical_wall + " " * horizontal_scale
            vertical_divider += components.vertical_wall
            warren += horizontal_divider + "\n" + (vertical_divider + "\n") * vertical_scale

        solid_horizontal_divider = ("+" + components.horizontal_wall * horizontal_scale) * columns + "+"
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


class Plan:
    def __init__(self, rows, columns):
        self._rows_columns = [[[] for _ in range(columns+1)] for _ in range(rows+1)]
        self._row_max_index = rows
        self._column_max_index = columns

    def cell(self, row_index, column_index):
        return self._rows_columns[row_index][column_index]

    def __str__(self):
        return "\n".join(" ".join(cell for cell in row) for row in self._rows_columns)


class RouteMatrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self._rows_columns = [[[] for _ in range(columns)] for _ in range(rows)]

    def start(self):
        self._rows_columns[0][0].append(EnteredFrom.TOP)
        self._location = Location(0, 0)

    def cell(self, row_index, column_index):
        return self._rows_columns[row_index][column_index]

    def cell_below(self, row_index, column_index):
        return self.cell(row_index - 1, column_index)

    def cell_to_left(self, row_index, column_index):
        return self.cell(row_index, column_index - 1)

    def cell_to_right(self, row_index, column_index):
        return self.cell(row_index, column_index + 1)

    def is_top_left_corner(self, row_index, column_index):
        return row_index == 0 and column_index == 0

    def has_row_above(self, row_index):
        return row_index > 0

    def has_column_to_left(self, column_index):
        return column_index > 0

    def has_column_to_right(self, column_index):
        return column_index < self.columns - 1

    def has_tunnelling_at_top_of_cell(self, row_index, column_index):
        return EnteredFrom.TOP in self.cell(row_index, column_index) or (
                self.has_row_above(row_index) and EnteredFrom.BOTTOM in self.cell_below(row_index, column_index))

    def has_tunnelling_at_left_of_cell(self, row_index, column_index):
        return EnteredFrom.LEFT in self.cell(row_index, column_index) or (
                self.has_column_to_left(column_index)
                and EnteredFrom.RIGHT in self.cell_to_left(row_index, column_index))

    def no_walls_touch_top_left(self, row_index, column_index):
        return (
                self.has_tunnelling_at_left_of_cell(row_index, column_index)
                and self.has_row_above(row_index)
                and self.has_tunnelling_at_left_of_cell(row_index - 1, column_index)
                and self.has_tunnelling_at_top_of_cell(row_index, column_index)
                and self.has_column_to_left(column_index)
                and self.has_tunnelling_at_top_of_cell(row_index, column_index - 1)
        )

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

        self._rows_columns[self._location.row][self._location.column].append(enter_into_new_cell_from)

    def __str__(self):
        def format_cell(directions_list):
            return "".join(directions_list).ljust(4)
        return "\n".join(" ".join(format_cell(cell) for cell in row) for row in self._rows_columns)


class AsciiComponents:
    horizontal_wall = "-"
    vertical_wall = "|"
    top_left_corner = "+"


class UnicodeComponents:
    horizontal_wall = "━"
    vertical_wall = "┃"
    top_left_corner = "┏"


def dig_route(rows, columns, digging_moves):
    route = RouteMatrix(rows, columns)
    if digging_moves:
        route.start()
        for direction in digging_moves[1:]:
            route.move(direction)
    return route


