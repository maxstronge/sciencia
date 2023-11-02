import numpy as np
import matplotlib.pyplot as plt

def f1(t):
    return 2 * (0 <= t) * (t <= 2)

def f2(t):
    return (-t + 2) * (0 <= t) * (t <= 2)

def convolution_result(t):
    return 0 * (t < 0) + \
           (4 * t - t**2) * (0 <= t) * (t <= 2) + \
           (t - 4)**2 * (2 < t) * (t < 4) + \
           0 * (t >= 4)

# Convert the functions to numpy functions
f1_np = np.vectorize(f1)
f2_np = np.vectorize(f2)
convolution_result_np = np.vectorize(convolution_result)

# Plot the functions
t_values = np.linspace(-4,8, 1000)
plt.figure()
plt.plot(t_values, f1_np(t_values), label='f1')
plt.plot(t_values, f2_np(t_values), label='f2')
plt.plot(t_values, convolution_result_np(t_values), label='convolution_result')
plt.xlim([-2, 8])
plt.ylim([0, 6]) 
plt.legend()
plt.show()