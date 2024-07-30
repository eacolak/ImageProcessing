# Distance between two points

#Using OpenCV, NumPy and the pyrealsense2 libraries, I will leverage my existing depth sensor camera, the Intel RealSense D457, to calculate the distance between two pixels provided in the code.
#This calculation will determine their depths in the X, Y, and Z planes in meters using sensor data. Subsequently, I will use the 3D distance formula:
#√((x₂ - x₁)² + (y₂ - y₁)² + (z₂ - z₁)²)
#to find and display the distance between the two points. This project is my first endeavor in image processing during my internship.
#In this project, I aim to process the data obtained from the depth sensor camera to calculate the real-world distance between two pixels in an image. 
#Such calculations are crucial in many image processing applications, such as object detection and measurement. The goal of my project is to use image data to make accurate and precise distance measurements.



import pyrealsense2 as rs
import numpy as np
import cv2

#3 boyutlu düzlemde uzaklık formülü 
def uzaklikAl(p1,p2):
    veri1 = ((p2[0]-p1[0])**2) + ((p2[1]-p1[1])**2) + ((p2[2]-p1[2])**2) 
    newUzaklik = np.sqrt(veri1)
    return newUzaklik

# Kamera akışını başlat
pipeline = rs.pipeline()
config = rs.config()


# Renk ve derinlik akışlarını yapılandır
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Kamera başlat
pipeline.start(config)

profile = pipeline.get_active_profile()
depth_sensor = profile.get_device().first_depth_sensor()
depth_stream = depth_sensor.get_stream_profiles()[0].as_video_stream_profile()
intrinsics = depth_stream.get_intrinsics()

try:
    while True:
        # Yeni bir veri seti al
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

        if not color_frame or not depth_frame:
            continue
        
        # Derinlik görüntüsünü numpy dizisine dönüştür
        depth_image = np.asanyarray(depth_frame.get_data())

        # İki nokta belirleyin
        point1 = (300, 240)  # x, y
        point2 = (400, 240)  # x, y

        #Z düzlemi hesaplandı
        p1dist = depth_frame.get_distance(300,240)
        p2dist = depth_frame.get_distance(400,240)

        # İki nokta arasındaki uzaklığı hesaplayın PİXEL
        delta_x = point2[0] - point1[0]
        delta_y = point2[1] - point1[1]


        distanceX = depth_frame.get_distance(point1[0], point1[1])
        point3Dx = rs.rs2_deproject_pixel_to_point(intrinsics,[point1[0] ,point1[1]],distanceX)
        
        distanceY = depth_frame.get_distance(point2[0], point2[1])
        point3Dy = rs.rs2_deproject_pixel_to_point(intrinsics,[point2[0] ,point2[1]],distanceY)


        #Sadece z yazdırdıgım yer
        #print(f"point1: {p1dist} ,/// point2: {p2dist}")


        #Total distance print
        print(f"Distance between two points: ({uzaklikAl(point3Dx,point3Dy)})M")
        print(f"Y point distance: ({point3Dy[0]}M,{point3Dy[1]}M,{point3Dy[2]})M")
        print(f"X point distance: ({point3Dx[0]}M,{point3Dx[1]}M,{point3Dx[2]})M")

        # Görüntüler
        color_image = np.asanyarray(color_frame.get_data())
        cv2.circle(color_image, point1, 5, (0, 255, 0), -1)  # Yeşil
        cv2.circle(color_image, point2, 5, (0, 0, 255), -1)  # Kırmızı
        cv2.line(color_image, point1, point2, (255, 0, 0), 2)  # Mavi

        #Kamera sekmesi
        cv2.imshow('Color Image', color_image)
        cv2.imshow('Depth İmage' ,depth_image)

        # 'q' tuşuna basılarak çıkış yap
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

finally:
    # Kamera akışını durdur
    pipeline.stop()
    cv2.destroyAllWindows()
