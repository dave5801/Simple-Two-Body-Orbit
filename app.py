from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clicks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Define Database Model
class Click(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Create Database Tables
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/button_click", methods=["POST"])
def button_click():
    data = request.get_json()
    name = data.get("name", "Anonymous")

    # Store the click in the database
    new_click = Click(name=name)
    db.session.add(new_click)
    db.session.commit()

    return jsonify({"message": f"Button clicked by {name}!"})

@app.route("/clicks")
def get_clicks():
    clicks = Click.query.all()
    click_list = [{"id": c.id, "name": c.name, "timestamp": c.timestamp.strftime("%Y-%m-%d %H:%M:%S")} for c in clicks]
    return jsonify(click_list)

if __name__ == "__main__":
    app.run(debug=True)
