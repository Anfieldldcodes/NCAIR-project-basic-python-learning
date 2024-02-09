import cv2
from PIL import Image
img = cv2.imread("C:/Users/CAROLINE/Desktop/messi.jpg/messi.jpg.jpeg")
width = 400
height = int(img.shape[0] * (width / img.shape[1]))
img = cv2.resize(img, (width, height))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Convert to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Apply median blur to reduce noise
blur = cv2.medianBlur(gray, 7)

# Apply adaptive thresholding
edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)

# Create the cartoon effect
cartoon = cv2.bilateralFilter(img, 9, 75, 75)

# Combine edges with cartoon
cartoon = cv2.bitwise_and(cartoon, cartoon, mask=edges)
cv2.imshow("Cartoonified Image", cartoon)
cv2.waitKey(0)  # Wait for a key press
output_path = "cartoonified_image.jpeg"
cv2.imwrite(output_path, cartoon)
print(f"Cartoonified image saved at: {output_path}")
