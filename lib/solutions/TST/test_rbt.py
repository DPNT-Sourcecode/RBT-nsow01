import unittest

from solutions.RBT.rabbit_hole_solution import RabbitHoleSolution

three_row_four_column_warren = """\
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
"""

class MyTestRabbitHole(unittest.TestCase):
    def test_something(self):
        warren = RabbitHoleSolution().rabbit_hole(3, 4)

        self.assertEqual(warren, three_row_four_column_warren)


if __name__ == '__main__':
    unittest.main()

