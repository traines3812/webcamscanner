import cv2

# Set the URL for the webcam
url = "http://192.168.1.1:8080/video"

# Connect to the webcam
cap = cv2.VideoCapture(url)

# Check if the connection was successful
if not cap.isOpened():
    print("Failed to connect to the webcam.")
else:
    print("Successfully connected to the webcam.")
    cap.release()
This script uses the cv2 (OpenCV) library to connect to a webcam using its URL. In this example, the URL is set to http://192.168.1.1:8080/video, but you can replace this with the URL of your own webcam. The script then uses the cv2.VideoCapture function to connect to the webcam and checks if the connection was successful by using the isOpened method.

Please note that this script only tests if a connection can be established with the webcam, and not if the webcam is actually available. Also, make sure to comply with the laws and regulations of your country regarding the use of webcams.





