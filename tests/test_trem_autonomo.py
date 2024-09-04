import unittest
from src.trem_autonomo import Train

class TestTrain(unittest.TestCase):

    def setUp(self):
        self.train = Train()

    def test_move_right(self):
        self.assertEqual(self.train.move(["DIREITA", "DIREITA"]), 2)

    def test_move_left(self):
        self.assertEqual(self.train.move(["ESQUERDA"]), -1)

    def test_mixed_moves(self):
        commands = ["ESQUERDA", "DIREITA", "DIREITA", "DIREITA", "DIREITA", "ESQUERDA"]
        self.assertEqual(self.train.move(commands), 2)

    def test_invalid_command(self):
        with self.assertRaises(ValueError):
            self.train.move(["UP"])

    def test_consecutive_moves_limit(self):
        commands = ["DIREITA"] * 21
        self.assertEqual(self.train.move(commands), 20)

if __name__ == '__main__':
    unittest.main()
