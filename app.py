import matplotlib
matplotlib.use('Agg')  # Set non-GUI backend before importing pyplot
import matplotlib.pyplot as plt
from flask import Flask, request, jsonify, send_file
import tensorflow as tf
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import os  # Import os to handle file directories

app = Flask(__name__)

# Load trained model
model = tf.keras.models.load_model("orbit_model.h5")

@app.route("/")
def home():
    return "Welcome to the Orbital Prediction API with 3D Tracking!"

@app.route("/predict", methods=["GET"])
def predict():
    try:
        time_value = float(request.args.get("time"))
        input_data = np.array([[time_value]])
        predicted_output = model.predict(input_data)[0]

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


@app.route("/orbit_plot", methods=["GET"])
def orbit_plot():
    try:

        # Ensure the 'static' directory exists
        static_dir = "static"
        if not os.path.exists(static_dir):
            os.makedirs(static_dir)  # Create 'static' directory if missing

        # Generate orbit points
        time_steps = np.linspace(0, 5800, num=300)  # Covering one full orbit
        input_data = time_steps.reshape(-1, 1)
        predictions = model.predict(input_data)

        x_positions = predictions[:, 0]
        y_positions = predictions[:, 1]
        altitudes = predictions[:, 2]

        # Convert altitude to Z-axis (assuming simple circular motion)
        z_positions = altitudes

        # Create 3D plot
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection="3d")

        ax.plot(x_positions, y_positions, z_positions, label="Orbital Path", color="blue")
        ax.scatter([0], [0], [0], color="red", s=100, label="Earth (Center)")

        ax.set_xlabel("X Position (km)")
        ax.set_ylabel("Y Position (km)")
        ax.set_zlabel("Altitude (km)")
        ax.set_title("3D Orbital Trajectory")
        ax.legend()

        # Save plot to file
        plot_path = "static/orbit_plot.png"
        plt.savefig(plot_path)
        plt.close()

        return send_file(plot_path, mimetype="image/png")

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
