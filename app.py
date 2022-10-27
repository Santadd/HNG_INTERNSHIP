from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


payload = { "slackUsername": "duahdivine1", 
           "backend": True, 
           "age": 25, 
           "bio": "I am a Backend Developer"
           }

@app.route('/')
def home():
    return jsonify(payload)

if __name__ == "__main__":
    app.run()