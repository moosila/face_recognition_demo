import os
from pygame import mixer
import time
import cv2
from gtts import gTTS
import face_recognition

known_face_encodings = [
]

known_face_names = [
]


# assign directory
directory = './img/known'
for filename in os.listdir(directory):
  f = os.path.join(directory, filename)
  if os.path.isfile(f) and not filename.startswith('.'):
    name_of_person = os.path.splitext(filename)[0]
    image_of_person = face_recognition.load_image_file(f)
    person_face_encoding = face_recognition.face_encodings(image_of_person)[0]
    known_face_encodings.append(person_face_encoding)
    known_face_names.append(name_of_person)

samePerson = ""

# Load Camera
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    test_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)    

    # Find faces in test image
    face_locations = face_recognition.face_locations(test_image)
    face_encodings = face_recognition.face_encodings(test_image, face_locations)

    # Loop through faces in test image
    for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        
        time.sleep(0.25)
        name = "Buddy"

        # If match
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Greet the person(s)
        if name != samePerson:
            greet_message = "සිද්ධි රස්තු %s!" % (name)
            samePerson = name

            print (greet_message)
            
            # audio greet
            tts = gTTS(greet_message,"lk", "si")
            tts.save('greeting.mp3')
            mixer.init()
            mixer.music.load("greeting.mp3")
            mixer.music.play()
            while mixer.music.get_busy():  # wait for music to finish playing
                time.sleep(1)            
            mixer.music.unload()
            mixer.quit()
        
    key = cv2.waitKey(1)
    if key == 27:
        break

