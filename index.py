from flask import Flask
app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:8080'

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
