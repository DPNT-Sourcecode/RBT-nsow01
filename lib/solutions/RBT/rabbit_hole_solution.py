
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
        if not rows or columns:
            return ""
        horizontal_divider = "+---" + "+"
        vertical_divider = "|   " + "|"
        return horizontal_divider + "\n" + vertical_divider + "\n" + horizontal_divider



