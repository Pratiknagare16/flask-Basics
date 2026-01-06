from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return "HELLO PRATIK ! This is my Flask App"

@app.route("/about")

def about():
    return "<h1>Hello Flask!</h1><p>This is HTML</p>"

@app.route("/about")

def abouttt():
    return "This is the about page"

if __name__ == '__main__':
    app.run(debug=True)