
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
        return (horizontal_divider + "\n" + vertical_divider + "\n") * columns + horizontal_divider





