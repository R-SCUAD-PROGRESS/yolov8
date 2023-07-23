import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('best.pt')

# Open the video file
image = "image.jpg"
frame = cv2.imread(image)

results = model(frame)

# Visualize the results on the frame
annotated_frame = results[0].plot()

# Display the annotated frame
cv2.imshow("YOLOv8 Inference", annotated_frame)

cv2.waitKey(0)
cv2.destroyAllWindows()