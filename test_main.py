from main import Player
from main import evalute_winner
import unittest


class Testing(unittest.TestCase):

    def test_evalute_winner(self):
        e = evalute_winner("rock", "rock")
        self.assertEqual(e, "draw")

        e = evalute_winner("rock", "paper")
        self.assertEqual(e, "paper")

if __name__ == '__main__':
    unittest.main()
