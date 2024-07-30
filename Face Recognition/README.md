# Face Detection with Intel RealSense D457

This project demonstrates face detection using the Intel RealSense D457 depth camera along with OpenCV and the `pyrealsense2` library. The following code captures video from the camera, processes it to detect faces, and visualizes the results.

## Overview

1. **Libraries Used:**
   - `cv2` (OpenCV): For image processing and face detection.
   - `numpy`: For handling image data.
   - `pyrealsense2`: For interfacing with the Intel RealSense depth camera.

2. **Camera Setup:**
   - The Intel RealSense D457 camera is configured to stream both color and depth data at a resolution of 640x480 pixels and 30 frames per second (fps).

3. **Face Detection:**
   - OpenCV’s Haar cascade classifier is used to detect faces in the color frames captured by the camera.
   - Detected faces are highlighted with rectangles in different colors based on their order.

4. **Code Functionality:**
   - **Initialization:** Sets up the camera and loads the face detection model.
   - **Frame Capture:** Continuously captures frames from the camera.
   - **Face Detection:** Processes each frame to detect faces and draw bounding boxes around them.
   - **Display:** Shows the processed video feed with detected faces highlighted.
   - **Exit:** The application runs until the user presses the 'q' key.

## How to Run

1. **Install Dependencies:**
   - Make sure you have Python installed. Then, install the required libraries using pip:
     ```sh
     pip install opencv-python numpy pyrealsense2
     ```

2. **Connect the Intel RealSense Camera:**
   - Connect your Intel RealSense D457 camera to your computer via USB.

3. **Run the Code:**
   - Save the provided Python script to a file, for example, `face_detection.py`.
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is saved.
   - Run the script using Python:
     ```sh
     python face_detection.py
     ```

4. **Exit the Application:**
   - The application will run and display a window with the live video feed and detected faces.
   - Press 'q' while the window is focused to stop the application and close the window.

## Notes

- Ensure that the Intel RealSense SDK and drivers are properly installed and configured.
- The `haarcascade_frontalface_default.xml` file must be available in the OpenCV data directory.
