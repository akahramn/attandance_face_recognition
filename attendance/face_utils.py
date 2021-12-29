import cv2
import face_recognition
import numpy as np


def take_snap():
    cap = cv2.VideoCapture(0)  # video capture source camera (Here webcam of laptop)
    ret, frame = cap.read()  # return a single frame in variable `frame`

    # cv2.imshow('img1', frame)  # display the captured image
    cv2.imwrite('images/c1.png', frame)
    # cv2.destroyAllWindows()
    cap.release()


def recognize_faces():
    adem_image = face_recognition.load_image_file("Adem.jpeg")
    hazar_image = face_recognition.load_image_file("Hazar.jpeg")
    abdullah_image = face_recognition.load_image_file("Abdullah.jpeg")
    ceren_image = face_recognition.load_image_file("Ceren.jpeg")
    unknown_image = face_recognition.load_image_file("images/c1.png")

    try:
        adem_face_encoding = face_recognition.face_encodings(adem_image)[0]
        hazar_face_encoding = face_recognition.face_encodings(hazar_image)[0]
        abdullah_face_encoding = face_recognition.face_encodings(abdullah_image)[0]
        ceren_face_encoding = face_recognition.face_encodings(ceren_image)[0]
        unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
    except IndexError:
        print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
        quit()

    known_faces = [
        adem_face_encoding,
        hazar_face_encoding,
        abdullah_face_encoding,
        ceren_face_encoding,
    ]

    known_face_names = [
        "Adem",
        "Hazar",
        "Abdullah",
        "Ceren"
    ]

    matches = face_recognition.compare_faces(known_faces, unknown_face_encoding)
    a = ["0", "1", "2", "1"]
    indexes = [index for index in range(len(matches)) if matches[index] == True]
    result = []

    for x in indexes:
        result.append(known_face_names[x])

    return result
