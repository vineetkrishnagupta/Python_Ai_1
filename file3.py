""""
 This Function Change Text To Speech.
"""
import pyttsx3
def speak(audio):
    eng = pyttsx3.init("sapi5")
    vos = eng.getProperty("voices")
    eng.setProperty("voice", vos[0].id)
    eng.say(audio)
    eng.runAndWait()
if __name__=="__main__":
    speak("What is your name")
#Makeby vineet krishna gupta.