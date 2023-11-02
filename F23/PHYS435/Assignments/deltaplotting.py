import numpy as np
import matplotlib.pyplot as plt

# Define the points a and b
a = 1
b = 3

# Define the x values
x = np.linspace(-2, 5, 1000)

# Define the Dirac delta functions
delta_a = np.where(np.isclose(x, a, atol=0.005), 1000, 0)
delta_b = np.where(np.isclose(x, b, atol=0.005), 1000, 0)

# Plot the Dirac delta functions
plt.figure()
plt.plot(x, delta_a, label='delta(t-a1)')
plt.plot(x, delta_b, label='delta(t-a2)')
plt.ylim([0, 1100])
plt.legend()
plt.show()