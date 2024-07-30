import cv2.data
import numpy as np
import cv2
import pyrealsense2 as rs

# Kamera akışını başlat
pipeline = rs.pipeline()
config = rs.config()
# Renk ve derinlik akışlarını yapılandır
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Kamera başlat
pipeline.start(config)
#Kalibrasyon
profile = pipeline.get_active_profile()
depth_sensor = profile.get_device().first_depth_sensor()
depth_stream = depth_sensor.get_stream_profiles()[0].as_video_stream_profile()
intrinsics = depth_stream.get_intrinsics()



yuz_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
while(True):
    frame = pipeline.wait_for_frames()
    color_frame = frame.get_color_frame()    

    color_image = np.asanyarray(color_frame.get_data())    

    if not color_frame:
        continue


    gray = cv2.cvtColor(color_image,cv2.COLOR_BGR2GRAY)
    # YUZLER CIKTISI (X,Y,width,height)
    yuzler = yuz_cascade.detectMultiScale(gray,1.3,5)
    

    for i,(x,y,w,h) in enumerate(yuzler):
        if i == 0:
            color = (0,0,255)
        elif i == 1:
            color = (0,255,0)
        else:
            color = (255,0,0)
            
        cv2.rectangle(color_image,(x,y),(x+w,y+h),color,2)    
        


    print(len(yuzler))

    cv2.imshow("title" ,color_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

pipeline.stop()
cv2.destroyAllWindows()