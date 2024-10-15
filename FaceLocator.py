import face_recognition
import cv2

image = face_recognition.load_image_file("assets/image.jpg")

face_locations = face_recognition.face_locations(image)


print("Found {} face(s) in this photograph.".format(len(face_locations)))
#Prints face location tuple in RGB
print(face_locations)

# Convert the image from RGB (face_recognition) to BGR (OpenCV) format
image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# Draw rectangles around each face
for (top, right, bottom, left) in face_locations:
    cv2.rectangle(image_bgr, (left, top), (right, bottom), (0, 255, 0), 2)

# Display the image with the faces
cv2.imshow("Detected Faces", image_bgr)



#Open window until key pressed
cv2.waitKey(0)
cv2.destroyAllWindows()