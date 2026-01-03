from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/submit', methods=['POST'])
def submit():
    # Read form fields sent from the Express-served HTML
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Do your processing here: save to DB, run logic, etc.
    print(f"Received: {name}, {email}, {message}")

    # For demo, just return JSON
    return jsonify({
        "status": "success",
        "data": {
            "name": name,
            "email": email,
            "message": message
        }
    }), 200

if __name__ == '__main__':
    app.run(port=5000, host = '0.0.0.0', debug=True)

