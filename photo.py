from cv2 import VideoCapture, imwrite
from time import sleep


def take_picture(file_name="temp", number=2):
    # Initialize webcam
    for i in range(number):
        cap = VideoCapture(0)
        # Capture a single frame
        _, frame = cap.read()

        # Save the frame as "webcam_picture.jpg"
        imwrite(f"{file_name}_{i}.jpg", frame)

        # Release the webcam
        cap.release()

        # Print a success message
        print(f"Webcam picture captured and saved as {file_name}_{i}.jpg")
        sleep(5)


take_picture()
