import numpy as np
import matplotlib.pyplot as plt

class Orbit:
    def __init__(self, semi_major_axis, eccentricity):
        self.semi_major_axis = semi_major_axis
        self.eccentricity = eccentricity

    def get_position(self, true_anomaly):
        # Calculate the distance from the focus to the body
        r = (self.semi_major_axis * (1 - self.eccentricity**2)) / (1 + self.eccentricity * np.cos(true_anomaly))
        x = r * np.cos(true_anomaly)
        y = r * np.sin(true_anomaly)
        return x, y
    
    def plot_orbit(self, num_points=100):
        true_anomalies = np.linspace(0, 2 * np.pi, num_points)
        positions = [self.get_position(ta) for ta in true_anomalies]
        x, y = zip(*positions)

        plt.figure(figsize=(6, 6))
        plt.plot(x, y, label="Orbit Path")
        plt.scatter([0], [0], color='red', label="Focus (e.g., Sun)")
        plt.title("Orbit Simulation")
        plt.xlabel("X (AU)")
        plt.ylabel("Y (AU)")
        plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
        plt.axvline(0, color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.grid()
        plt.axis("equal")
        plt.show()

if __name__ == '__main__':
    # This block is executed when the script is run directly
    # Define orbital parameters
    a = 5  # Semi-major axis
    e = 0.6  # Eccentricity
    b = a * np.sqrt(1 - e**2)  # Semi-minor axis
    # Create an instance of the Orbit class
    orbit = Orbit(semi_major_axis=a, eccentricity=e)
    orbit.plot_orbit(num_points=1000)

    print("Simple two-body orbit simulation completed.")