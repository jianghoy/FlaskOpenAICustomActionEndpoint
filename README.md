# What is this
This is an example OpenAI custom action endpoint. What it does is a stateless tick-tac-toe AI player.

# How to run
Right now I haven't figure out how to encorporate gunicorn to .replit yet, so I'm using the old fashioned `gunicorn -w=4 -b=0.0.0.0:80 main:app` command in linux.