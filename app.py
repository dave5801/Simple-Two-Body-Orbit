from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Load trained model
model = tf.keras.models.load_model("orbit_model.h5")

@app.route("/")
def home():
    return "Welcome to the Orbital Prediction API!"

@app.route("/predict", methods=["GET"])
def predict():
    try:
        # Get time input from query string
        time_value = float(request.args.get("time"))

        # Convert input to NumPy array for prediction
        input_data = np.array([[time_value]])

        # Predict (X, Y) position in km
        predicted_position = model.predict(input_data)[0]

        # Convert to Python float for JSON serialization
        x_km = float(predicted_position[0])
        y_km = float(predicted_position[1])

        return jsonify({
            "time (seconds)": time_value,
            "predicted_x (km)": x_km,
            "predicted_y (km)": y_km
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
