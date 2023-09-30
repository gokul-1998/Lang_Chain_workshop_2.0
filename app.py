from flask import Flask, request, render_template
from langchain.llms import OpenAI
from bot import Bot
from env import OPENAI_API_KEY

app = Flask(__name__)


@app.route("/")
def index():
  return render_template("chat.html")

@app.post("/chat")
def chat():
  question = request.json["question"]
  # llm = OpenAI(openai_api_key=OPENAI_API_KEY)
  # return llm.predict(question)
  return Bot.ask(question)


if __name__ == "__main__":
  app.run(port=5002, debug=True)