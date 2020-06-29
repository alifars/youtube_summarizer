
from flask import Flask, request
from bert_extractive_summary import *




app = Flask("__main__")

@app.route("/")
def home():
    return " working"


@app.route("/api/summarizer", methods=["GET", "POST"])
def api():
    video_id = request.args["video_id"]
    text = main(video_id)
    return text
if __name__ == "__main__":
    app.run()
