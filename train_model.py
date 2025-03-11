import tensorflow as tf
import numpy as np

# Generate sample orbital data
time_steps = np.linspace(0, 100, num=100)
positions = np.sin(time_steps)  # Simulating an orbital motion

# Build the TensorFlow model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)  # Predicting next position
])

model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(time_steps, positions, epochs=100, verbose=1)

# Save the trained model
model.save("model.h5")

print("Model saved as model.h5")
