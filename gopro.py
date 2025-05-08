import cv2

# 当GoPro进入UVC模式时，会被识别为普通摄像头
# 通常设备号为0或1，具体取决于你的系统
camera_index = 0  # 可能需要尝试0,1,2等

cap = cv2.VideoCapture(camera_index)

if not cap.isOpened():
    print("无法打开GoPro摄像头")
    exit()

# 设置分辨率（如果支持）
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    ret, frame = cap.read()
    if not ret:
        print("无法获取帧")
        break
    
    # 显示图像
    cv2.imshow('GoPro UVC Mode', frame)
    
    # 按'q'退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()