import cv2
from cvzone.PoseModule import PoseDetector
import numpy as np

# Initialize the video capture
cap = cv2.VideoCapture(0)  # Use 0 for the default camera

# Initialize the pose detector
detector = PoseDetector()
posList = []

# Read the first frame for movement detection
_, first_frame = cap.read()
first_frame_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_frame_gray = cv2.GaussianBlur(first_frame_gray, (21, 21), 0)

while True:
    # Read the current frame
    success, frame = cap.read()
    if not success:
        print("No more frames or error reading the video.")
        break

    # Convert to grayscale and apply Gaussian blur for movement detection
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.GaussianBlur(frame_gray, (21, 21), 0)

    # Compute the absolute difference between the first frame and the current frame
    delta_frame = cv2.absdiff(first_frame_gray, frame_gray)

    # Threshold the delta frame to get the binary image
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    # Dilate the threshold image to fill in holes
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # Find contours in the threshold image
    contours, _ = cv2.findContours(thresh_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Adjust the threshold for your needs
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw a rectangle around the moving object

            # Perform pose detection if movement is detected
            img = detector.findPose(frame)
            lmList, bboxInfo = detector.findPosition(img)

            # Check if landmarks are detected and save positions
            if lmList:
                lmString = ""
                for lm in lmList:
                    if len(lm) >= 4:  # Ensure there are enough elements in lm
                        lmString += f'{lm[1]},{img.shape[0] - lm[2]},{lm[3]},'
                posList.append(lmString)
                print(len(posList))

    # Show the original frame with movement rectangles
    cv2.imshow("Movement Detection", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Save the positions to a file when 's' is pressed
with open("AnimationFile.txt", 'w') as f:
    f.writelines(["%s\n" % item for item in posList])

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
