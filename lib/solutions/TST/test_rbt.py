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
    # def test_three_rows_four_columns(self):
    #     warren = RabbitHoleSolution().rabbit_hole(3, 4, None, None)
    #
    #     self.assertEqual(warren, THREE_ROW_FOUR_COLUMN_WARREN)

    def test_zero_rows(self):
        warren = RabbitHoleSolution().rabbit_hole(0, 4, None, None)

        self.assertEqual("", warren)

    def test_one_row_one_column(self):
        warren = RabbitHoleSolution().rabbit_hole(1, 1, None, None)

        verify(warren)

    def test_one_row_two_column(self):
        warren = RabbitHoleSolution().rabbit_hole(1, 2, None, None)

        verify(warren)


if __name__ == '__main__':
    unittest.main()





