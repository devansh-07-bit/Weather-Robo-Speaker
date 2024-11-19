import pyttsx3 #pip install pyttsx3
#it is used for converting the text to speech

if __name__=="__main__": # used to ensure that a block of code is only executed when the Python file is run directly, not when it is imported as a module in another file.
    print("Welcome to the Robospeaker 1.1. created by Devansh")

   #pyttsx3.init(): Initializes the speech engine.
   # engine.say(x): Sets the text you entered (x) to be spoken.
   # engine.runAndWait(): Waits for the speech engine to finish speaking the input text.


    while True:
        x = input("Enter What you want me to speak ")
        if x=="stop":
            engine.say("Bye Bye System")
            break
        engine = pyttsx3.init()  # Initialize the TTS engine
        engine.say(x)  # Set the text to be pronounced
        engine.runAndWait()  # Run the speech engine to pronounce the text
