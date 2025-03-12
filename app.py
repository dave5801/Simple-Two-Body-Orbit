from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model("model.h5")

@app.route("/")
def home():
    return "Welcome to the Orbit Prediction API!"

@app.route("/predict", methods=["GET"])
def predict():
    try:
        # Get 'time' parameter from the URL query string (e.g., /predict?time=105)
        time_value = float(request.args.get("time"))

        # Convert input to a NumPy array for model prediction
        input_data = np.array([[time_value]])

        # Predict the orbital position
        predicted_position = model.predict(input_data)[0][0]

        # Return the prediction as JSON
        return jsonify({"time (seconds)": time_value, "predicted_position (km)": float(predicted_position)})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

