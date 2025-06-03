import unittest
from approvaltests.approvals import verify

from solutions.RBT.rabbit_hole_solution import RabbitHoleSolution

ONE_ROW_ONE_COLUMN_WARREN = """\
+---+
|   |
+---+"""

ONE_ROW_TWO_COLUMN_WARREN = """\
+---+---+
|   |   |
+---+---+"""

THREE_ROW_FOUR_COLUMN_WARREN = """\
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+"""


class MyTestRabbitHole(unittest.TestCase):
    # def test_three_rows_four_columns(self):
    #     warren = RabbitHoleSolution().rabbit_hole(3, 4, None, None)
    #
    #     self.assertEqual(warren, THREE_ROW_FOUR_COLUMN_WARREN)

    def test_zero_rows(self):
        warren = RabbitHoleSolution().rabbit_hole(0, 4, None, None)

        self.assertEqual("", warren)

    def test_one_row_one_column(self):
        warren = RabbitHoleSolution().rabbit_hole(1, 1, None, None)

        self.assertEqual(ONE_ROW_ONE_COLUMN_WARREN, warren)

    def test_one_row_two_column(self):
        warren = RabbitHoleSolution().rabbit_hole(1, 1, None, None)

        verify(ONE_ROW_TWO_COLUMN_WARREN, warren)


if __name__ == '__main__':
    unittest.main()




