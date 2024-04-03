import cv2
from deepface import DeepFace

# Requirment: tensorflow, tf-keras ... pip install deepface 
# Reference: https://github.com/serengil/deepface

# To run, 
# python Facial_Expression_Recognition.py

# webcam 
cap = cv2.VideoCapture(0)  

frame_count = 0 

while True:
    ret, frame = cap.read()

    # Error 
    if not ret:
        print("Error")
        break

    cv2.imshow('Video', frame)

    # 30 fps -> 1s  
    if frame_count % 30 == 0: 
        try: 
            objs = DeepFace.analyze(img_path=frame, actions=['emotion'])
            print(objs[0]['dominant_emotion'])
            frame_count = 0 
        
        except:
            frame_count = 0
        
    frame_count += 1
    
    # press 'q' to quit 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
