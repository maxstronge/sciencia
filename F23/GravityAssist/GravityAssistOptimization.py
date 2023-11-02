
#standard imports
import numpy as np
import matplotlib.pyplot as plt
import re
import taichi as ti


ti.init(arch=ti.gpu)

# Constants
G = 6.67430e-20  # Gravitational constant in km^3 / (kg s^2)
G_AU = 6.67430e-11 * (1.496e11)**3  # m^3 AU^-1 s^-2
dx, dy, dz = 1.0, 1.0, 1.0  # Grid spacing in km
dt = 1.0 * 24 * 60 * 60  # time step in seconds
# Grid dimensions (let's say the solar system is about 40 AU in radius)
n_x = 80  # in AU
n_y = 80
n_z = 80


# Define the masses of celestial bodies
masses = {
    'SOL': 1.989e30,  # kg
    'MERCURY': 3.301e23,
    'VENUS': 4.867e24,
    'MARS': 6.4171e23,
    'JUPITER': 1.898e27,
    'SATURN': 5.6834e26,
    'URANUS': 8.6810e25,
    'NEPTUNE': 1.02413e26
}


def get_file_for_body(body):
    # Define the base path
    base_path = r'C:\Users\maxst\sciencia\F23\PHYS435\Assignments\GravityAssist\\'

    # Construct the file path with '***' replaced by the provided string
    file_path = base_path + body + '_ephemeris.txt'

    return file_path

def parse_ephemeris_file(file_path):
    """
    Reads ephemeris data from a text file and returns position data as a numpy array.
    
    Parameters:
    - file_path (str): Path to the ephemeris text file.
    
    Returns:
    - np.array: A numpy array where each element is a tuple (X, Y, Z) representing the position vector.
    """
    position_data = []
    
    # Regular expression pattern to match lines containing X, Y, Z coordinates
    pattern = r"X\s*=\s*([\d\+\-\.Ee]+)\s*Y\s*=\s*([\d\+\-\.Ee]+)\s*Z\s*=\s*([\d\+\-\.Ee]+)"
    
    with open(file_path, 'r') as file:
        reading = False  # Flag to start or stop reading lines
        
        for line in file:
            if "$$SOE" in line:
                reading = True
                continue
            
            if "$$EOE" in line:
                break
            
            if reading:
                match = re.search(pattern, line)
                if match:
                    x, y, z = map(float, match.groups())
                    position_data.append((x, y, z))
    
    return np.array(position_data)

# define position arrays (converted to AU)
SOL_positions = parse_ephemeris_file(get_file_for_body('SOL'))/1.496e8 
MERCURY_positions = parse_ephemeris_file(get_file_for_body('MERCURY'))/1.496e8 
VENUS_positions = parse_ephemeris_file(get_file_for_body('VENUS'))/1.496e8
MARS_positions = parse_ephemeris_file(get_file_for_body('MARS'))/1.496e8
JUPITER_positions = parse_ephemeris_file(get_file_for_body('JUPITER'))/1.496e8 
SATURN_positions = parse_ephemeris_file(get_file_for_body('SATURN'))/1.496e8 
URANUS_positions = parse_ephemeris_file(get_file_for_body('URANUS'))/1.496e8 
NEPTUNE_positions = parse_ephemeris_file(get_file_for_body('NEPTUNE'))/1.496e8 

n_days = len(SOL_positions)
print(f"Number of days: {n_days}")

# Initialize the 4D numpy array for gravitational potential energy.
potential_energy = np.zeros((n_x, n_y, n_z, n_days), dtype=np.float16)