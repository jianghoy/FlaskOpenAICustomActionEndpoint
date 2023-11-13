import unittest
from game import TicTacToeAI

class TestHumanMove(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToeAI()

    def test_legal_move(self):
        new_board = [
            ["X", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        result = self.game.human_move(new_board)
        expected_status = 'continue'
        self.assertEqual(result['status'], expected_status)

    def test_win_move(self):
        new_board = [
            ["X", "X", " "],
            ["O", "O", " "],
            [" ", " ", " "]
        ]
        self.game.board = [
            ["X", "X", " "],
            ["O", "O", " "],
            [" ", " ", " "]
        ]
        self.game.human_move(new_board)
        print(self.game.board)
        winner = self.game.check_winner()
        print(winner)
        self.assertTrue(winner)
        self.assertEqual('O', winner)

    def test_draw_move(self):
        new_board = [
            ["X", "O", "X"],
            ["X", "X", "O"],
            ["O", "X", "O"]
        ]
        self.game.board = [
            ["X", "O", "X"],
            ["X", "X", "O"],
            ["O", " ", "O"]
        ]
        response = self.game.human_move(new_board)
        self.assertEqual(response['winner'], 'Draw')

    def test_invalid_board_length(self):
        new_board = [
            ["X", " ", " "],
            [" ", " ", " "]
        ]
        with self.assertRaises(ValueError):
            self.game.human_move(new_board)

    def test_invalid_board_sublength(self):
        new_board = [
            ["X", " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "]
        ]
        with self.assertRaises(ValueError):
            self.game.human_move(new_board)

    def test_invalid_board_value(self):
        new_board = [
            ["X", " ", " "],
            [" ", "Y", " "],  # Invalid value
            [" ", " ", " "]
        ]
        with self.assertRaises(ValueError):
            self.game.human_move(new_board)

if __name__ == '__main__':
    unittest.main()
