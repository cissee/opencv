import cv2
import face_recognition
import numpy as np
from database import get_connection

def register_user(name, role):
    conn = get_connection()
    cursor = conn.cursor()
    
    video_capture = cv2.VideoCapture(0)
    print("Placez votre visage devant la caméra...")

    while True:
        ret, frame = video_capture.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)

        if face_locations:
            face_encoding = face_recognition.face_encodings(rgb_frame, face_locations)[0]
            encoded_face = np.array(face_encoding).tobytes()

            cursor.execute("INSERT INTO users (name, role, encoding) VALUES (?, ?, ?)", (name, role, encoded_face))
            conn.commit()
            print(f"{name} enregistré avec succès !")
            break

    video_capture.release()
    cv2.destroyAllWindows()
    conn.close()

# Exemple d'enregistrement
if __name__ == "__main__":
    register_user("Alice", "Administrateur")
