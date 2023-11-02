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

# Define the symbols
beta, d = symbols('beta d')

# Define the function delta_u_m
D = (G * M_mars) / (d * (u_spacecraft ** 2))
term1 = (1 - 2 * (cos(beta) * (1 - D ** 2) - sin(beta) * D) / (1 + D ** 2) * (u_mars / u_spacecraft)+ ((u_mars / u_spacecraft) ** 2))**0.5
term2 = (1 - 2 * cos(beta) * (u_mars / u_spacecraft) + (u_mars / u_spacecraft) ** 2)**0.5
delta_u_m = u_spacecraft * (term1 - term2)

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
# Loop through each d value
for d_value in d_list:
    if d_value > R_mars*1.5:
        optimal_beta = bisection_optimization(delta_u_m_prime_func, low, high, tol, d_value)
        print("the optimal value of beta for d = ", d_value, " km is ", np.degrees(optimal_beta), "degrees")
        optimal_betas.append(optimal_beta)


# Convert the symbolic expression to a numerical function
delta_u_m_func = lambdify((beta, d), delta_u_m)

# Now you can call delta_u_m_func as a function
delta_v_list = []
for i, beta in enumerate(optimal_betas):
    delta_v = delta_u_m_func(beta, d_list[i])
    delta_v_list.append(delta_v)


# print the maximum value of delta u_m and the corresponding d and beta
max_delta_v = max(delta_v_list)
max_delta_v_index = delta_v_list.index(max_delta_v)
max_d = d_list[max_delta_v_index]
max_beta = optimal_betas[max_delta_v_index]


print("The maximum delta u_m is ", max_delta_v, " km/s")
print("The corresponding d is ", max_d, " km")
print("The corresponding beta is ", np.degrees(max_beta), " degrees")




# Generate a range of beta values
beta_values = np.linspace(0, np.pi, 1000)  # 1000 points between pi/2 and pi

# get a list of only the first two elements of d_list
d_values_to_plot = d_list[::len(d_list)//5]  # for example, plot every 5th d value

# Plot Delta u_m for each d value
for d_value in d_values_to_plot:
    delta_u_m_values = [delta_u_m_func(beta, d_value) for beta in beta_values]
    plt.plot(beta_values, delta_u_m_values, label=f'd = {d_value:.2f} km')

# Add labels and legend
plt.xlabel('Beta (degrees)')
plt.ylabel('Delta u_m (km/s)')
plt.legend()

# Show the plot
plt.show()



# Choose a range of d values to plot
d_values_to_plot = d_list[::len(d_list)//5]  # for example, plot every 5th d value

# Create a new figure with a defined size and dpi
plt.figure(figsize=(10, 6), dpi=80)

# Plot delta_u_m_prime for each d value
for d_value in d_values_to_plot:
    delta_u_m_prime_values = [delta_u_m_prime_func(beta, d_value) for beta in beta_values]
    plt.plot(beta_values, delta_u_m_prime_values, label=f'd = {d_value:.2f} km')

# Add labels and legend
plt.xlabel('Beta (degrees)', fontsize=14)
plt.ylabel('delta_u_m_prime', fontsize=14)
plt.title('Delta u_m_prime vs Beta', fontsize=16)
plt.grid(True)
plt.legend(fontsize=12)

# Show the plot
plt.show()