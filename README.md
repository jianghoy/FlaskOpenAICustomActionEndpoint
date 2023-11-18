[![Run on Repl.it](https://replit.com/badge/github/jianghoy/FlaskOpenAICustomActionEndpoint)](https://replit.com/new/github/jianghoy/FlaskOpenAICustomActionEndpoint)

# Flask OpenAI Custom Action Endpoint
This is an example OpenAI custom action endpoint. What it does is hosting a web api for OpenAI GPTs to take it as custom action. The specific action here is a minimax tic-tac-toe algorithm, but you can simply swap it to anything you want. You can find the corresponding GPTs here: [Tic Tac Toe Game With Direct API](https://chat.openai.com/g/g-gLuNmwdjS-tic-tac-toe-game-with-direct-api-play)

# How to run the server
1. Install poetry: [documentation](https://python-poetry.org/docs/)
2. `poetry install` 
1. If you're using replit:
   1. First click the run on replit button.
   2. Click run button.
3. If you're not using replit: run`gunicorn -w=4 -b=0.0.0.0:80 main:app` command in console.

# How to setup OpenAI action
Once you get it running, under `your_url/docs` (if you're using replit, a web browser should automatic pop up), you can find a OpenAPI config, copy paste it to a text editor and do the following for this config:
1. **change `http` to `https` within that config**: replit serves as a reverse proxy, so it's using https for internet traffic.
2.  Add `"operationId": "your_id"` under  `"paths": -> "/human_move" -> "get"`: 
3.  (*To be researched*) Add `"x-openai-isConsequential:true` under  `"paths": -> "/human_move" -> "get"`: It seems OpenAI is using this flag to determine rest api call ([source](https://platform.openai.com/docs/actions/consequential-flag)*by the way I don't really understand what the doc means*)
4.  (To be researched) Update `"summary"` under api, add more description to prompt LLM to use the endpoint.

I didn't configure any authentication, so you can skip authentication there. You can also use `your_url/privacy` as a privacy document (for now it's simply a json).

# Misc
As of now, it seems GPTs doesn't work well with POST request for some reason. I would recommend use GET whenever possible.