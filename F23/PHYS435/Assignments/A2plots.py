import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return np.where(abs(x) < 1, 1 - x**2, 0)

# Generate x values
x = np.linspace(-2, 2, 400)

# Generate y values
y = f(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()