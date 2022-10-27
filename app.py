from flask import Flask


app = Flask(__name__)

payload = { "slackUsername": "Santana", "backend": True, "age": 25, "bio": "It is well" }

@app.route('/')
def home():
    return payload





if __name__ == "__main__":
    app.run(debug=True)