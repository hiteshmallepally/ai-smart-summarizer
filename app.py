from flask import Flask, render_template_string

app = Flask(__name__)

html = open("index.html").read()

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)