[![Run on Repl.it](https://replit.com/badge/github/jianghoy/FlaskOpenAICustomActionEndpoint)](https://replit.com/new/github/jianghoy/FlaskOpenAICustomActionEndpoint)

# Flask OpenAI Custom Action Endpoint
This is an example OpenAI custom action endpoint. What it does is hosting a web api for OpenAI GPTs to take it as custom action. The specific action here is a minimax tic-tac-toe algorithm, but you can simply swap it to anything you want.

# How to run the server
1. If you're using replit:
   1. First click the run on replit button.
   2. Click run button.
3. If you're not using replit: run`gunicorn -w=4 -b=0.0.0.0:80 main:app` command in console.

# How to setup OpenAI action
Once you get it running, under `your_url/docs` (if you're using replit, a web browser should automatic pop up), you can find a OpenAPI config, copy paste it to a text editor and do the following for this config:
1. **change `http` to `https` within that config**: replit serves as a reverse proxy, so it's using https for internet traffic.
2.  Add `"operationId": "your_id"` under  `"paths": -> "/human_move" -> "post"`: **everytime you make update on your OpenAPI config, increase operationId by 1** because this is the only way to keep track of OpenAI action update status. You'll thank me later
3.  (*To be researched*) Add `"x-openai-isConsequential:true` under  `"paths": -> "/human_move" -> "post"`: It seems OpenAI is using this flag to determine rest api call ([source](https://platform.openai.com/docs/actions/consequential-flag)*by the way I don't really understand what the doc means*)
4.  (To be researched) Update `"summary"` under api, add more description to prompt LLM to use the endpoint.

I didn't configure any authentication, so you can skip authentication there. You can also use `your_url/privacy` as a privacy document (for now it's simply a json).

# How to debug OpenAI action connection
Right now there's no good debugging for OpenAI connection. One thing I did is to print the request in console. And you can track what OpenAI sends to the endpoint. Another thing that I found useful is that OpenAI UI doesn't really tell if your latest config got saved, so you want to increase your operationId (see above) to kepp track of it.