import cv2

def list_webcams(max_cameras=10):
    available_cameras = []
    
    for index in range(max_cameras):
        # Try to open the webcam
        video_capture = cv2.VideoCapture(index)
        
        if video_capture.isOpened():
            available_cameras.append(index)
            print(f"Webcam available at index: {index}")
            video_capture.release()  # Release the camera
        else:
            print(f"No webcam found at index: {index}")
    
    return available_cameras

# Call the function to list available webcams
cameras = list_webcams()
print("Available webcams:", cameras)