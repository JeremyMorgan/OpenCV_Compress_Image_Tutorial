# Import the OpenCV library
import cv2

# Read the original image file using cv2.imread function
original_img = cv2.imread('sampleimage.jpg')

# Write the original image to a new file in WebP format with 80% quality using cv2.imwrite function
# cv2.IMWRITE_WEBP_QUALITY is a flag for the cv2.imwrite function that specifies the quality of the output image
# The quality value can range from 1 (worst) to 100 (best)
cv2.imwrite('compressed.webp', original_img , [cv2.IMWRITE_WEBP_QUALITY, 80])