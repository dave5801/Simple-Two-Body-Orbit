import numpy as np
import matplotlib.pyplot as plt

# Define orbital parameters
a = 5  # Semi-major axis
e = 0.6  # Eccentricity
b = a * np.sqrt(1 - e**2)  # Semi-minor axis

# Generate points using the parametric equations
E = np.linspace(0, 2 * np.pi, 500)  # Eccentric anomaly
x = a * (np.cos(E) - e)
y = b * np.sin(E)

# Plot the orbit
plt.figure(figsize=(6,6))
plt.plot(x, y, label="Elliptical Orbit")
plt.scatter([-e * a], [0], color='red', label="Focus (e.g., Sun)")

# Formatting the plot
plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
plt.axvline(0, color='gray', linestyle='--', linewidth=0.5)
plt.xlabel("X (AU)")
plt.ylabel("Y (AU)")
plt.legend()
plt.title("Elliptical Orbit Simulation")
plt.grid()
plt.axis("equal")  # Keep aspect ratio

plt.show()
