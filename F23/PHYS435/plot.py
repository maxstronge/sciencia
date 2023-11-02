import numpy as np
import matplotlib.pyplot as plt


def f1(t):
    return 2 * (0 <= t) * (t <= 2)

def f2(t):
    return (-t + 2) * (0 <= t) * (t <= 2)

def convolution_result(t):
    if t < 0:
        return 0
    elif 0 <= t < 2:
        return 2 * t**2
    elif 2 <= t < 4:
        return 12 * t
    else:
        return 2 * t**2 + 4 * t + 28

# Generate time array
t_values = np.linspace(-1, 6, 500)

# Evaluate functions and convolution
f1_values = np.array([f1(t) for t in t_values])
f2_values = np.array([f2(t) for t in t_values])
conv_values = np.array([convolution_result(t) for t in t_values])

# Plotting
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t_values, f1_values)
plt.title("f1(t)")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t_values, f2_values)
plt.title("f2(t)")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t_values, conv_values)
plt.title("f1(t) * f2(t)")
plt.grid(True)

plt.tight_layout()
plt.show()
