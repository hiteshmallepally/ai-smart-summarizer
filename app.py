from flask import Flask, render_template_string
import os

app = Flask(__name__)

html = open("index.html").read()

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
