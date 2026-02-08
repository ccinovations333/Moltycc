from flask import Flask, request
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Input validation function
def validate_input(data):
    if not isinstance(data, dict):
        raise BadRequest("Invalid input data")
    if 'name' not in data or not data['name']:
        raise BadRequest("'name' is required")

# Example secure bot logic
@app.route('/secure-bot', methods=['POST'])
def secure_bot():
    data = request.get_json()
    validate_input(data)
    # Implement secure logic here
    return {'status': 'success', 'data': data}, 200

if __name__ == '__main__':
    app.run(debug=True)