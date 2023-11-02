import numpy as np
import matplotlib.pyplot as plt

# Constants
AU = 149597871  # Conversion factor for AU to km
G = 6.67408e-20  # Gravitational constant in km^3 kg^-1 s^-2
M_sun = 1.989e30  # Mass of the sun in kg
M_mars = 6.39e23  # Mass of Mars in kg
R_mars = 3389.5  # Radius of Mars in km
r_earth = 1 * AU  # Radius of Earth's orbit in km
r_mars = r_earth + 0.3727 * AU  # Distance from Earth to Mars at closest approach in km
a_mars = 1.523679 * AU  # Mars semimajor axis
a = (r_earth + r_mars) / 2  # Semimajor axis of weighted orbit

# Calculate the gravitational parameter
mu = G * M_sun

# Calculate velocities
u_mars = np.sqrt(mu * ((2 / r_mars) - (1 / a_mars)))  # Velocity of Mars relative to the sun at closest approach (in km/s)
u_spacecraft = np.sqrt(mu * ((2 / r_mars) - (1 / a)))  # Velocity of the spacecraft when it reaches the Martian sphere of influence (in km/s)

print("u_mars =", u_mars, "km/s")
print("u_spacecraft =", u_spacecraft, "km/s")


def calculate_d_values(G, M, u_mi):
    """
    Calculate the impact parameter values for a given gravitational constant, mass, and initial speed.
    
    Parameters:
    G: Gravitational constant
    M: Mass of the object
    u_mi: Initial speed
    
    Returns:
    d_values: List of impact parameter values
    """
    d_values = []
    for gamma_degree in range(1, 180):
        gamma_rad = np.radians(gamma_degree)
        tan_gamma_over_2 = np.tan(gamma_rad / 2)
        d = (G * M) / (tan_gamma_over_2 * u_mi ** 2)
        d_values.append(d)
    return d_values


# Generate list of d values for the impact parameter
d_list = calculate_d_values(G, M_mars, u_spacecraft)


def calculate_delta_u_m(beta, d, G, M, u_mi, u_p):
    """
    Calculate the change in speed given input angle beta, impact parameter d, gravitational constant G,
    mass M, initial speed u_mi, and planet speed u_p.
    
    Parameters:
    beta: Input angle in radians
    d: Impact parameter
    G: Gravitational constant
    M: Mass of the object
    u_mi: Initial speed
    u_p: Planet speed
    
    Returns:
    delta_u_m: Change in speed
    """
    D = (G * M) / (d * (u_mi ** 2))
    term1 = np.sqrt(1 - 2 * (np.cos(beta) * (1 - D ** 2) - np.sin(beta) * D) / (1 + D ** 2) * (u_p / u_mi) + ((u_p / u_mi) ** 2))
    term2 = np.sqrt(1 - 2 * np.cos(beta) * (u_p / u_mi) + (u_p / u_mi) ** 2)
    return u_mi * (term1 - term2)

def calculate_delta_u_m_prime(d, G, M, u_mi, u_p):
    """
    Calculate the derivative of delta_u_m with respect to beta.
    
    Parameters:
    beta: Input angle in radians
    d: Impact parameter
    G: Gravitational constant
    M: Mass of the object
    u_mi: Initial speed
    u_p: Planet speed
    
    Returns:
    delta_u_m_prime: Derivative of delta_u_m
    """
    D = (G * M) / (d * (u_mi ** 2))
    return -u_mi * (
            u_p * np.sin(beta) / (u_mi * np.sqrt(1 - 2 * u_p * np.cos(beta) / u_mi + u_p ** 2 / u_mi ** 2)
        ) - u_p ** 2 * (
                D * np.cos(beta) + (1 - D ** 2) * np.sin(beta)
        ) / (
                u_mi ** 2 * np.sqrt(
                    1 + 2 * u_p ** 2 * (D * np.sin(beta) - (1 - D ** 2) * np.cos(beta)) / (
                            u_mi ** 2 * (D ** 2 + 1))
                ) * (D ** 2 + 1)
        )
    )


def bisection_optimization(func, low, high, tol, d, G, M, u_mi, u_p):
    """
    Perform bisection optimization to find the optimal value of beta for a given function and parameters.
    
    Parameters:
    func: Function to optimize
    low: Lower bound for beta in radians
    high: Upper bound for beta in radians
    tol: Tolerance level
    d: Impact parameter
    G: Gravitational constant
    M: Mass of the object
    u_mi: Initial speed
    u_p: Planet speed
    
    Returns:
    optimal_beta: Optimal value of beta
    """
    while (high - low) / 2.0 > tol:
        midpoint = (low + high) / 2.0
        if func(midpoint, d, G, M, u_mi, u_p) * func(low, d, G, M, u_mi, u_p) > 0:
            low = midpoint
        else:
            high = midpoint
    return (high + low) / 2.0


# Initialize variables for bisection method
low = np.pi / 2  # Lower bound for beta in radians
high = np.pi  # Upper bound for beta in radians
tol = 1e-5  # Tolerance level


# Loop through each d value
optimal_betas = []
for d in d_list:
    if d > R_mars:
        optimal_beta = bisection_optimization(calculate_delta_u_m_prime, low, high, tol, d, G, M_mars, u_spacecraft, u_mars)
        print("The optimal value of beta for d =", d, "km is", np.degrees(optimal_beta), "degrees")
        optimal_betas.append(optimal_beta)

delta_v_list = []
for beta in optimal_betas:
    delta_v = calculate_delta_u_m(beta, d_list[0], G, M_mars, u_spacecraft, u_mars)
    delta_v_list.append(delta_v)

# Print the maximum value of delta u_m and the corresponding d and beta
max_delta_v = max(delta_v_list)
max_delta_v_index = delta_v_list.index(max_delta_v)
max_d = d_list[max_delta_v_index]
max_beta = optimal_betas[max_delta_v_index]
print("The maximum delta u_m is", max_delta_v * 1000, "km/s")
print("The corresponding d is", max_d, "km")
print("The corresponding beta is", np.degrees(max_beta), "degrees")