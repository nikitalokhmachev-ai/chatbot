import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/message', methods=['POST'])
def process_message():
    
    content = request.json
    
    message = content['message']
    answer = {"response": "Hello, " + message}
    
    return jsonify(answer)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    #app.run(debug=True, host='localhost', port=int(os.environ.get('PORT', 8080)))