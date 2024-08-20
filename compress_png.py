# Import the OpenCV library
import cv2

# Read the original image file using cv2.imread function
original_img = cv2.imread('sampleimage.jpg')

# Write the original image to a new file in PNG format with compression level 9 using cv2.imwrite function
# cv2.IMWRITE_PNG_COMPRESSION is a flag for the cv2.imwrite function that specifies the compression level of the output image
# The compression level can range from 0 (no compression) to 9 (highest compression)
cv2.imwrite('compressed.png', original_img, [cv2.IMWRITE_PNG_COMPRESSION, 9])