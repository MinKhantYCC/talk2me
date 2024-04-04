# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3 

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.setProperty("voice", 0.5)
    engine.say(command) 
    engine.runAndWait()
	
# Loop infinitely for user to
# speak
def listen(lang=None):
    MyText = ""
    # Exception handling to handle
    # exceptions at the runtime
    try:
        # use the microphone as source for input.
        with sr.Microphone() as source2:	
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            print("Adjusting Noise....", end="")
            r.adjust_for_ambient_noise(source2, duration=0.2)
            print("Done")
            #listens for the user's input 
            print("Listening...")
            audio2 = r.listen(source2)
            
            # Using google to recognize audio
            if lang == None:
                MyText = r.recognize_google(audio2)
            else:
                MyText = r.recognize_google(audio2, language=lang)
            MyText = MyText.lower()
            return str(MyText)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        
    except sr.UnknownValueError:
        print("unknown error occurred")
    return None