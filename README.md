### **SMART-PARKING-SYSTEM 🚗**  

---

<h1 align="center">SMART-PARKING-SYSTEM</h1>  
<p align="center">
  <a href="#">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQfaTiGrhKrZ__y70ByRq6I8cSW2m8EMRTGhlCGGP0KpXQQde5R&usqp=CAU" alt="Logo" width="auto" height="auto">
  </a>
</p>  

---

## **📕 Abstract**  
The **SMART-PARKING-SYSTEM** leverages image processing techniques to automate the detection of available parking slots in real-time. Aimed at reducing human involvement and traffic congestion in parking lots, this system uses a high-definition camera and software to provide parking guidance. By analyzing images from parking lots, the system identifies vacant slots, displays their locations, and navigates drivers to these spaces. This cost-effective, automated system ensures efficient parking lot management while enhancing the user experience.  

---

## **📜 Introduction**  
With the increasing number of vehicles in urban areas, finding available parking spaces has become a significant challenge. Drivers often waste valuable time and fuel navigating through parking lots. The **SMART-PARKING-SYSTEM** addresses these issues by:  
1. Capturing real-time images of parking areas using CCTV cameras.  
2. Detecting cars and empty parking spaces using image processing techniques.  
3. Guiding drivers to available slots, optimizing space utilization.  

This project utilizes MATLAB as the primary development platform, providing a scalable and cost-effective parking management solution.  

---

## **📃 Proposed Model and Methodology**  
The system operates in five key stages:  

### **1. System Initialization**  
- A reference image of an empty parking lot is captured at the time of installation.  
- The image serves as a baseline for identifying parking slots.  

### **2. Image Acquisition**  
- Real-time images of the parking lot are captured using CCTV cameras.  
- Images are processed in MATLAB to identify changes (e.g., parked cars).  

### **3. Thresholding and Image Processing**  
- Captured images are converted to grayscale and binary formats.  
- Binary images are processed using morphological operations and filters to eliminate noise and improve accuracy.  

### **4. Image Detection**  
- Blob analysis is performed to identify cars and count their numbers.  
- The system calculates the number of vacant slots based on this analysis.  

### **5. Parking Guidance**  
- Real-time information about available slots is displayed for drivers.  
- Drivers are navigated to the nearest vacant slot efficiently.  

---

## **📄 Algorithm**  
The main algorithm steps include:  
1. Capture live video stream from the parking lot using cameras.  
2. Extract images from the video stream.  
3. Convert RGB images to binary images.  
4. Divide images lane-wise and process each lane sequentially.  
5. Detect vacant slots by comparing live images with the reference image.  
6. Display the location of available slots and guide drivers accordingly.  

---

## **📸 Screenshots**  

### **Command Window Output**  
<p align="center">
  <a href="#">
    <img src="https://raw.githubusercontent.com/abhishekapk/SMART-PARKING-SYSTEM/master/Images/image7.jpg" alt="Command Window Output" width="auto" height="auto">
  </a>
</p>  

### **Parking Lot Observation**  
- **Figure 1**: Overall view of the parking lot.  
<p align="center">
  <a href="#">
    <img src="https://raw.githubusercontent.com/abhishekapk/SMART-PARKING-SYSTEM/master/Images/image8.jpg" alt="Figure 1" width="auto" height="auto">
  </a>
</p>  

- **Figure 2**: Lane-wise parking observation with vacant slot detection.  
<p align="center">
  <a href="#">
    <img src="https://raw.githubusercontent.com/abhishekapk/SMART-PARKING-SYSTEM/master/Images/image9.jpg" alt="Figure 2" width="auto" height="auto">
  </a>
</p>  

---

## **📑 Conclusion**  
The **SMART-PARKING-SYSTEM** offers a robust and scalable solution for managing parking lots in urban areas. By using image processing techniques, the system efficiently detects and manages parking spaces while minimizing human involvement and operational costs.  
**Future Scope**:  
- Integration with online parking reservation systems.  
- Mobile app support for real-time slot booking.  
- Enhanced security through vehicle tracking.  

---

## **📜 License**  
This project is licensed under the MIT License.  

---

## **💻 Team Members**  
Developed by **Team 3**:  
- **Lebi Raja**  
- **Jayasurya**  
- **Maniprakash**  
- **Joshua**  
