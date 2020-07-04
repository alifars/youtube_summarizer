from flask import Flask, request, render_template, jsonify
from bert_extractive_summary import *




app = Flask("__main__")

def parse(url):
    # https://www.youtube.com/watch?v=7DIcxavnF2k
    return url.split("?v=")[1]

@app.route("/")
def home():
    return render_template("home.html")


@app.route('/background_process')
def background_process():
    try:
        url = request.args.get('url', 0, type=str)
        print(url)
        video_id = parse(url)
        print(video_id)
        summary  = main(video_id)
        print(summary)
        
        return jsonify(result=summary)
    except Exception as e:
        return str(e)

@app.route("/api/summarizer", methods=["GET", "POST"])
def api():
    video_id = request.args["video_id"]
    text = main(video_id)
    return text
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000)
