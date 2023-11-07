from fer import FER
import cv2
import time

num_frames = 40
cam = cv2.VideoCapture(0)
detector = FER()
start_time = time.time()
for i in range(num_frames):
    result, image = cam.read()
    if result:
        print(detector.detect_emotions(image)[0]['emotions'])

end_time = time.time()
elapsed_time = end_time - start_time
fps = num_frames / elapsed_time
print(f"Took {elapsed_time:.2f} seconds for {num_frames} frames")
print(f"Frames per Second (FPS): {fps:.2f}")
