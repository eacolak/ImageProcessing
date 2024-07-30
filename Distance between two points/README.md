# Distance Measurement with Intel RealSense D457

This project demonstrates how to measure the distance between two points in a 3D space using the Intel RealSense D457 depth camera along with the `pyrealsense2` and `OpenCV` libraries. The following code captures both color and depth images from the camera, calculates the distance between two specified points, and visualizes the results.

## Overview

1. **Libraries Used:**
   - `pyrealsense2`: For interfacing with the Intel RealSense depth camera.
   - `numpy`: For numerical operations.
   - `cv2` (OpenCV): For image processing and visualization.

2. **Camera Setup:**
   - Configures the Intel RealSense D457 camera to stream depth and color data at a resolution of 640x480 pixels and 30 frames per second (fps).

3. **Distance Calculation:**
   - The code calculates the 3D distance between two points in the camera's view using depth data. 
   - The 3D distance is computed using the formula: 
     \[
    √((x₂ - x₁)² + (y₂ - y₁)² + (z₂ - z₁)²)
     \]
   - Depth values for each point are obtained using the RealSense API and converted to 3D coordinates.

4. **Code Functionality:**
   - **Initialization:** Sets up the camera and retrieves depth stream intrinsics.
   - **Frame Capture:** Continuously captures frames from the camera.
   - **Distance Calculation:** Converts pixel coordinates to 3D coordinates and calculates the distance between the two points.
   - **Display:** Shows the color and depth images with the two points highlighted and connected by a line.
   - **Exit:** The application runs until the user presses the 'q' key.
  
## How to Run

1. **Install Dependencies:**
   - Ensure Python is installed. Then, install the required libraries using pip:
     ```sh
     pip install opencv-python numpy pyrealsense2
     ```

2. **Connect the Intel RealSense Camera:**
   - Connect your Intel RealSense D457 camera to your computer via USB.

3. **Run the Code:**
   - Save the provided Python script to a file, for example, `distance_measurement.py`.
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is saved.
   - Run the script using Python:
     ```sh
     python distance_measurement.py
     ```

4. **Exit the Application:**
   - The application will display the color and depth images with highlighted points and the distance between them.
   - Press 'q' to stop the application and close the windows.
