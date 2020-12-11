"""
   This Function change speech to Text.
"""
import speech_recognition as sr
def take_string ():
    Rg=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening---")
        Rg.pause_threshold=1
        audio = Rg.listen(source)
    try:
        print("Recording---")
        query=Rg.recognize_google(audio,language='en-in')
        print(f'User say---{query}\n')
    except Exception as e:
        print('Say!Error\n',e)
        return 'None'
    return query
print(take_string().lower())
# Make by vineet krishna gupta.