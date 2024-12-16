

## **Overview**
This project is a real-time parking lot detection system that uses **YOLOv8** (You Only Look Once) for detecting cars and determining the number of vacant parking slots. The system integrates a Python-based backend with a modern web interface to display live results and start camera detection directly from the browser.

---

## **Features**
- **Real-time car detection** using YOLOv8.
- Counts the number of cars and calculates available parking slots.
- A web interface with animations to start the detection process.
- Fully responsive and modern UI design.
- Easy to set up and run on any system with a webcam.

---

## **Requirements**

### **Python Dependencies**
- Python 3.9+
- `opencv-python`
- `ultralytics`
- `flask`
- `flask-cors`
- `numpy`

Install these dependencies using:
```bash
pip install opencv-python ultralytics flask flask-cors numpy
```

### **Frontend Dependencies**
The frontend is built with HTML, CSS, and JavaScript. No additional dependencies are required for the web interface.

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-repository/parking-lot-detection.git
cd parking-lot-detection
```

### **2. Set Up Python Backend**
1. Ensure all dependencies are installed using the `pip install` command above.
2. Run the backend server:
   ```bash
   python app.py
   ```

### **3. Run the Frontend**
1. Open the `index.html` file in any modern browser (preferably Google Chrome).
2. Alternatively, host the frontend locally with any server (e.g., `http-server` for Node.js).

### **4. Start the Detection**
1. Click the **"Start Camera"** button on the webpage.
2. The backend will activate the webcam and begin detecting cars.

---

## **Usage**
1. Open the web application.
2. Ensure the camera is connected and the parking lot is in the frame.
3. The system will automatically detect cars and display:
   - Total parking slots.
   - Number of occupied slots.
   - Number of vacant slots.
4. Press **"q"** in the camera window to stop detection.

---

## **File Structure**
```
parking-lot-detection/
│
├── app.py               # Python backend for real-time car detection
├── yolo_camera.py       # YOLOv8-based car detection logic
├── templates/
│   └── index.html       # Main frontend file
├── static/
│   ├── css/
│   │   └── styles.css   # Styling for the web application
│   ├── js/
│   │   └── app.js       # JavaScript for interactivity and animations
├── README.md            # Project documentation
└── .vscode/
    └── launch.json      # Debugging configuration for VS Code
```

---

## **Customization**

### **1. Change Total Slots**
Update the `total_slots` variable in the `yolo_camera.py` file:
```python
total_slots = 36  # Adjust based on your parking lot
```

### **2. Modify Frontend**
You can enhance the web interface by editing the `index.html`, `styles.css`, and `app.js` files located in the `static` folder.

---

## **Future Improvements**
- Use a pre-trained parking dataset for better accuracy in detecting vacant slots.
- Add support for multiple cameras.
- Display real-time analytics on the web interface.
- Deploy the system to a cloud server for remote access.

---

## **Contributors**
- **Lebi Raja**  
  Artificial Intelligence & Data Science Student, Karunya University.

---

## **License**
This project is licensed under the MIT License.

--- 
