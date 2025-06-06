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

    def test_second_move_to_right(self):
        warren = RabbitHoleSolution().rabbit_hole(1, 2, "DR", None)
        verify(warren)

    def test_second_move_down(self):
        warren = RabbitHoleSolution().rabbit_hole(2, 1, "DD", None)
        verify(warren)

    def test_diging_up(self):
        warren = RabbitHoleSolution().rabbit_hole(2, 2, "DDRU", None)
        verify(warren)

    def test_diging_left(self):
        warren = RabbitHoleSolution().rabbit_hole(2, 2, "DRDL", None)
        verify(warren)

    def test_diging_DRDLDRRUURDD(self):
        warren = RabbitHoleSolution().rabbit_hole(3, 4, "DRDLDRRUURDD", None)
        verify(warren)

    def test_fully_dug_2x2(self):
        warren = RabbitHoleSolution().rabbit_hole(2, 2, "DRDLU", None)
        verify(warren)

    def test_fully_room_in_dug_4x4(self):
        warren = RabbitHoleSolution().rabbit_hole(4, 4, "DDRRDLULU", None)
        verify(warren)

    def test_large_room_in_dug_5x5(self):
        warren = RabbitHoleSolution().rabbit_hole(5, 5, "DDDRULDRRULDRRULD", None)
        verify(warren)

    def test_explicit_scaling_at_default_levels(self):
        rendering_options = {"HORIZONTAL_SCALE": "3", "VERTICAL_SCALE": "1"}
        warren = RabbitHoleSolution().rabbit_hole(3, 4, "DRDLDRRUURDD", rendering_options)
        verify(warren)

    def test_explicit_scaling_at_larger_levels(self):
        rendering_options = {"HORIZONTAL_SCALE": "6", "VERTICAL_SCALE": "2"}
        warren = RabbitHoleSolution().rabbit_hole(3, 4, "DRDLDRRUURDD", rendering_options)
        verify(warren)

    def test_unicode_theme(self):
        rendering_options = {"HORIZONTAL_SCALE": "3", "VERTICAL_SCALE": "1", "RENDERING_THEME": "UNICODE"}
        warren = RabbitHoleSolution().rabbit_hole(3, 4, "DRDLDRRUURDD", rendering_options)
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

    def test_3x4_DRDLDRRUURDD(self):
        route_matrix = dig_route(rows=3, columns=4, digging_moves="DRDLDRRUURDD")
        verify(route_matrix)

    def test_3x1_DDD(self):
        route_matrix = dig_route(rows=3, columns=1, digging_moves="DDD")
        verify(route_matrix)

    def test_2x2_loop(self):
        warren = dig_route(rows=2, columns=2, digging_moves="DRDLU")
        verify(warren)

if __name__ == '__main__':
    unittest.main()

