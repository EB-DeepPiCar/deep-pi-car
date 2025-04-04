import cv2
import numpy as np

def nothing(x):
    pass

# Avaa video (0 = sisäinen kamera tai korvaa 'video.mp4' / kuva)
cap = cv2.VideoCapture(0)

# Luo ikkuna liukusäätimille
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 400, 300)

# Luo liukusäätimet
cv2.createTrackbar("Hue Min", "Trackbars", 100, 179, nothing)
cv2.createTrackbar("Hue Max", "Trackbars", 130, 179, nothing)
cv2.createTrackbar("Sat Min", "Trackbars", 150, 255, nothing)
cv2.createTrackbar("Sat Max", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("Val Min", "Trackbars", 50, 255, nothing)
cv2.createTrackbar("Val Max", "Trackbars", 255, 255, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Hae liukusäätimien arvot
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars")

    # Luo maski
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Näytä kuvat
    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Filtered Result", result)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC lopettaa
        break

cap.release()
cv2.destroyAllWindows()
