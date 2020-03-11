# import the necessary packages
import cv2
 
# load the image and show it
image = cv2.imread("florida_trip.png")
cv2.imshow("Original", image)
 
# cropping an image is accomplished using simple NumPy array slices --
# let's crop the face from the image
face = image[85:250, 85:220]
cv2.imshow("Face", face)
 
# ...and now let's crop the entire body
body = image[90:450, 0:290]
cv2.imshow("Body", body)

# 2. Question
# Download the source code and image to this lesson. Then, use the florida_trip.png image to answer the following question.
# What is the most appropriate NumPy array slice to crop the people in the background from the florida_trip.png image?
body = image[173:235, 13:81]
cv2.imshow("2. Question", body)

# 3. Question
# Use the same image from the previous question and determine the best NumPy slice to extract the boat/building-like structure from the background of florida_trip.png.
body = image[124:212, 225:380]
cv2.imshow("3. Question", body)

cv2.waitKey(0)