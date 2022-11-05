from flask import Flask, jsonify, request, json
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




@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def home():
    if request.method == "POST":
        data = request.get_data()
        converted_data = json.loads(data.decode('utf-8'))
        operation_type = converted_data['operation_type']
        x = converted_data['x']
        y = converted_data['y']
        print(converted_data['operation_type'])
        if operation_type.lower() == "multiplication":
            print("Ujash")
            res = x * y
        elif operation_type.lower() == "addition":
            res = x + y
        elif operation_type.lower() == "subtraction":
            res = x - y
        
        return {"slackUsername": "Santana", 
                "result": res, 
                "operation_type": converted_data['operation_type']
                }
    return jsonify(payload)

if __name__ == "__main__":
    app.run()