import numpy as np
import matplotlib.pyplot as plt

# Define the complex number
c = -2 - 1j

# Calculate the roots
roots = [np.power(c, 1/6) * np.exp(1j * 2 * np.pi * k / 6) for k in range(6)]

# Extract real and imaginary parts
real_parts = [root.real for root in roots]
imag_parts = [root.imag for root in roots]

# Plot the roots
plt.scatter(real_parts, imag_parts)
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.title('Roots of $z = \sqrt[6]{ -2-i }$')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()