import os
import cv2
import mediapipe as mp
# Video capture setup
cap = cv2.VideoCapture(0)

# Directory setup
directory = 'Nepali_Number_Images/'

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# While loop to continuously capture frames
while True:
    # Read a frame from the video capture
    ret, frame = cap.read()
    if not ret:
        break

    # Define region of interest (ROI) for hand sign
    roi = frame[40:400, 0:300]

    # Display the frame
    cv2.imshow("Nepali Number Sign Detection", frame)

    # Wait for keypress and save image based on the pressed key
    key = cv2.waitKey(1) & 0xFF
    if key == ord('0'):  # Nepali Number ०
        save_path = os.path.join(directory, '0')
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        cv2.imwrite(os.path.join(save_path, f'{len(os.listdir(save_path))}.png'), roi)
    elif key == ord('1'):  # Nepali Number १
        save_path = os.path.join(directory, '1')
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        cv2.imwrite(os.path.join(save_path, f'{len(os.listdir(save_path))}.png'), roi)
    elif key == ord('2'):  # Nepali Number २
        save_path = os.path.join(directory, '2')
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        cv2.imwrite(os.path.join(save_path, f'{len(os.listdir(save_path))}.png'), roi)
    elif key == ord('3'):  # Nepali Number ३
        save_path = os.path.join(directory, '3')
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        cv2.imwrite(os.path.join(save_path, f'{len(os.listdir(save_path))}.png'), roi)
    elif key == ord('4'):  # Nepali Number ४
        save_path = os.path.join(directory, '4')
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        cv2.imwrite(os.path.join(save_path, f'{len(os.listdir(save_path))}.png'), roi)
    elif key == ord('5'):  # Nepali Number ५
        save_path = os.path.join(directory, '5')
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        cv2.imwrite(os.path.join(save_path, f'{len(os.listdir(save_path))}.png'), roi)
    elif key == ord('6'):  # Nepali Number ६
        save_path = os.path.join(directory, '6')
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        cv2.imwrite(os.path.join(save_path, f'{len(os.listdir(save_path))}.png'), roi)
    elif key == ord('7'):  # Nepali Number ७
        save_path = os.path.join(directory, '7')
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        cv2.imwrite(os.path.join(save_path, f'{len(os.listdir(save_path))}.png'), roi)
    elif key == ord('8'):  # Nepali Number ८
        save_path = os.path.join(directory, '8')
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        cv2.imwrite(os.path.join(save_path, f'{len(os.listdir(save_path))}.png'), roi)
    elif key == ord('9'):  # Nepali Number ९
        save_path = os.path.join(directory, '9')
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        cv2.imwrite(os.path.join(save_path, f'{len(os.listdir(save_path))}.png'), roi)

    # Break the loop when 'q' is pressed or the close button of the window is clicked
    if key == ord('q') or cv2.getWindowProperty("Nepali Number Sign Detection", cv2.WND_PROP_VISIBLE) < 1:
        break

# Release video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
