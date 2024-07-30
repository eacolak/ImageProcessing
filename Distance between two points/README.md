# Distance between two points

Using OpenCV, NumPy and the pyrealsense2 libraries, I will leverage my existing depth sensor camera, the Intel RealSense D457, to calculate the distance between two pixels provided in the code.
This calculation will determine their depths in the X, Y, and Z planes in meters using sensor data. Subsequently, I will use the 3D distance formula:

√((x₂ - x₁)² + (y₂ - y₁)² + (z₂ - z₁)²)

to find and display the distance between the two points. This project is my first endeavor in image processing during my internship.

In this project, I aim to process the data obtained from the depth sensor camera to calculate the real-world distance between two pixels in an image. 
Such calculations are crucial in many image processing applications, such as object detection and measurement. The goal of my project is to use image data to make accurate and precise distance measurements.
