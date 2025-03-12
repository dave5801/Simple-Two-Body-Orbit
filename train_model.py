import numpy as np
import tensorflow as tf

# Orbital parameters
semi_major_axis = 7000  # km (Earth radius + altitude)
eccentricity = 0.01  # Slightly elliptical orbit
orbital_period = 5800  # seconds (approximate)
mu = 398600  # km^3/s^2 (Earth's gravitational parameter)

# Generate time steps for one full orbit
time_steps = np.linspace(0, orbital_period, num=200)

# Compute Mean Anomaly (M)
mean_anomaly = 2 * np.pi * time_steps / orbital_period

# Approximate Eccentric Anomaly (E)
ecc_anomaly = mean_anomaly + eccentricity * np.sin(mean_anomaly)

# Compute True Anomaly (ν)
true_anomaly = 2 * np.arctan(
    np.sqrt((1 + eccentricity) / (1 - eccentricity)) * np.tan(ecc_anomaly / 2)
)

# Compute position in the orbital plane (radius)
radius = semi_major_axis * (1 - eccentricity**2) / (1 + eccentricity * np.cos(true_anomaly))

# Convert to Cartesian coordinates (X, Y)
x_positions = radius * np.cos(true_anomaly)
y_positions = radius * np.sin(true_anomaly)

# Compute altitude (radius above Earth surface)
earth_radius = 6378  # km
altitudes = radius - earth_radius  # km above Earth's surface

# Compute orbital velocity using Vis-viva equation: v = sqrt(mu * (2/r - 1/a))
velocities = np.sqrt(mu * (2 / radius - 1 / semi_major_axis))  # km/s

# Training data: input is time, output is (X, Y, Altitude, Velocity)
X_train = time_steps.reshape(-1, 1)
Y_train = np.column_stack((x_positions, y_positions, altitudes, velocities))

# Create and train the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(4)  # Output: X, Y, Altitude, Velocity
])

model.compile(optimizer='adam', loss='mse')
model.fit(X_train, Y_train, epochs=200, verbose=1)

# Save the updated model
model.save("orbit_model.h5")

print("Updated model saved as orbit_model.h5")
