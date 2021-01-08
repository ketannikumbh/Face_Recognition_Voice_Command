##pip install cmake
##pip install dlib
##pip install face-recognition
##pip install pyttsx3
##pip install SpeechRecognition
##pip install DateTime
##pip install opencv-python
##pip install requests
##pip install wikipedia
##pip install smtplib
##pip install urllib3
##Anshul Sir Image Url ('https://i.imgur.com/eOH6HSX.png')
import face_recognition
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import smtplib
import urllib.request
import sys

print("""                               
                                                                    
                     ( )_ ____                ___.--'   `--(  
                     //      \      __.------'              ||
                    //        `----'                        ||
                   //                                       ||
                  //                                        ||
                 //       WELCOME TO OUR PROJECT            ||
   ,,,,,        //                                  ,,,,,   ||
  ;;;;;\      ,/(_/                                ;;;;;\   ||
  ';;C '\   .'//     ____                    /--'-'';;C '\-\|-:
   );  _) .' //\____'    `----.____.--`\----'       );  _)  / :
 .'=. (  '/|//                                    .'=. (   / /
|   )`-\.' __/                                    |   )`-\/ /|
\   \ ,'\///                                      \   \ /  /||
 ;.  '  ///                                        ;.  '  / ||
 | `._,'//                                         | `._,'|-||:
 \     //                                          \      )-||:
  )===//]                                           )=====] ||
 /   // \                                          /       \||
 \_ (/   |                                         \_      )||
  \      |\                                        \\      |
  \      | \                                        \\     |
  |      |  )                                       ||     /
  |     /  /                                        ||    |
   \    | /                                         \\    |
   |    |/                                          ||    |
  /|    |                                           ||    |
 /\|    |                                           ||    |
/`.|    |                                           ||    |
`=.[____)                                           |[___/
    )  '`--.                                        ))  '`--.
    `='===='                                        ``='===='

------------------------------------------------


""")

img_url=input("Enter your Image Online URL Link ; Just Paste Here :\n ")

def image_download(url):
    
    fullname = "name" + ".jpg"
    urllib.request.urlretrieve(url, fullname)
    
print("Welcome To Our Program \n")

print("Please Wait Camera is loading \n")

print("Notice : You Need To close camera by pressing ESC !! \n")

image_download(img_url )

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
    elif k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break;
        
cv2.destroyAllWindows()
cam.release()


        
print('Welcome to our login page !!\n')

print("""
 __^__                                                        __^__
( ___ )------------------------------------------------------( ___ )
 | / |                                                        | \ |
 | / |                                                        | \ |
 |___|                                                        |___|
(_____)------------------------------------------------------(_____)

""")

print("\nPlease wait , We are authorizing you !\n")
print("LOADING !!! HAVE PATIENCE\n")
#inserting image of first person

image_of_firstperson = face_recognition.load_image_file("name.jpg")
firstperson_face_encoding = face_recognition.face_encodings(image_of_firstperson)[0]

#CHECKING FOR UNKNOWN IMAGE WITH INSERTING IMAGE FOR ACCESS GRANTED

unknown_image = face_recognition.load_image_file("opencv_frame_0.png")
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

# Compare faces
results = face_recognition.compare_faces(
    [firstperson_face_encoding], unknown_face_encoding)

if results[0]:
    os.remove("opencv_frame_0.png")
    os.remove("name.jpg")
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    
    def speak(audio):
        engine.say(audio)
        print(audio)
        engine.runAndWait()
    speak("ACCESS GRANTED ! WELCOME TO THE WORLD OF ARTIFICIAL INTELLIGENCE")
    
    def speak(audio):
        engine.say(audio)
        print(audio)
        engine.runAndWait()

    def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source: 
            print("listening...")
            r.pause_threshold = 2
            audio = r.listen(source,timeout=4,phrase_time_limit=5)

            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='en-in')
                print(f"user said: {query}")

            except Exception as e:
                speak("Say that again please...")
                return "none"
            return query

    def sendEmail(to,content):
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login('aichandigarh58@gmail.com', 'Aichandigarh2')
        server.sendmail('aichandigarh58@gmail.com', to, content)
        server.quit()
        

    def wish():
        hour= int(datetime.datetime.now().hour)
        if hour >=0 and hour <=12:
            speak("good morning")
        elif hour>12 and hour<18:
            speak("good afternoon")
        else:
            speak("good afternoon")
        speak("I am your assistant sir, please tell me how can i help you")

    if __name__== "__main__":
        wish()
        while True:

            query = takecommand().lower()

            if"open notepad" in query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)

            elif"open command prompt" in query:
                os.system("start cmd")

            elif "play music" in query:
                webbrowser.open("https://www.youtube.com/watch?v=SjFPM1ecDCA")
            elif "open camera" in query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()

            elif "ip address" in query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "wikipedia" in query:
                speak("searching wikipedia....")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                speak(results)

            elif "open youtube" in query:
                webbrowser.open("www.youtube.com")

            elif "open facebook" in query:
                webbrowser.open("www.facebook.com")

            elif "open blackboard" in query:
                webbrowser.open("https://cuchd.blackboard.com/")

            elif "open google" in query:
                speak("sir, what should i search on google")
                cm = takecommand().lower()
                webbrowser.open(f"{cm}")
                
            elif "send email" in query:
                try:
                    speak("what should i say?")
                    content = takecommand().lower()
                    to = input("Please Enter Email ID : \n")
                    sendEmail(to,content)
                    speak("Email has been sent")
                except Exception as e:
                    print(e)
                    speak("sorry sir, i am not able to sent this mail")
           
            elif "no thanks" in query:
                speak("thanks for using me sir, have a good day.")
                sys.exit()

            speak("sir, do you have any other work")

            
else:
    print('ACCESS DENIED !!!')
    os.remove("opencv_frame_0.png")
    os.remove("name.jpg")
    
    



