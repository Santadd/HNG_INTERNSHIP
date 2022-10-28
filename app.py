from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSON_SORT_KEYS'] = False



payload = { "slackUsername": "duahdivine1", 
           "backend": True, 
           "age": 25, 
           "bio": "I am a Backend Developer"
           }

@app.route('/')
@cross_origin()
def home():
    return jsonify(payload)

if __name__ == "__main__":
    app.run()