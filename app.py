from flask import Flask, render_template, jsonify, request

app = Flask(__name__)  # Create a Flask app instance

@app.route('/')  # Define a route for the home page
def home():
    return render_template('index.html')

@app.route("/button_click", methods=["POST"])
def button_click():
    return jsonify({"message": "Button Clicked! Data sent to Flask!"})

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode