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
  winner = String(validate=OneOf(['X', 'O', 'Draw', None]), allow_none=True)


# used for logging OpenAI request.
@app.before_request
def before_request_logging():
  print(request)
  print('Headers:\n', request.headers)
  print('Body:\n', request.get_data())
  print('\n')


@app.route('/human_move', methods=['POST'])
@app.input(BoardSchema)
@app.output(MoveResultSchema)
def human_move(json_data):
  try:
    response = game.human_move(json_data['board'])
    return response
  except Exception as e:
    return {'error': str(e)}, 400


@app.get('/privacy')
def privacy():
  return {'disclaimer': "The app doesn't collect any user data"}


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
