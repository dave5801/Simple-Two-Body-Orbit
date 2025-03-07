from flask import Flask, render_template

app = Flask(__name__)  # Create a Flask app instance

@app.route('/')  # Define a route for the home page
def home():
    return render_template('index.html')

@app.route('/hello')  # Define another route
def hello():
    return "Hello, World!"

@app.route("/clicked")
def button_clicked():
    return "You clicked the button!"

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode