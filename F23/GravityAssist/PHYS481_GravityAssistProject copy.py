import numpy as np
import matplotlib.pyplot as plt
from sympy import diff, symbols, lambdify, cos, sin


# Constants

# conversion factor for AU to km
AU = 149597871 #km

# gravitational constant in km^3 kg^-1 s^-2
G = 6.67408e-20

# mass of the sun in kg
M_sun = 1.989e30

# mass of mars in kg
M_mars = 6.39e23

# radius of mars in km
R_mars = 3389.5

# radius of Earth's orbit in km
r_earth = 1*AU

# distance from Earth to Mars at closest approach in km (it is .3727 AU)
r_mars = r_earth + 0.3727*AU

# mars semimajor axis
a_mars = 1.523679*AU

# gravitational parameter mu
mu = G*M_sun

# velocity of mars relative to the sun at closest approach (in km/s)
u_mars = np.sqrt(mu*((2/r_mars)-(1/a_mars))) 


# semimajor axis of weighted orbit
a = (r_earth + r_mars)/2

# velocity of the spacecraft when it reaches the martian sphere of influence (in km/s)
u_spacecraft = np.sqrt(mu*((2/r_mars)-(1/a))) 

print("u_mars = ", u_mars, "km/s")
print("u_spacecraft = ", u_spacecraft, "km/s")

# Calculate the sphere of influence of Mars
SOI_mars = a_mars * (M_mars / M_sun)**(2/5)

# Generate a range of d values from the radius of Mars to the SOI of Mars
d_list = np.linspace(R_mars, SOI_mars, 1000)

# add 50 to the value of each element in the d_list
d_list = d_list + 50

# Define the symbols
beta, d = symbols('beta d')

# Define the function delta_u_m
D = (G * M_mars) / (d * (u_spacecraft ** 2))
term1 = (1 - 2 * (cos(beta) * (1 - D ** 2) - sin(beta) * D) / (1 + D ** 2) * (u_mars / u_spacecraft)+ ((u_mars / u_spacecraft) ** 2))**0.5
term2 = (1 - 2 * cos(beta) * (u_mars / u_spacecraft) + (u_mars / u_spacecraft) ** 2)**0.5
delta_u_m = u_spacecraft * (term1 - term2)

# make a function out of the symbolic function
delta_u_m_func = lambdify((beta, d), delta_u_m)

# Calculate the derivative
delta_u_m_prime = diff(delta_u_m, beta)

# Convert the symbolic function to a numerical function
delta_u_m_prime_func = lambdify((beta, d), delta_u_m_prime)



def bisection_optimization(func, low, high, tol, d):
    while (high - low) / 2.0 > tol:
        midpoint = (low + high) / 2.0
        if func(midpoint, d) * func(low, d) > 0:
            low = midpoint
        else:
            high = midpoint
    return (high + low) / 2.0

# Initialize variables for bisection method
low = 0 # Lower bound for beta in radians
high = np.pi/2  # Upper bound for beta in radians
tol = 1e-5  # Tolerance level

optimal_betas = []
# for each value of d, find the value of beta that makes delta_u_m_prime_func equal to zero
for d_value in d_list:
    optimal_betas.append(bisection_optimization(delta_u_m_prime_func, low, high, tol, d_value))

# Convert the list of optimal beta values to a numpy array
optimal_betas = np.array(optimal_betas)

# for each pair d and its optimal beta, compute the delta_u_m value and add it to a list, keeping track of the index
# of the optimal beta value
delta_u_m_list = []

for i in range(len(d_list)):
    delta_u_m_list.append(delta_u_m_func(optimal_betas[i], d_list[i]))


# find the maximum value of delta_u_m and its index
max_delta_u_m = max(delta_u_m_list)
max_index = delta_u_m_list.index(max_delta_u_m)

# find the corresponding optimal beta and d values
optimal_beta = optimal_betas[max_index]
optimal_d = d_list[max_index]

# print the maximum value of delta u_m and the corresponding d and beta
print("the maximum value of delta u_m is ", max_delta_u_m, " km/s for d = ", optimal_d, " km and ", np.degrees(optimal_beta), " degrees")

# plot the delta_u_m vs beta graph for d
beta_values = np.linspace(0, np.pi/2, 1000)
# don't need to plot all 1000, so just plot 100
d_values_to_plot = np.linspace(d_list[0], d_list[-1], num=100)
plt.figure()
lines = []  # list to store the line objects
labels = []  # list to store the label names

for d_value in d_values_to_plot:
    delta_u_m_values = [delta_u_m_func(beta, d_value) for beta in beta_values]
    line, = plt.plot(np.degrees(beta_values), delta_u_m_values, label=f'd = {d_value:.2f} km')
    lines.append(line)
    labels.append(f'd = {d_value:.2f} km')

plt.xlabel("beta (degrees)")
plt.ylabel("delta_u_m (km/s)")
plt.title("delta_u_m vs beta for different d values")

# Only use the first 10 lines and labels for the legend
plt.legend(handles=lines[:10], labels=labels[:10], loc='upper right')

plt.show()

# plot the delta_u_m vs d graph for beta = 20.046958923339844 
beta_value = optimal_beta
d_values_to_plot = np.linspace(d_list[0], d_list[-1], num=100)
plt.figure()
plt.plot(d_list, delta_u_m_list)
plt.xlabel("d (km)")
plt.ylabel("delta_u_m (km/s)")
plt.title("delta_u_m vs d for beta = 20.0469 degrees")
plt.show()
