import numpy as np
import matplotlib.pyplot as plt

def plot_emission_amplitude_with_conditions(x0, gamma, omega0, t_max=10, num_points=1000):
    """
    Plots the amplitude of emitted electromagnetic radiation as a function of time
    with additional initial conditions x(0) = x0 and x'(0) = 0.

    Args:
        x0 (float): Initial value of x.
        gamma (float): Value of gamma.
        omega0 (float): Value of omega.
        t_max (float, optional): Maximum value of time (t). Defaults to 10.
        num_points (int, optional): Number of points for generating t values. Defaults to 1000.
    """
    # Calculate the constant A to satisfy the initial conditions
    A = x0

    t = np.linspace(0, t_max, num_points)
    x_t = A * np.exp(-gamma/2 * t) * np.cos(omega0 * t)

    plt.figure(figsize=(8, 6))
    plt.plot(t, x_t, label='$x(t) = x_0 e^{-\\frac{\\gamma}{2} t} \\cos(\\omega_0 t)$')
    plt.xlabel('Time (t)')
    plt.ylabel('Amplitude of Emission')
    plt.title('Amplitude of Emitted Electromagnetic Radiation vs. Time with Initial Conditions')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage:
x0 = 1.0
gamma = 0.5
omega0 = 2.0
plot_emission_amplitude_with_conditions(x0, gamma, omega0)
