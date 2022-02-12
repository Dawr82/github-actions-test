from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "<h1>Welcome to my website<\h1>"

@app.route("/data")
def api():
    return {
        "Name": "Dawid",
        "Surname": "Skorupa",
    }

@app.route("/faulty")
def faulty()
    return 0


if __name__ == "__main__":
    app.run()