import cv2
import numpy as np

def calculate_mse(img1, img2):
    """
    Calculates the Mean Squared Error (MSE) between two images.

    Parameters:
    img1 (numpy.ndarray): The first image represented as a 2D NumPy array.
    img2 (numpy.ndarray): The second image represented as a 2D NumPy array.

    Returns:
    float: The Mean Squared Error (MSE) between the two images.
    """
    return np.mean((img1 - img2) ** 2)

def calculate_psnr(img1, img2):
    """
    Calculates the Peak Signal-to-Noise Ratio (PSNR) between two images.

    Parameters:
    img1 (numpy.ndarray): The first image represented as a 2D NumPy array.
    img2 (numpy.ndarray): The second image represented as a 2D NumPy array.

    Returns:
    float: The PSNR value between the two images. If the Mean Squared Error (MSE) is zero,
           the function returns infinity (float('inf')).
    """
    mse = calculate_mse(img1, img2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    return 20 * np.log10(max_pixel / np.sqrt(mse))

def compress_image(image_path, quality=90):
    """
    Compresses an image using JPEG compression.

    This function reads an image from the specified path, compresses it using JPEG compression,
    and then decodes the compressed image back to its original format.

    Parameters:
    image_path (str): The path to the image file to be compressed.
    quality (int, optional): The quality of the compressed image. The value should be between 0 and 100.
                             Default is 90.

    Returns:
    numpy.ndarray: The decoded compressed image represented as a 2D NumPy array.
    """
    # Read the image
    img = cv2.imread(image_path)
    
    # Encode the image with JPEG compression
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    _, encoded_img = cv2.imencode('.jpg', img, encode_param)
    
    # Decode the compressed image
    decoded_img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)
    
    return decoded_img

# Read the original image
original_img = cv2.imread('sampleimage.jpg')
# Compress the image with 50% quality
compressed_img = compress_image('sampleimage.jpg', quality=50)

# Display results
cv2.imshow('Original', original_img)
cv2.imshow('Compressed', compressed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


