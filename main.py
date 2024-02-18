import os
import cv2

# Video capture setup
cap = cv2.VideoCapture(0)

# Directory setup
directory = 'Image/'

# Create directories if they don't exist
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    letter_dir = os.path.join(directory, letter)
    if not os.path.exists(letter_dir):
        os.makedirs(letter_dir)

# While loop to continuously capture frames
while True:
    _, frame = cap.read()
    count = {letter: len(os.listdir(os.path.join(directory, letter))) for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}

    # Display the frame and region of interest (ROI)
    row, col, _ = frame.shape
    cv2.rectangle(frame, (0, 40), (300, 400), (255, 255, 255), 2)
    cv2.imshow("data", frame)
    cv2.imshow("ROI", frame[40:400, 0:300])
    roi = frame[40:400, 0:300]

    # Save images based on the pressed key
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == ord('q'):
        break
    elif ord('a') <= interrupt & 0xFF <= ord('z'):
        letter = chr(interrupt & 0xFF).upper()
        cv2.imwrite(os.path.join(directory, letter, f'{count[letter]}.png'), roi)

# Release video capture and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
