from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import cv2
import numpy as np
from ultralytics import YOLO
import threading
import time

# Initialize YOLOv8 model
model = YOLO("yolov8n.pt")  # YOLOv8 pretrained model (cars detection)

# Total parking slots (customize this for your parking lot)
total_slots = 36

# Flask app and SocketIO setup
app = Flask(__name__)
socketio = SocketIO(app)

# Start processing the camera feed and send updates to frontend
def process_camera():
    cap = cv2.VideoCapture(0)  # Webcam capture
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to capture frame.")
            break

        # Run YOLO detection
        results = model(frame)
        detections = results[0].boxes.xyxy  # Bounding boxes
        classes = results[0].boxes.cls      # Class IDs
        scores = results[0].boxes.conf      # Confidence scores

        # Filter for 'car' class (based on COCO dataset IDs)
        car_detections = [
            (int(x1), int(y1), int(x2), int(y2)) for (x1, y1, x2, y2), cls in zip(detections, classes) if cls == 2
        ]

        # Count detected cars
        number_of_cars = len(car_detections)
        vacant_slots = max(0, total_slots - number_of_cars)

        # Send data to frontend via SocketIO
        socketio.emit('update_parking_status', {'available': vacant_slots, 'occupied': number_of_cars})

        # Sleep to simulate real-time data update
        time.sleep(1)

    cap.release()

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML page

# Start camera feed when "Start Camera" button is clicked
@socketio.on('start_camera')
def handle_start_camera():
    """ Handle the start_camera event sent by frontend """
    print("Starting real-time parking detection...")
    # Start the camera processing in a separate thread
    threading.Thread(target=process_camera, daemon=True).start()

if __name__ == '__main__':
    socketio.run(app, debug=True)

