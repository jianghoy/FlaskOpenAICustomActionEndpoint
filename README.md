[![Run on Repl.it](https://replit.com/badge/github/jianghoy/FlaskOpenAICustomActionEndpoint)](https://replit.com/new/github/jianghoy/FlaskOpenAICustomActionEndpoint)

# What is this
This is an example OpenAI custom action endpoint. What it does is a stateless tick-tac-toe AI player. But the gaming functionality is not important; the APIFlask config and hosting on replit are.

# How to run the server
1. If you're using replit:
   1. First click the run on replit button.
   2. Click run button.
3. If you're not using replit:`gunicorn -w=4 -b=0.0.0.0:80 main:app` command in linux.

# How to setup OpenAI action
Under /docs, you can find a OpenAPI config, copy paste it to GPTs config panel. One thing worth noting is that, replit serves as a reverse proxy, so you need to change the OpenAPI config's `http` to `https`. You can find example connection here: 

# How to debug OpenAI action connection
Right now there's no good debugging for OpenAI connection. The code