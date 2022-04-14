import face_recognition
import cv2
import numpy as np


def take_snap():
    cap = cv2.VideoCapture(0)  # video capture source camera (Here webcam of laptop)
    ret, frame = cap.read()  # return a single frame in variable `frame`

    # cv2.imshow('img1', frame)  # display the captured image
    cv2.imwrite('images/c1.png', frame)
    # cv2.destroyAllWindows()
    cap.release()


def recognize_faces():
    abdullah_image = face_recognition.load_image_file("attendance/static/students/Abdullah.jpeg")
    ceren_image = face_recognition.load_image_file("attendance/static/students/Ceren.jpeg")
    aysun_image = face_recognition.load_image_file("attendance/static/students/aysun_eyiz.jpeg")
    murat_image = face_recognition.load_image_file("attendance/static/students/murat_donmez.jpeg")
    arif_image = face_recognition.load_image_file("attendance/static/students/arif_mert_kılıç.jpeg")
    enes_image = face_recognition.load_image_file("attendance/static/students/enes_yıldızoglu.jpeg")
    unknown_image = face_recognition.load_image_file("images/c1.png")

    try:
        abdullah_face_encoding = face_recognition.face_encodings(abdullah_image)[0]
        ceren_face_encoding = face_recognition.face_encodings(ceren_image)[0]
        aysun_face_encoding = face_recognition.face_encodings(aysun_image)[0]
        murat_face_encoding = face_recognition.face_encodings(murat_image)[0]
        arif_face_encoding = face_recognition.face_encodings(arif_image)[0]
        enes_face_encoding = face_recognition.face_encodings(enes_image)[0]
        unknown_face_encodings = face_recognition.face_encodings(unknown_image)
    except IndexError:
        print("I wasn't able to locate any faces in at least one of the unknown_images. Check the image files. Aborting...")
        quit()

    known_faces = [
        abdullah_face_encoding,
        ceren_face_encoding,
        aysun_face_encoding,
        murat_face_encoding,
        arif_face_encoding,
        arif_face_encoding,
        enes_face_encoding,
    ]

    known_face_names = [
        "Abdullah Kahraman",
        "Ceren Gülmez",
        "Aysun Eyiz",
        "Murat Dönmez",
        "Arif Mert Kılıç",
        "Enes Yıldızoğlu",
    ]
    result = []

    for unknown_face_encoding in unknown_face_encodings:
        matches = face_recognition.compare_faces(known_faces, unknown_face_encoding)
        result.append(known_face_names[matches.index(True)])
        print("Matches=", matches)


    return result
