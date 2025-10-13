import cv2
import numpy as np

path_points = []

lower_green = np.array([35, 100, 100])
upper_green = np.array([85, 255, 255])

video = cv2.VideoCapture('Ball_Tracking.mp4')

while True:
    is_frame_read_successfully, frame = video.read()

    if not is_frame_read_successfully:
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    green_mask = cv2.inRange(hsv_frame, lower_green, upper_green)

    contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        biggest_contour = max(contours, key=cv2.contourArea)
        
        (x, y), radius = cv2.minEnclosingCircle(biggest_contour)

        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            
            center_point = (int(x), int(y))
            path_points.append(center_point)

    for i in range(1, len(path_points)):
        start_point = path_points[i - 1]
        end_point = path_points[i]
        cv2.line(frame, start_point, end_point, (0, 0, 255), 2)

    cv2.imshow("Beginner Ball Tracker", frame)

    key = cv2.waitKey(25)
    if key == ord("q"):
        break

video.release()
cv2.destroyAllWindows()