import cv2 as cv

cap = cv.VideoCapture(0)  # or try using other indexes like 1, 2, etc.

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break  # Exit the loop if the frame could not be captured
    
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("webcam", gray_frame)

    if cv.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()