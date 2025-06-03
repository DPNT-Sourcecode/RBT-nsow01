import unittest
from approvaltests.approvals import verify

from solutions.RBT.rabbit_hole_solution import RabbitHoleSolution

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



if __name__ == '__main__':
    unittest.main()

