# Movement Detection with Pose Estimation

This repository contains two Python scripts that utilize OpenCV and the CVZone library for movement detection and pose estimation. The scripts demonstrate the capability to analyze video input from a file or a webcam and save the detected pose landmarks to a text file.

## Requirements

- Python 3.x
- OpenCV
- CVZone

You can install the required libraries using pip:

```bash
pip install opencv-python cvzone
```
**Note:** install mediapipe if not install automatically
```bash
pip install mediapipe
```

## Scripts
### 1. Video Pose Detection from File
This script reads a video file and utilizes a pose detector to identify and log the pose landmarks in each frame. The detected landmarks are saved to a file named AnimationFile.txt when the 's' key is pressed.

#### Key Features:
* Reads a video file specified in the code.
* Uses CVZone's PoseDetector to find and log pose landmarks.
* Outputs landmark data in a specific format to AnimationFile.txt.

#### Usage:

**1. Modify the path of the video file in the script:**
```bash
cap = cv2.VideoCapture("path_to_your_video_file.mp4")
```

**2. Run the script:**
```bash
python file_name.py
```
**3. Press 's' to save the landmark data and 'q' to exit.**

## 2. Movement Detection with Webcam
This script captures video from the default webcam and detects movement. When movement is detected, it applies pose estimation to the frame, logging the pose landmarks similarly to the first script.

#### Key Features:
* Utilizes the default webcam for real-time movement detection.
* Applies Gaussian blur and contour detection to identify movement.
* Saves the detected pose landmarks to AnimationFile.txt when the 's' key is pressed.

#### Usage:

**1. Run the script:**
```bash
python file_name.py
```
**2. Move in front of the webcam to trigger detection. Press 's' to save the landmark data and 'q' to exit.**

## Notes
* Ensure your webcam is enabled and accessible for the second script.
* Adjust the movement detection sensitivity by changing the contour area threshold in the second script.
* The output landmark data format in AnimationFile.txt consists of coordinates for each landmark detected.
