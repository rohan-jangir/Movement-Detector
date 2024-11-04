import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture("C:\\Users\\rohan\\OneDrive\\Desktop\\data science\\capstone projects\\movement_detect\\test.mp4")

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

detector = PoseDetector()
posList = []

while True:
    success, img = cap.read()
    if not success:
        print("No more frames or error reading the video.")
        break

    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img)

    print("Landmarks:", lmList)  # Debugging output

    if lmList:
        lmString = ""
        for lm in lmList:
            if len(lm) >= 4:  # Ensure there are enough elements in lm
                lmString += f'{lm[1]},{img.shape[0] - lm[2]},{lm[3]},'
            else:
                print("Warning: Landmark does not have enough data:", lm)
        posList.append(lmString)
        print(len(posList))

    if img is not None:
        cv2.imshow("Image", img)
    else:
        print("Error: Image is None.")

    key = cv2.waitKey(1)
    if key == ord('s'):
        with open("AnimationFile.txt", 'w') as f:
            f.writelines(["%s\n" % item for item in posList])

# Release resources
cap.release()
cv2.destroyAllWindows()
