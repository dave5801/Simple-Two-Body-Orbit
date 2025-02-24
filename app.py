from flask import Flask

app = Flask(__name__)  # Create a Flask app instance

@app.route('/')  # Define a route for the home page
def home():
    return "Welcome to My Flask App!"

@app.route('/hello')  # Define another route
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode