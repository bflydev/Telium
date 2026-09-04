import cv2
import os

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
VIDEO_PATH = os.path.join(MODULE_DIR, "super_secret.mp4")

def play_video():
    video = cv2.VideoCapture(VIDEO_PATH)

    delay = int(1000 / 25.44)
    cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Video", 1920, 1080)

    screen_width = 1920
    screen_height = 1080
    x = (screen_width - 1920) // 2
    y = (screen_height - 1080) // 2
    cv2.moveWindow("Video", x, y)

    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break

        resized_frame = cv2.resize(frame, (1920, 1080))
        cv2.imshow("Video", resized_frame)

        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

# Credit to catgirlshadow on discord for the code for this