import face_recognition
known_image = face_recognition.load_image_file("images/1.jpg")
unknown_image = face_recognition.load_image_file("images/1.jpg")

image1_encoding = face_recognition.face_encodings(known_image)[0]
image2_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([image1_encoding], image2_encoding)

print(results)

print(image1_encoding)
print(image2_encoding)