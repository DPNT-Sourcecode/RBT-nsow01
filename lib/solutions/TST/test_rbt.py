import unittest
from approvaltests.approvals import verify

from solutions.RBT.rabbit_hole_solution import RabbitHoleSolution, dig_route

THREE_ROW_FOUR_COLUMN_WARREN = """\
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+"""


class MyTestRabbitHole(unittest.TestCase):
    def test_undug_three_rows_four_columns(self):
        warren = RabbitHoleSolution().rabbit_hole(3, 4, "", None)

        self.assertEqual(warren, THREE_ROW_FOUR_COLUMN_WARREN)

    def test_undug_zero_rows(self):
        warren = RabbitHoleSolution().rabbit_hole(0, 4, "", None)

        self.assertEqual("", warren)

    def test_undug_one_row_one_column(self):
        warren = RabbitHoleSolution().rabbit_hole(1, 1, "", None)

        verify(warren)

    def test_undug_one_row_two_column(self):
        warren = RabbitHoleSolution().rabbit_hole(1, 2, "", None)

        verify(warren)

    def test_undug_two_rows_one_column(self):
        warren = RabbitHoleSolution().rabbit_hole(2, 1, "", None)

        verify(warren)

    def test_first_dig(self):
        warren = RabbitHoleSolution().rabbit_hole(2, 1, "D", None)

        verify(warren)


class TestDigRoute(unittest.TestCase):
    def test_no_dig(self):
        route_matrix = dig_route(rows=3, columns=2, digging_moves="")
        verify(route_matrix)

    def test_first_move(self):
        route_matrix = dig_route(rows=3, columns=2, digging_moves="D")
        verify(route_matrix)

    def test_second_move(self):
        route_matrix = dig_route(rows=3, columns=2, digging_moves="DR")
        verify(route_matrix)


if __name__ == '__main__':
    unittest.main()


