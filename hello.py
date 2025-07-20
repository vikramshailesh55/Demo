import speech_recognition as sr

# Create a speech recognition object
r = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Try to recognize the speech
try:
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand your audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))