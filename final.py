import speech_recognition as sr
import cv2

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Speech recognition using Google Speech Recognition
try:
    print("You said: " + r.recognize_google(audio), language='ko')
    if r.recognize_google(audio)=='카메라':
        cap = cv2.VideoCapture(0)

        while True:
        # 카메라 연결 여부(True/False)와 현재 프레임 이미지를 읽음
            retval, frame = cap.read()
    
        # 만약 카메라가 연결되어 있지 않으면 while 반복문 종료
            if retval == False:
                break
    
    # 'camera'이란 창 이름으로 현재 프레임 출력
            cv2.imshow('camera', frame)

    # 10초가 지나거나, ESC 키가 입력되면 while 반복문 종료
            if cv2.waitKey(10) == 27:
                break

    # step4.카메라 닫고 모든창 종료
        cap.release()

        cv2.destroyAllWindows()
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
