from apiflask import APIFlask, Schema
from apiflask.fields import List, String, Enum
from apiflask.validators import Length
from marshmallow.validate import OneOf
from game import TicTacToeAI
from flask_cors import CORS
from flask import request
import time

app = APIFlask(__name__)
CORS(app, supports_credentials=True, origins='*')
game = TicTacToeAI()


class BoardSchema(Schema):
  board = List(List(String(validate=Length(equal=1)),
                    validate=Length(equal=3)),
               validate=Length(equal=3),
               required=True)


class MoveResultSchema(BoardSchema):
  status = String(validate=OneOf(['end', 'continue', 'unknown']),
                  required=True)
  winner = String(validate=OneOf(['X', 'O', 'Draw', 'No winner']),
                  required=True)


class HumanMoveInput(Schema):
  position_1 = String(validate=OneOf(["X", "O", ""]), missing="")
  position_2 = String(validate=OneOf(["X", "O", ""]), missing="")
  position_3 = String(validate=OneOf(["X", "O", ""]), missing="")
  position_4 = String(validate=OneOf(["X", "O", ""]), missing="")
  position_5 = String(validate=OneOf(["X", "O", ""]), missing="")
  position_6 = String(validate=OneOf(["X", "O", ""]), missing="")
  position_7 = String(validate=OneOf(["X", "O", ""]), missing="")
  position_8 = String(validate=OneOf(["X", "O", ""]), missing="")
  position_9 = String(validate=OneOf(["X", "O", ""]), missing="")


# used for logging OpenAI request.
@app.before_request
def before_request_logging():
  print(request)
  print('Headers:\n', request.headers)
  print('Body:\n', request.get_data())
  print('\n')


@app.get('/human_move')
@app.input(HumanMoveInput, location='query')
def human_move(**positions):
  print('here is position variable')
  print(positions)
  positions = positions['query_data']
  board = [[
      positions["position_1"], positions["position_2"], positions["position_3"]
  ], [
      positions["position_4"], positions["position_5"], positions["position_6"]
  ], [
      positions["position_7"], positions["position_8"], positions["position_9"]
  ]]
  for row_index, row in enumerate(board):
    for col_index, cell in enumerate(row):
      if not cell:
        board[row_index][col_index] = " "
  print(board)
  # Process the board and perform any necessary actions
  try:
    response = game.human_move(board)
    return response
  except Exception as e:
    return {'error': str(e)}, 400


@app.get('/privacy')
def privacy():
  return {'disclaimer': "The app doesn't collect any user data"}


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
