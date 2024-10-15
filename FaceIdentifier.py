import face_recognition
import cv2

# Load the reference image of John and encode it
john_image = face_recognition.load_image_file("assets/john.jpg")
john_encoding = face_recognition.face_encodings(john_image)[0]  # Get the encoding of John's face

# Create a list of known face encodings and their corresponding names
known_face_encodings = [john_encoding]
known_face_names = ["John"]

# Load the image in which you want to detect John
test_image = face_recognition.load_image_file("assets/isolate.jpg")

# Find all face locations and encodings in the test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Convert the test image from RGB (face_recognition) to BGR (OpenCV)
test_image_bgr = cv2.cvtColor(test_image, cv2.COLOR_RGB2BGR)

# Loop through each face found in the test image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # Compare the detected face encoding to known faces
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    
    name = "Unknown"  # Default name if no match is found

    # If a match is found, use the known name
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw a rectangle around the face
    cv2.rectangle(test_image_bgr, (left, top), (right, bottom), (0, 255, 0), 2)
    # Display the name below the face
    cv2.putText(test_image_bgr, name, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# Display the image with the results
cv2.imshow("Detected Faces", test_image_bgr)

# Wait until a key is pressed and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
