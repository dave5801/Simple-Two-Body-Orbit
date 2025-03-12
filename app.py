from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Load trained model
model = tf.keras.models.load_model("orbit_model.h5")

@app.route("/")
def home():
    return "Welcome to the Enhanced Orbital Prediction API!"

@app.route("/predict", methods=["GET"])
def predict():
    try:
        # Get time input from query string
        time_value = float(request.args.get("time"))

        # Convert input to NumPy array for prediction
        input_data = np.array([[time_value]])

        # Predict (X, Y, Altitude, Velocity)
        predicted_output = model.predict(input_data)[0]

        # Extract predictions and convert to standard float format
        x_km = float(predicted_output[0])
        y_km = float(predicted_output[1])
        altitude_km = float(predicted_output[2])
        velocity_kms = float(predicted_output[3])

        return jsonify({
            "time (seconds)": time_value,
            "predicted_x (km)": x_km,
            "predicted_y (km)": y_km,
            "altitude (km)": altitude_km,
            "velocity (km/s)": velocity_kms
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
