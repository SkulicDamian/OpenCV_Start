import cv2

cap = cv2.VideoCapture(r"C:\Users\Damian\cv_image\sample-mp4-file.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break



