from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "<h1>Welcome to my website<\h1>"

if __name__ == "__main__":
    app.run()