import numpy as np
import tensorflow as tf

# Orbital parameters
semi_major_axis = 7000  # km (Earth radius + altitude)
eccentricity = 0.01  # Nearly circular orbit
orbital_period = 5800  # seconds (approximate for LEO)
mu = 398600  # km^3/s^2 (Earth's gravitational parameter)

# Generate time steps (one full orbit)
time_steps = np.linspace(0, orbital_period, num=100)

# Solve for Mean Anomaly (M) using Kepler's equation
mean_anomaly = 2 * np.pi * time_steps / orbital_period

# Approximate Eccentric Anomaly (E)
ecc_anomaly = mean_anomaly + eccentricity * np.sin(mean_anomaly)

# Compute true anomaly (ν)
true_anomaly = 2 * np.arctan(
    np.sqrt((1 + eccentricity) / (1 - eccentricity)) * np.tan(ecc_anomaly / 2)
)

# Compute position in the orbital plane (radius)
radius = semi_major_axis * (1 - eccentricity**2) / (1 + eccentricity * np.cos(true_anomaly))

# Convert to Cartesian (X, Y) assuming orbit in the XY plane
x_positions = radius * np.cos(true_anomaly)
y_positions = radius * np.sin(true_anomaly)

# Training data: input is time, output is (X, Y)
X_train = time_steps.reshape(-1, 1)
Y_train = np.column_stack((x_positions, y_positions))

# Create and train the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(2)  # Output (X, Y) coordinates
])

model.compile(optimizer='adam', loss='mse')
model.fit(X_train, Y_train, epochs=100, verbose=1)

# Save model
model.save("orbit_model.h5")

print("Model saved as orbit_model.h5")
