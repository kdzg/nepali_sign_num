import os
import cv2
from datetime import datetime

# Function to save an image with a custom name
def save_image_with_custom_name(directory, roi):
    while True:
        # Prompt user for input to enter file name explicitly
        str_name = input("Enter number: ")
        if not str_name.strip():
            # If user presses 'Enter' without entering a name, cancel image capture
            return
        # Get the current date and time
        now = datetime.now()
        date_time = now.strftime("%d_%m_%Y_%H_%M_%S")
        # Construct full file path
        file_name = f"{date_time}_{str_name}.png"
        image_path = os.path.join(directory, file_name)
        if not os.path.exists(image_path):
            # Save the image
            cv2.imwrite(image_path, roi)
            print(f"Image saved as '{image_path}'")
            break
        else:
            print("A file with that name already exists. Please choose a different name.")

# Video capture setup
cap = cv2.VideoCapture(0)

# Directory setup
directory = 'Nepali_Number_Images/'

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Failed to open the camera.")
    exit()

# While loop to continuously capture frames
while True:
    # Read a frame from the video capture
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Define region of interest (ROI) for hand sign
    cv2.rectangle(frame, (0, 40), (300, 400), (255, 255, 255), 2)  # Adding the frame around the ROI
    roi = frame[40:400, 0:300]

    # Display the frame
    cv2.imshow("Nepali Number Sign Detection", frame)

    # Wait for keypress and save image based on the pressed key
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        # Break the loop when 'q' is pressed
        break
    elif chr(key) in '0123456789':  # Check if the pressed key is a number key
        save_path = os.path.join(directory, chr(key))
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        # Prompt user for custom file name and save image
        save_image_with_custom_name(save_path, roi)

# Release video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
