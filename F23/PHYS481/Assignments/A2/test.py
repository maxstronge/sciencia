# Question 2b
# Load the mandrill image
mandrill_img = mpimg.imread('mandrill.png')

def rotate_image_v2(image, angle_deg):
    """
    Rotate an image anticlockwise by a given angle in degrees using NumPy. This method uses precomputed trigonometric values to speed up the calculation.

    Args: image (numpy.ndarray): The input image to be rotated, angle_deg (float): The angle in degrees to rotate the image by

    Returns: rotated_img (numpy.ndarray): The input image rotated by the specified angle
    
    """
    # Convert the angle from degrees to radians
    angle_rad = np.radians(angle_deg)
    
    # Precompute trigonometric values
    cos_angle = np.cos(angle_rad)
    sin_angle = np.sin(angle_rad)

    # Get the number of rows and columns in the image
    n_rows, m_columns, _ = image.shape

    # Create an empty array to store the rotated image
    rotated_img = np.zeros_like(image)
    
    # Pre-compute row and column adjustments
    row_adjust = n_rows / 2
    col_adjust = m_columns / 2
    
# Loop over the rows and columns of the image
    for i in range(n_rows):
        for j in range(m_columns):
            # Calculate pixel adjustments for rotation
            i_adjust = i - row_adjust
            j_adjust = j - col_adjust
            
            # Calculate the new x and y coordinates using precomputed trigonometric values
            x = int(i_adjust * cos_angle - j_adjust * sin_angle + row_adjust)
            y = int(i_adjust * sin_angle + j_adjust * cos_angle + col_adjust)
            
            # Check if the new coordinates are within the bounds of the image
            if 0 <= x < n_rows and 0 <= y < m_columns:
                rotated_img[i, j, :] = image[x, y, :]

    return rotated_img



# Define a function to generate the plots for Question 2b
def q2b(original, rotated, rotation_degrees):
    """
    Plot the original and rotated images. 
    
    Args: original (numpy.ndarray): The original image, rotated (numpy.ndarray): The rotated image, rotation_degrees (float): The angle in degrees that the image was rotated by

    Returns: None
    
    """
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(rotated)
    plt.title(f'Rotated Image ({rotation_degrees} degrees)')
    plt.show()

# Define the rotation angle in degrees (clockwise)
angle_deg = 20.0

# Rotate the image clockwise
%timeit rotated_img = rotate_image_v2(mandrill_img, angle_deg)

# Plot the images
q2b(mandrill_img, rotated_img, angle_deg)
